# AgentIR: Agent-Assisted Incident Response with RAG

AgentIR is a Python-based incident response prototype that demonstrates how a retrieval-augmented generation (RAG) workflow can support analyst triage.

The project ingests analyst questions, retrieves relevant response playbooks from a local corpus using embedding-based semantic search, ranks response procedures by similarity, and uses the OpenAI API to generate grounded incident summaries and triage recommendations.

This repository is a public sample of the current project intended to show the core architecture and implementation approach.

## Why This Repo Is Only a Sample

This repository is intentionally limited to a sanitized public prototype.

The full project is developed beyond this baseline and includes more advanced orchestration logic, expanded evaluation workflows, and product-oriented incident response features. To avoid exposing proprietary implementation details or future project components, only the core sample pipeline is published here.

## What This Prototype Demonstrates

- AI agent-assisted incident response workflow for analyst-facing triage support
- Retrieval-augmented generation (RAG) for playbook lookup and context injection
- Playbook-based chunking for cleaner retrieval than fixed character-only chunking
- Embedding-based semantic search over incident response procedures
- OpenAI API integration for grounded response synthesis
- Local, reproducible baseline implementation in Python

## Scope

- Ingest a local markdown corpus of incident response playbooks
- Chunk playbooks by markdown section (`## ...`) or by fixed characters
- Generate embeddings for playbook chunks and analyst queries
- Rank chunks using cosine similarity
- Build a grounded prompt from the top-k retrieved chunks
- Generate a response using the OpenAI API, or print the prompt if no API key is configured

The included corpus covers:

- Phishing
- Impossible travel
- Malware beaconing

## Project Structure

- `scripts/IR_rag.py`: main sample RAG pipeline
- `scripts/phase0_rag.py`: earlier baseline version
- `rag/corpus/playbook_response.md`: sample incident response corpus
- `.env`: local environment file for credentials (not committed)
- `requirements.txt`: Python dependencies

## Setup

Install dependencies from the project root:

```powershell
pip install -r requirements.txt
```

Create a local `.env` file in the project root:

```env
PUT YOUR KEY HERE
```

`.env` is excluded from version control and should never be committed.

## Run

From the project root:

```powershell
python scripts/IR_rag.py --query "What should I do after an impossible travel alert?"
```

From the `scripts` directory:

```powershell
python IR_rag.py --query "What should I do after an impossible travel alert?"
```

Optional: use fixed-size character chunking instead of playbook-based chunking:

```powershell
python scripts/IR_rag.py --chunk-mode char --query "What should I do after an impossible travel alert?"
```
