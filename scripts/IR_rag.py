import argparse
import math
import os
from pathlib import Path
from typing import List, Sequence, Tuple

import numpy as np
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer


def read_text_file(file_path: Path) -> str:
    return file_path.read_text(encoding="utf-8")


def load_project_env() -> None:
    project_root = Path(__file__).resolve().parents[1]
    env_file = project_root / ".env"
    if env_file.exists():
        load_dotenv(dotenv_path=env_file)


def chunk_text(text: str, chunk_size: int) -> List[str]:
    return [text[i : i + chunk_size] for i in range(0, len(text), chunk_size)]


def chunk_markdown_playbooks(text: str) -> List[str]:
    lines = text.splitlines()
    chunks: List[str] = []
    current_title = ""
    current_body: List[str] = []

    for line in lines:
        if line.startswith("## "):
            if current_title:
                chunk = f"{current_title}\n" + "\n".join(current_body).strip()
                chunks.append(chunk.strip())
            current_title = line.strip()
            current_body = []
        else:
            if current_title:
                current_body.append(line)

    if current_title:
        chunk = f"{current_title}\n" + "\n".join(current_body).strip()
        chunks.append(chunk.strip())

    return [chunk for chunk in chunks if chunk]


def get_embedding_model(model_name: str) -> SentenceTransformer:
    return SentenceTransformer(model_name)


def get_embeddings(embed_model: SentenceTransformer, text: str) -> List[float]:
    return embed_model.encode(text, normalize_embeddings=False).tolist()


def dot_product(vec1: Sequence[float], vec2: Sequence[float]) -> float:
    return sum(a * b for a, b in zip(vec1, vec2))


def magnitude(vec: Sequence[float]) -> float:
    return math.sqrt(sum(v**2 for v in vec))


def cosine_similarity(vec1: Sequence[float], vec2: Sequence[float]) -> float:
    dot_prod = dot_product(vec1, vec2)
    mag_vec1 = magnitude(vec1)
    mag_vec2 = magnitude(vec2)

    if mag_vec1 == 0 or mag_vec2 == 0:
        return 0.0

    return dot_prod / (mag_vec1 * mag_vec2)


def top_k_chunks(
    query_embedding: Sequence[float],
    chunk_embeddings: Sequence[Sequence[float]],
    chunks: Sequence[str],
    k: int,
) -> List[Tuple[int, float, str]]:
    ratings = [cosine_similarity(query_embedding, emb) for emb in chunk_embeddings]
    k = min(k, len(ratings))
    if k <= 0:
        return []

    idx = np.argpartition(ratings, -k)[-k:]
    sorted_idx = sorted(idx.tolist(), key=lambda i: ratings[i], reverse=True)
    return [(i, ratings[i], chunks[i]) for i in sorted_idx]


def build_prompt(query: str, retrieved_chunks: Sequence[Tuple[int, float, str]]) -> str:
    context = "\n\n".join(
        [f"[Chunk {i} | score={score:.4f}]\n{chunk}" for i, score, chunk in retrieved_chunks]
    )
    return (
        "You are an incident response assistant. "
        "A question will be asked and relevant information is provided. "
        "Answer only using the provided information. "
        "If the answer is not present, say you do not have enough context.\n\n"
        f"Question: {query}\n\n"
        f"Relevant Information:\n{context}\n"
    )


def generate_prompt(prompt: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY") # Put your own API key in a .env file in the parent directory
    if not api_key:
        return (
            "OpenAI API key not found. Skipping model generation.\n\n"
            "Prompt preview:\n"
            f"{prompt}"
        )

    try:
        from openai import OpenAI
    except ImportError:
        return (
            "openai package not installed. Run `pip install openai` to enable generation.\n\n"
            "Prompt preview:\n"
            f"{prompt}"
        )

    client = OpenAI(api_key=api_key)
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
        temperature=0,
    )
    return response.output_text


def main() -> None:
    load_project_env()

    parser = argparse.ArgumentParser(description="Phase 0: simple RAG pipeline for IR context")
    parser.add_argument(
        "--corpus",
        type=Path,
        default=Path("rag/corpus/playbook_response.md"),
        help="Path to the source text corpus",
    )
    parser.add_argument("--query", type=str, required=True, help="User question")
    parser.add_argument("--chunk-size", type=int, default=400, help="Character chunk size")
    parser.add_argument(
        "--chunk-mode",
        choices=["playbook", "char"],
        default="playbook",
        help="Chunking strategy: one chunk per markdown playbook section or fixed characters",
    )
    parser.add_argument("--k", type=int, default=4, help="Top-K chunks to retrieve")
    parser.add_argument(
        "--embedding-model",
        type=str,
        default="BAAI/bge-small-en-v1.5",
        help="SentenceTransformer model name",
    )
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parents[1]
    corpus_path = args.corpus
    if not corpus_path.is_absolute():
        corpus_path = project_root / corpus_path

    text = read_text_file(corpus_path)
    if args.chunk_mode == "playbook":
        chunks = chunk_markdown_playbooks(text)
        if not chunks:
            chunks = chunk_text(text, args.chunk_size)
    else:
        chunks = chunk_text(text, args.chunk_size)

    embed_model = get_embedding_model(args.embedding_model)
    chunk_embeddings = [get_embeddings(embed_model, chunk) for chunk in chunks]

    query_embedding = get_embeddings(embed_model, args.query)
    retrieved = top_k_chunks(query_embedding, chunk_embeddings, chunks, args.k)

    print("Top chunks:")
    for i, score, _ in retrieved:
        print(f"- chunk={i}, score={score:.4f}")

    prompt = build_prompt(args.query, retrieved)
    output = generate_prompt(prompt)

    print("\n=== Model Output ===\n")
    print(output)


if __name__ == "__main__":
    main()
