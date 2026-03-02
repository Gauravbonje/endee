import streamlit as st
from endee import Endee
from sentence_transformers import SentenceTransformer
from groq import Groq

# 1. Page Configuration
st.set_page_config(page_title="CodeBuddy — AI RAG Search", layout="wide")

# 2. Resources Loading (Cached for M2 Speed)
@st.cache_resource
def load_resources():
    # Model runs on MPS (GPU) for M2 MacBook Air
    model = SentenceTransformer("all-MiniLM-L6-v2") 
    client = Endee("") 
    client.set_base_url("http://localhost:8080/api/v1")
    # Replace with your actual Groq Key
    groq_client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    return model, client, groq_client

model, client, groq_client = load_resources()

# 3. Sidebar for Stats
if st.button("Check Database Status"):
        try:
            idx = client.get_index("stackoverflow_qa")
            # Using .info() as per your initial working blueprint logic
            stats = idx.info() 
            st.write(f"Vectors Indexed: {stats.get('total_elements', 0)}")
        except Exception as e:
            st.error(f"Could not fetch stats: {e}")

# 4. RAG Logic Function
def get_ai_explanation(context, user_query):
    prompt = f"""
    You are a Senior Software Engineer. Fix the following programming error.
    
    Context from StackOverflow:
    {context}
    
    User Error:
    {user_query}
    
    Provide a concise, step-by-step fix and the corrected code snippet.
    """
    # Using the new model from your verified list
    chat_completion = groq_client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.1-8b-instant", 
    )
    return chat_completion.choices[0].message.content

# 5. Main UI
st.title("🔍 Semantic Code Error Search & AI Fix")
query = st.text_input("Describe your programming problem:", placeholder="e.g., java null pointer")

if query:
    with st.spinner("Retrieving solutions from Endee and generating AI fix..."):
        # Vector Search
        q_vec = model.encode(query, normalize_embeddings=True).tolist()
        index = client.get_index("stackoverflow_qa")
        results = index.query(vector=q_vec, top_k=3)

        if results:
            # Prepare context for RAG
            context_text = ""
            for r in results:
                context_text += f"Title: {r['meta'].get('title')}\nBody: {r['meta'].get('body')}\n---\n"

            # AI Generation
            ai_fix = get_ai_explanation(context_text, query)

            # Display AI Answer
            st.subheader("💡 AI Suggested Fix")
            st.success(ai_fix)

            # Display Reference Results
            st.subheader("📚 Related StackOverflow Discussions")
            for r in results:
                with st.expander(f"🎯 {r['meta'].get('title')} (Match: {r.get('similarity', 0.0):.2%})"):
                    st.write(r['meta'].get('body'))
                    st.markdown(f"[View Discussion](https://stackoverflow.com/questions/{r['id']})")
        else:
            st.warning("No relevant solutions found in the vector database.")