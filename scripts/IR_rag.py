import argparse
import json
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter

ALERT_FIXTURE_PATH = Path(r"tests\fixtures\impossible_travel_alert.json")


# Load project-level .env if present
def load_env() -> None:

    project_root = Path(__file__).resolve().parents[1]
    env_file = project_root / ".env"

    if env_file.exists():
        load_dotenv(env_file)


# Collect supported corpus files from a file path or directory
def collect_corpus_files(corpus_path: Path) -> list[Path]:

    if corpus_path.is_file():
        return [corpus_path]

    files: list[Path] = []
    for pattern in ("*.rst", "*.md", "*.txt"):
        files.extend(sorted(corpus_path.rglob(pattern)))  # add to list of corpus files

    return files


# Read corpus files and split them into chunked LangChain documents
def build_documents(corpus_path: Path, chunk_size: int) -> list[Document]:

    files = collect_corpus_files(corpus_path)

    if not files:
        raise ValueError(f"No corpus files found in: {corpus_path}")

    # Small overlap helps preserve context at chunk boundaries
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=80)  # KNOBS TO SET
    docs: list[Document] = []

    for file in files:

        text = file.read_text(encoding="utf-8")
        chunks = splitter.split_text(text)  # CHUNKING STAGE

        for i, chunk in enumerate(chunks):  # Store metadata of each chunk for ground truth
            docs.append(
                Document(
                    page_content=chunk,
                    metadata={"source": str(file), "chunk": i},
                )
            )

    return docs


# Convert FAISS distance to an easy-to-read similarity-like score
def similarity(distance: float) -> float:
    return 1.0 / (1.0 + float(distance))


# Load a hardcoded fixture alert and serialize it for prompt context
def load_alert_context() -> str:

    project_root = Path(__file__).resolve().parents[1]
    alert_path = project_root / ALERT_FIXTURE_PATH
    payload = json.loads(alert_path.read_text(encoding="utf-8"))

    return json.dumps(payload, indent=2)


# Render fallback prompt text when model generation is unavailable
def render_prompt_preview(query: str, docs: list[Document]) -> str:
    context = "\n\n".join(
        f"[source={d.metadata.get('source')} chunk={d.metadata.get('chunk')}]\n{d.page_content}"
        for d in docs
    )
    alert_context = load_alert_context()

    return (
        "You are an incident response assistant."
        "Answer only using the provided playbook context."
        "If the answer is not in context, say you do not have enough context.\n\n"
        f"Question: {query}\n\n"
        f"Alert Context (JSON):\n{alert_context}\n\n"
        f"Relevant Information:\n{context}\n"
    )


# Generate an answer from retrieved docs, or return prompt preview fallback
def generate_answer(query: str, docs: list[Document]) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    alert_context = load_alert_context()

    if not api_key:
        return (
            "OPENAI_API_KEY not found. Skipping generation.\n\nPrompt preview:\n"
            f"{render_prompt_preview(query, docs)}"
        )

    prompt = ChatPromptTemplate.from_template(
        "You are an incident response assistant."
        "Answer only using the provided playbook context."
        "If the answer is not in context, say you do not have enough context.\n\n"
        "Question: {input}\n\n"
        "Alert Context (JSON):\n{alert_context}\n\n"
        "Relevant Information:\n{context}"
    )

    llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0, api_key=api_key)
    chain = create_stuff_documents_chain(llm, prompt)  # sends prompt to LLM and returns model output

    return chain.invoke(
        {"input": query, "alert_context": alert_context, "context": docs}
    )  # query and context "stuffed" into prompt


# Execute retrieval + generation for one query
def run(query: str, corpus: Path, k: int, chunk_size: int, embedding_model: str) -> int:
    docs = build_documents(corpus, chunk_size)
    # Build a local vector index for semantic retrieval
    embeddings = HuggingFaceEmbeddings(model_name=embedding_model)
    vector_store = FAISS.from_documents(docs, embeddings)  # EMBEDDING STAGE

    results = vector_store.similarity_search_with_score(query, k=k)  # SIMILARITY STAGE

    top_docs = [doc for doc, _ in results]

    print("\nTop chunks:")
    for doc, dist in results:
        print(
            "- "
            f"score={similarity(dist):.4f} "
            f"source={doc.metadata.get('source')} "
            f"chunk={doc.metadata.get('chunk')}"
        )

    print("\n=== Model Output ===\n")
    print(generate_answer(query, top_docs))  # GENERATION STAGE

    return 0


# Create CLI parser for the minimal RAG pipeline
def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Minimal IR RAG pipeline")
    parser.add_argument("--query", required=True, help="Question to answer")
    parser.add_argument(
        "--corpus",
        type=Path,
        default=Path("rag/corpus"),
        help="Corpus file or directory (default: rag/corpus)",
    )
    parser.add_argument("--k", type=int, default=4, help="Top-k chunks to retrieve")
    parser.add_argument("--chunk-size", type=int, default=700, help="Chunk size")
    parser.add_argument(
        "--embedding-model",
        default="BAAI/bge-small-en-v1.5",
        help="Embedding model name",
    )
    return parser


# CLI entrypoint with path resolution and basic error handling
def main() -> int:
    load_env()
    args = build_parser().parse_args()

    project_root = Path(__file__).resolve().parents[1]
    corpus = args.corpus if args.corpus.is_absolute() else project_root / args.corpus

    try:
        return run(
            query=args.query,
            corpus=corpus,
            k=args.k,
            chunk_size=args.chunk_size,
            embedding_model=args.embedding_model,
        )
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
