CodeBuddy — AI-Powered RAG Search Engine

CodeBuddy is a production-grade Retrieval-Augmented Generation (RAG) system that helps developers solve programming errors using semantic intelligence instead of keyword search. It combines the Endee Vector Database for fast retrieval, SentenceTransformers for embeddings, and Groq Cloud LLMs for real-time AI explanations.

The system indexes thousands of real Stack Overflow questions and retrieves the most relevant context before generating grounded, accurate solutions.

Project Objective

Traditional search engines rely on keywords and fail when developers describe problems in natural language. CodeBuddy solves this by understanding semantic meaning and retrieving relevant programming solutions instantly.

This project demonstrates efficient information retrieval using Endee as the core engine.

Key Features

Large-Scale Retrieval
Indexed 50,000+ Stack Overflow questions using the pacovaldez/stackoverflow-questions dataset.

Semantic Search
Uses all-MiniLM-L6-v2 embeddings mapped into a 384-dimensional vector space.

AI-Generated Fixes
Integrates Groq Cloud (Llama-3-8B) to generate real-time solutions based on retrieved context.

Fast Search
Endee HNSW index performs nearest-neighbor search in milliseconds.

Memory Efficient
Uses INT8 quantization in Endee to reduce storage usage while maintaining accuracy.

Apple Silicon Optimized
Runs efficiently on MacBook Air M2 using PyTorch MPS acceleration.

Local Deployment
Runs entirely on a local Endee server with Docker support.

System Architecture

User enters programming error in natural language.

Query is converted into vector using SentenceTransformers.

Endee vector database performs nearest-neighbor search.

Top-k results are sent as context to Groq LLM.

Streamlit UI shows AI-generated solution and references.

Tech Stack

Vector Database
Endee Vector Database (INT8 Precision, HNSW Index)

Embedding Model
SentenceTransformers all-MiniLM-L6-v2

LLM Inference
Groq Cloud (Llama-3-8B-8192)

Frontend
Streamlit

Backend
Python 3.11+

Containerization
Docker Compose

Hardware
Apple Silicon M2 (MPS acceleration)

Dataset

Source
Stack Overflow questions dataset from Hugging Face.

Size
50,000 records indexed.

Topics Covered
Python errors
Java errors
C++ errors
React errors
General programming issues

This dataset covers most real-world developer problems.

Setup Instructions
1. Clone Repository
git clone https://github.com/Gauravbonje/endee.git
cd endee/projects/codebuddy
2. Create Virtual Environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
3. Start Endee Server

If using Docker:

docker compose up -d

If running locally:

cd ~/endee
./run.sh

Check server at:

http://localhost:8080/api/v1/index/list
4. Add Groq API Key

Create file:

.streamlit/secrets.toml

Add:

GROQ_API_KEY="your_api_key_here"
5. Index Dataset
python src/data_loader.py

This loads Stack Overflow dataset and builds the vector index.

6. Run Search Engine

Command line search:

python src/search_engine.py

Streamlit UI:

streamlit run app.py

Open browser at:

http://localhost:8501
Performance Metrics

Total indexed records: 50,000+
Search latency: under 5 ms
Embedding throughput: ~500 records/sec on M2
Storage precision: INT8 cosine similarity

Example Query

Input
"java null pointer error"

Output
Relevant Stack Overflow questions retrieved and AI-generated explanation provided.

Future Improvements

Index full Stack Overflow dataset
Add answer body and code snippets
Add multi-agent reasoning using CrewAI
Add evaluation metrics (precision, recall)
Deploy on cloud server
Add code auto-fix feature

Repository Structure
codebuddy/
│
├── app.py
├── src/
│   ├── data_loader.py
│   ├── search_engine.py
│   └── rag_engine.py
├── data/
├── docker-compose.yml
├── requirements.txt
└── README.md
Author

Gaurav Bonje
GitHub: https://github.com/Gauravbonje

Project: Endee Vector Database 

License

This project is for educational and research purposes.
It solves a real developer problem and showcases practical usage of vector databases in AI applications.
