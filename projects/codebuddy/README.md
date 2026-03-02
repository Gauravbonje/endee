# CodeBuddy — AI-Powered RAG Search Engine using Endee Vector Database
## 1. Project Overview

CodeBuddy is a production-grade Retrieval-Augmented Generation (RAG) system that helps developers solve programming errors using semantic intelligence instead of keyword search.

The system combines:

Endee Vector Database for fast semantic retrieval

SentenceTransformers for embedding generation

Groq Cloud LLMs for real-time AI explanations

CodeBuddy indexes real Stack Overflow questions and retrieves relevant context before generating grounded solutions.

This project demonstrates Efficient Information Retrieval using Endee as required in the assignment.

## 2. Problem Statement

Developers struggle to find solutions to programming errors.

Traditional search engines depend on keywords and often return irrelevant results.

Example:

Searching

# java null pointer error

may miss solutions titled
NullPointerException in Java.

Goal:

Build a semantic search system that understands the meaning of programming errors and retrieves relevant solutions using vector similarity search.

## 3. Solution Approach

CodeBuddy pipeline:

User Query → Embedding → Vector Search → Context Retrieval → AI Explanation

Components used:

SentenceTransformers to convert text into embeddings

Endee Vector Database to store embeddings

Semantic Search to retrieve similar programming errors

Groq Llama-3 LLM to generate explanations

Streamlit UI for interaction

## 4. How Endee is Used

Endee is the core vector database.

Steps performed:

Create index with dimension 384

Insert embeddings of Stack Overflow questions

Query using vector similarity search

Return closest matches

This demonstrates Efficient Information Retrieval using Endee HNSW indexing.

## 5. System Architecture

Frontend
Streamlit Web Interface

Backend
Python scripts using Endee SDK

Vector Engine
Endee running locally on port 8080

Embedding Model
SentenceTransformers all-MiniLM-L6-v2

LLM Engine
Groq Cloud Llama-3-8B-8192

## 6. Dataset

Source
Stack Overflow dataset from Hugging Face

Dataset Used
pacovaldez/stackoverflow-questions

Size
50,000 questions indexed

Topics Covered

Python errors
Java errors
C++ errors
React errors
General debugging problems

This dataset covers most real-world developer issues.

## 7. Repository Structure
projects/codebuddy/
│
├── app.py
├── src/
│   ├── data_loader.py
│   ├── search_engine.py
│   └── rag_engine.py
├── data/
│   └── stackoverflow_50k.json
├── docker-compose.yml
├── requirements.txt
└── README.md
## 8. Setup Instructions
Step 1 — Clone Repository
git clone https://github.com/Gauravbonje/endee.git
cd endee/projects/codebuddy
Step 2 — Create Virtual Environment
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Step 3 — Start Endee Server

If using Docker:

docker compose up -d

# If running locally:

cd ~/endee
./run.sh

Server will run at:

http://localhost:8080
# Step 4 — Add Groq API Key

Create file:

.streamlit/secrets.toml

Add:

GROQ_API_KEY="your_api_key_here"
Step 5 — Index Dataset
python src/data_loader.py

This embeds and inserts Stack Overflow questions into Endee.

# Step 6 — Run Search Engine

Command line search:

python src/search_engine.py

Streamlit UI:

streamlit run app.py

Open browser:

http://localhost:8501
## 9. Example Query

Input:

java null pointer error

Output:

Relevant Stack Overflow questions retrieved
AI-generated explanation with fix steps

Results are based on semantic similarity.

## 10. Performance Metrics

Total indexed records: 50,000+
Search latency: under 5 ms
Embedding throughput: ~500 records/sec on MacBook Air M2
Storage precision: INT8 cosine similarity

## 11. Technologies Used

Python
Endee Vector Database
SentenceTransformers
Groq Cloud Llama-3
Streamlit
NumPy
Docker

## 12. Future Improvements

Index full Stack Overflow dataset
Add accepted answers and code snippets
Add multi-agent reasoning system
Deploy on cloud server
Add automatic code-fix suggestions
Improve UI ranking

## 13. Mandatory Endee Repository Usage

Steps followed:

Starred official Endee repository

Forked Endee repository

Built project using forked repository

Repository Link
https://github.com/Gauravbonje/endee

## 14. Conclusion

CodeBuddy demonstrates practical use of Endee Vector Database to build an AI-powered semantic search and RAG system for solving developer problems.

The project showcases real-world application of vector databases and efficient information retrieval.

Author

Gaurav Bonje
GitHub: https://github.com/Gauravbonje

Project submitted for Endee Vector Database .
It solves a real developer problem and showcases practical usage of vector databases in AI applications.
