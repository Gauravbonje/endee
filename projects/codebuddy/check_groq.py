import os
from groq import Groq

# 1. Yahan apni Groq API Key daalein
GROQ_API_KEY = "YOUR_KEY_HERE_FOR_LOCAL_TESTING"

def verify_groq():
    try:
        # Client initialize karein
        client = Groq(api_key=GROQ_API_KEY)
        
        # 2. Available models ki list fetch karein
        models = client.models.list()
        
        print("✅ Success! Groq API is working.")
        print("\nAvailable Models for your Free Tier:")
        for model in models.data:
            print(f"- {model.id}")
            
        # 3. Ek chota test message bhej kar check karein
        print("\nTesting Llama3-8b response...")
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": "Hello Groq, is Llama3 ready for CodeBuddy?"}
            ],
            model="llama3-8b-8192", # Sabse fast aur free model
        )
        print(f"\nGroq Response: {chat_completion.choices[0].message.content}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    verify_groq()