import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

index = None
stored_chunks = []


def create_embeddings(chunks):
    global index, stored_chunks

    texts = [chunk["content"] for chunk in chunks]

    embeddings = model.encode(texts)
    embeddings = np.array(embeddings).astype("float32")

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    stored_chunks = chunks

    return len(stored_chunks)


def search_similar_chunks(question, top_k=3):
    global index, stored_chunks

    if index is None:
        return []

    question_embedding = model.encode([question])
    question_embedding = np.array(question_embedding).astype("float32")

    distances, indices = index.search(question_embedding, top_k)

    results = []
    for i in indices[0]:
        if i < len(stored_chunks):
            results.append(stored_chunks[i])

    return results
