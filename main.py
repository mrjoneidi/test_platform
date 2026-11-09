import json
from config import RAGPipelineConfig
from engine import RAGEngine

def main():
    # Load configuration
    print("Loading configuration from example_config.json...")
    with open("example_config.json", "r") as f:
        config_data = json.load(f)

    config = RAGPipelineConfig(**config_data)

    # Initialize Engine
    engine = RAGEngine(config)

    # 1. Ingest Data
    engine.ingest_documents(source="https://example.com/docs")

    # 2. Run initial query
    response1 = engine.run_query("How does the unified JSON schema work?")
    print(f"Response 1: {response1}\n")

    # 3. Run follow up query to test memory
    response2 = engine.run_query("Can you give me an example?")
    print(f"Response 2: {response2}\n")

if __name__ == "__main__":
    main()
