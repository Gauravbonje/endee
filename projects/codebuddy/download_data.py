from datasets import load_dataset

ds = load_dataset("pacovaldez/stackoverflow-questions", split="train[:50000]")

ds.to_json("data/stackoverflow_50k.json")
print("Saved 50k dataset")