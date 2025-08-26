# Retrieval-Augmented Generation (RAG) System

This project implements a Retrieval-Augmented Generation (RAG) system using FastAPI, ChromaDB, and GPT-4. The goal is to create a backend service capable of answering user questions by retrieving relevant information from a set of documents and generating responses using a language model.

## File structure

    RAG/
    ├── src/
    │   ├── main.py               # FastAPI application and endpoint definitions
    │   ├── config.py             # Configuration for environment variables and API keys
    │   ├── core/
    │   │   ├── retrieval.py      # Retrieval functions using FAISS
    │   |   ├── pipeline.py       # RAG pipeline combining retrieval and generation
    │   |   └── indexing.py       # Indexing steps setup
    |   |   └── model_emb.py      # How the model will embed data
    |   |   └── genaration.py     # Answer genaration process
    |   |   └── load_docs.py      # Which types of data or docs model will process
    │   ├── configs/
    │       ├── config.yaml               # Configuration for environment variables and API keys
    │       └── logging_config.yaml       # Store the logs of configs
    |
    │── data/
    │   └── csv/                  # Raw csv data for indexing
    |   └── pdf/                  # Raw pdf data for indexing
    |   └── processed/            # Folder for store the priocessed data in the vcetor database(chroma.sqlit3)
    │
    |__ pydantic_models/
    |   └── rag_model.py          # Defining the state of the model(question, context & answer)
    |
    ├── requirements.txt          # List of dependencies for the project
    ├── README.md                 # Project documentation
    ├── .env                      # Environment variables for API keys and configurations
    |__ main.py                   # FastAPI application and endpoint definitions
    |__ vector_index.py           # Preprocss the dataset for vector index

## Setup Instructions

Create a environment file

    python -m venv ragenv

activate ragenv

    ragenv\Scripts\activate

Install all the dependency

    pip install -r requirement.txt

## Store Data in Vector index

Need to run the _vector_index.py_ file for once for a dataset.

    python vector_index.py

This data then store in the _.data/processed_ folder as we mentioned in the _src/configs/config.yaml_ file _vector_store_manager_ setting. If trying to update the data, you need to delete the previous stored data from that directory(_chroma.sqlite3*file*&\_sibling_folder_).
Then run once again the above cmd.

## Conversation with bot

Once data is preprocessed & stored in the vector database. Now it's time to chat with bot. Run below cmd to continue converstation.

    python main.py
