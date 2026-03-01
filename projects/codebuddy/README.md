# CodeBuddy — Semantic Code Error Search using Endee Vector Database

## 1. Project Overview

CodeBuddy is an AI-powered semantic search system that helps developers find solutions to programming errors using natural language queries.

Instead of keyword matching, CodeBuddy understands the meaning of an error message and retrieves the most relevant solutions using vector embeddings and the Endee Vector Database.

This project demonstrates a practical use of Endee for Efficient Information Retrieval, fulfilling the assignment requirement.

---

## 2. Problem Statement

Developers often struggle to find solutions to programming errors.

Traditional search engines depend on keywords, which leads to irrelevant results.

Example:
Searching "java null pointer error" may miss solutions titled "NullPointerException in Java".

Goal:
Build a semantic search system that understands the meaning of errors and retrieves relevant solutions using vector similarity search.

---

## 3. Solution Approach

CodeBuddy uses:

- Sentence Transformers to convert text into embeddings
- Endee Vector Database to store embeddings
- Semantic Search to retrieve similar programming errors
- Streamlit UI for user interaction

Workflow:

User Query → Convert to Vector → Search in Endee → Return Similar Errors

---

## 4. How Endee is Used

Endee is used as the core vector database.

Steps:

1. Create Index with dimension 384
2. Insert embeddings of programming errors
3. Query using vector similarity
4. Return closest matches

This demonstrates Efficient Information Retrieval using Endee.

---

## 5. System Architecture

Frontend:
Streamlit UI

Backend:
Python scripts using Endee SDK

Vector Engine:
Endee running locally on port 8080

Embedding Model:
SentenceTransformers all-MiniLM-L6-v2

---

## 6. Repository Structure

projects/codebuddy/
│
├── app.py
├── src/
│   ├── data_loader.py
│   └── search_engine.py
├── requirements.txt
└── README.md

---

## 7. Setup Instructions

### Step 1 — Clone Repo

git clone https://github.com/Gauravbonje/endee.git
cd endee/projects/codebuddy

### Step 2 — Create Virtual Environment

python -m venv venv
source venv/bin/activate

### Step 3 — Install Dependencies

pip install -r requirements.txt

### Step 4 — Run Endee Server

cd ~/endee
./run.sh

Server will start at:
http://localhost:8080

### Step 5 — Load Sample Data

cd ~/endee/projects/codebuddy
python src/data_loader.py

### Step 6 — Run Search Engine

python src/search_engine.py

### Step 7 — Run UI

streamlit run app.py

---

## 8. Example Query

Input:
java null pointer error

Output:
NullPointerException in Java when calling method
How to use async await inside forEach loop
Python list index out of range error

Results are based on semantic similarity.

---

## 9. Technologies Used

Python
Endee Vector Database
Sentence Transformers
Streamlit
NumPy

---

## 10. Future Improvements

Load full StackOverflow dataset
Add Retrieval-Augmented Generation using LLM
Add Docker deployment
Improve UI and ranking
Add multi-language support

---

## 11. Mandatory Endee Repository Usage

Steps followed:

1. Starred official Endee repository
2. Forked Endee repository
3. Built project using forked repository

Repository Link:
https://github.com/Gauravbonje/endee

---

## 12. Conclusion

CodeBuddy demonstrates how Endee can be used to build an efficient AI-powered semantic search system.

It solves a real developer problem and showcases practical usage of vector databases in AI applications.
