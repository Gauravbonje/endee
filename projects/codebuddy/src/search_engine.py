from endee import Endee
from sentence_transformers import SentenceTransformer

# 🔹 1. Load Model
print("Initializing CodeBuddy Search Engine...")
model = SentenceTransformer("all-MiniLM-L6-v2")

# 🔹 2. Connect to Endee
client = Endee("")
client.set_base_url("http://localhost:8080/api/v1")

INDEX_NAME = "stackoverflow_qa"
index = client.get_index(INDEX_NAME)

def perform_search():
    print("\n" + "="*50)
    print("CodeBuddy — Semantic Search (Powered by Endee)")
    print("="*50)
    
    query = input("\nAsk your programming question: 👉 ")
    if not query.strip():
        return

    # 🔹 3. Vectorize Query [cite: 109, 111]
    query_vector = model.encode(query, normalize_embeddings=True).tolist()

    # 🔹 4. Query Endee HNSW Index [cite: 115]
    # top_k=5 provides enough variety for the UI [cite: 105]
    results = index.query(vector=query_vector, top_k=5)

    print(f"\n🔍 Top 5 Results for: '{query}'\n")

    # 🔹 5. Display Results [cite: 119]
    for i, r in enumerate(results, 1):
        meta = r.get("meta", {})
        title = meta.get("title", "No Title")
        similarity = r.get("similarity", 0.0) # [cite: 119, 122]
        
        print(f"{i}. 🎯 {title}")
        print(f"   Similarity: {similarity:.2%}")
        
        # Print tags if they exist
        tags = meta.get("tags", [])
        if tags:
            print(f"   Tags: {', '.join(tags)}")
        print("-" * 30)

if __name__ == "__main__":
    while True:
        perform_search()
        cont = input("\nSearch again? (y/n): ")
        if cont.lower() != 'y':
            break