# Dynamic RAG Platform

A modular, developer-first backend execution engine for a Dynamic RAG (Retrieval-Augmented Generation) Platform, built in Python.

This project implements an end-to-end technical specification covering all 6 core configuration phases of a RAG pipeline:
1. Data Ingestion & Source Connectors
2. Text Chunking & Preprocessing
3. Embedding & Vector Database (VDB)
4. Retrieval & Search Strategy
5. LLM Generation & Prompt Engineering
6. Chat Memory & Context Management

## Setup

Ensure you have Python installed. The project relies on `pydantic` for strict configuration validation.

```bash
pip install -r requirements.txt
```

## Running the Engine

You can execute a sample run of the pipeline using the provided mock runner and configuration:

```bash
python main.py
```

This will load `example_config.json`, initialize the pipeline phases, and execute a sequence of queries reflecting memory management, context retrieval, and generation stubs.

## Testing

Tests are written using `pytest`. To run tests:

```bash
pip install pytest
pytest test_engine.py
```

## Architecture

* `config.py`: Unified JSON Configuration schema using Pydantic models.
* `engine.py`: Core `RAGEngine` class orchestrating all phases.
* `ingestion.py`, `chunking.py`, `embedding.py`, `retrieval.py`, `generation.py`, `memory.py`: Modular classes dedicated to each of the 6 specification phases.
