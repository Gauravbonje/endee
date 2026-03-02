import json
from endee import Endee, Precision
from sentence_transformers import SentenceTransformer

# 🔹 1. Setup & Load Model
print("Loading all-MiniLM-L6-v2 on M2 MPS...")
model = SentenceTransformer("all-MiniLM-L6-v2") # [cite: 21, 52]

# 🔹 2. Connect to Endee
client = Endee("") # [cite: 73]
client.set_base_url("http://localhost:8080/api/v1") # [cite: 74]

INDEX_NAME = "stackoverflow_qa"

# 🔹 3. Create Index with INT8 Precision (4x Compression)
try:
    client.create_index(
        name=INDEX_NAME,
        dimension=384,          # Matches MiniLM output [cite: 80]
        space_type="cosine",    # Best for text similarity [cite: 81]
        precision=Precision.INT8 # Memory efficiency [cite: 82]
    )
    print(f"Index '{INDEX_NAME}' created successfully.")
except Exception:
    print(f"Index '{INDEX_NAME}' already exists.")

index = client.get_index(INDEX_NAME) # [cite: 84]

# 🔹 4. Load the 50k Dataset
# 🔹 4. Load the 50k Dataset (Fix for JSON Lines format)
print("Loading 50k dataset from JSON Lines...")
all_data = []
with open("data/stackoverflow_50k.json", "r") as f:
    for line in f:
        if line.strip():
            all_data.append(json.loads(line))

print(f"Successfully loaded {len(all_data)} records from file.")

# 🔹 5. Batch Processing (Optimized for M2 MPS)
# 🔹 5. Batch Processing (Optimized with unique IDs for M2 MPS)
BATCH_SIZE = 64 
print(f"Starting batch indexing (Total: {len(all_data)} records)...")

for i in range(0, len(all_data), BATCH_SIZE):
    batch = all_data[i : i + BATCH_SIZE]
    
    # Text combine for better semantic search [cite: 87, 90]
    texts = [f"{d.get('title', '')} {d.get('body', '')}" for d in batch]
    
    # Generate vectors using M2's MPS acceleration [cite: 52, 94]
    vectors = model.encode(texts, normalize_embeddings=True, batch_size=BATCH_SIZE)
    
    items = []
    for j, (doc, vec) in enumerate(zip(batch, vectors)):
        # 🟢 Unique ID fix: overall index (i) + batch offset (j)
        unique_id = str(i + j)
        
        items.append({
            "id": unique_id,
            "vector": vec.tolist(),
            "meta": {
                "title": doc.get("title", "No Title"),
                "body": doc.get("body", "")[:500], # Snippet for UI display [cite: 36]
                "tags": doc.get("tags", [])
            }
        })
    
    # Upsert to Endee in chunks of 100 [cite: 101, 207]
    index.upsert(items)
    
    if (i + BATCH_SIZE) % 640 == 0:
        print(f"Indexed {i + BATCH_SIZE} / {len(all_data)} records...")

print("50,000 records successfully indexed in Endee! ✅")