import json
import pytest
from config import RAGPipelineConfig
from engine import RAGEngine
from ingestion import Document

@pytest.fixture
def test_config():
    return RAGPipelineConfig(
        ingestion={"source_type": "api"},
        chunking={"strategy": "fixed_size", "chunk_size": 200},
        retrieval={"search_mode": "keyword"},
        memory={"strategy": "buffer", "window_size": 2}
    )

def test_config_parsing(test_config):
    assert test_config.ingestion.source_type == "api"
    assert test_config.chunking.strategy == "fixed_size"
    assert test_config.chunking.chunk_size == 200
    assert test_config.retrieval.search_mode == "keyword"
    assert test_config.memory.window_size == 2

def test_engine_initialization(test_config):
    engine = RAGEngine(test_config)
    assert engine.config == test_config
    assert engine.ingestor.config.source_type == "api"
    assert engine.chunker.config.strategy == "fixed_size"

def test_engine_run_query(test_config):
    engine = RAGEngine(test_config)

    # We do a mock run_query
    response = engine.run_query("Test query")

    assert "Mock response to" in response
    assert "Test query" in response

    # Ensure memory captured it
    assert len(engine.memory.history) == 1
    assert engine.memory.history[0][0] == "Test query"

def test_engine_memory_window(test_config):
    engine = RAGEngine(test_config)

    # Run 3 queries (window size is 2)
    engine.run_query("Q1")
    engine.run_query("Q2")
    engine.run_query("Q3")

    # The first one should have popped
    assert len(engine.memory.history) == 2
    assert engine.memory.history[0][0] == "Q2"
    assert engine.memory.history[1][0] == "Q3"
