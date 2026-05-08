# AgentIR: Incident Response RAG Prototype

AgentIR is a Python incident response prototype that uses retrieval-augmented generation (RAG) over local playbooks.

The current pipeline:
- loads local IR documentation from `rag/corpus`
- chunks and embeds documents
- retrieves top-k relevant chunks with FAISS
- injects a fixture alert JSON into the prompt
- generates a grounded answer (or prints a prompt preview when no API key is set)

## Current Scope

- Minimal single-query CLI workflow
- Local corpus support for `.rst`, `.md`, and `.txt`
- Embedding-based semantic retrieval (`BAAI/bge-small-en-v1.5` by default)
- LangChain-based retrieval and generation orchestration
- Hardcoded alert-context injection from `tests/fixtures/impossible_travel_alert.json`

## Project Structure

- `scripts/IR_rag.py`: main minimal RAG pipeline
- `rag/corpus/`: incident response corpus documents
- `tests/fixtures/`: sample alert JSON fixtures
- `.env`: local environment file for credentials (not committed)
- `requirements.txt`: Python dependencies

## Setup

From project root:

```powershell
pip install -r requirements.txt
```

Create `.env` in project root:

```env
OPENAI_API_KEY=your_key_here
```

If `OPENAI_API_KEY` is missing, the script skips model generation and prints a prompt preview.

## Run

From project root:

```powershell
python scripts/IR_rag.py --query "What should we do first for a ransomware incident?"
```

Common options:

```powershell
python scripts/IR_rag.py --query "..." --corpus rag/corpus --k 5 --chunk-size 700 --embedding-model BAAI/bge-small-en-v1.5
```

## Notes

- Retrieval scores shown in output are a simple transformed value from FAISS distance (`1 / (1 + distance)`) for readability.
- Alert JSON context is currently hardcoded in `scripts/IR_rag.py` via:
  - `ALERT_FIXTURE_PATH = Path(r"tests\\fixtures\\impossible_travel_alert.json")`

## Limitations

- The FAISS index is rebuilt on every run; there is no persisted index or warm start.
- Retrieval currently uses top-k vector search only; there is no reranking stage.
- Prompt context includes a single hardcoded alert fixture path instead of a runtime-selected alert file.
- Corpus ingestion is local file-based only (`.rst`, `.md`, `.txt`) with no metadata filtering layer.
- Grounding is best-effort via prompt instruction; there is no hard enforcement or citation validator.
- The script is single-query CLI oriented and not structured as a multi-user service/API.

## Evaluation Status (Current Gap)

- There is no formal evaluation harness in this repository at this time.
- No benchmark dataset is included for retrieval quality or answer quality scoring.
- No automatic metrics are tracked yet (for example: recall@k, MRR, faithfulness, answer correctness).
- No regression test suite currently validates output quality across corpus or prompt changes.
- Model behavior is not calibrated with human-graded rubrics in this repo.
