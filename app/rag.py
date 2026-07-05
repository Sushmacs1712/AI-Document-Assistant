import os
from groq import Groq
from dotenv import load_dotenv
from app.embedding import search_similar_chunks

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL = "llama-3.1-8b-instant"


def generate_answer(question):
    relevant_chunks = search_similar_chunks(question)

    if not relevant_chunks:
        return {
            "answer": "No document uploaded or no relevant content found.",
            "sources": []
        }

    context = "\n\n".join([chunk["content"] for chunk in relevant_chunks])

    prompt = f"""
Answer the question based only on the context below.

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    sources = [
        {
            "page": chunk["page"],
            "content": chunk["content"][:200]
        }
        for chunk in relevant_chunks
    ]

    return {
        "answer": response.choices[0].message.content,
        "sources": sources
    }