from pydantic import BaseModel
from app.rag import generate_answer
from fastapi import FastAPI, UploadFile, File
import os
from app.pdf_utils import extract_text_from_pdf, chunk_text
from app.embedding import create_embeddings

app = FastAPI(
    title="AI Document Assistant",
    description="RAG based PDF Question Answering API",
    version="1.0.0"
)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "AI Document Assistant API is running"}


@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    pages_text = extract_text_from_pdf(file_path)
    chunks = chunk_text(pages_text)
    total_vectors = create_embeddings(chunks)

    return {
       "message": "PDF processed and embeddings created successfully",
        "filename": file.filename,
        "total_pages": len(pages_text),
        "total_chunks": len(chunks),
        "total_vectors": total_vectors,
        "sample_chunk": chunks[0] if chunks else "No text found"
    }
@app.post("/ask")
def ask_question(request: QuestionRequest):
    result = generate_answer(request.question)
    return result