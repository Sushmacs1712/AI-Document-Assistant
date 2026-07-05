# 📄 AI Document Assistant

## Overview

AI Document Assistant is a Retrieval-Augmented Generation (RAG) application built using **Python** and **FastAPI**. It allows users to upload PDF documents and ask questions in natural language. The application extracts text from the uploaded PDF, generates embeddings, retrieves relevant content, and provides intelligent answers using the **Groq LLM**.

---

## Features

- 📄 Upload PDF documents
- ✂️ Extract and chunk PDF text
- 🧠 Generate embeddings
- 🔍 Retrieve relevant document context
- 💬 Answer questions using Groq LLM
- ⚡ FastAPI REST APIs
- 📚 Swagger API Documentation

---

## Tech Stack

- Python
- FastAPI
- Groq LLM
- Sentence Transformers
- FAISS Vector Database
- PyPDF2
- Uvicorn

---

## Project Structure

```text
AI-Document-Assistant/
│── app/
│   ├── embedding.py
│   ├── main.py
│   ├── pdf_utils.py
│   ├── rag.py
│── uploads/
│── requirements.txt
│── README.md
│── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Sushmacs1712/AI-Document-Assistant.git
cd AI-Document-Assistant
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows**

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your Groq API key:

```text
GROQ_API_KEY=your_api_key
```

Run the application:

```bash
uvicorn app.main:app --reload
```

---

## API Endpoints

### Upload PDF

**POST** `/upload-pdf`

Uploads a PDF document for processing.

### Ask Question

**POST** `/ask-question`

Returns answers based on the uploaded PDF.

---

## API Documentation

After running the project, open:

```
http://127.0.0.1:8000/docs
```

---

## Sample Questions

- Summarize this document.
- What are the key points?
- Explain the conclusion.
- What does the document say about a specific topic?

---

## Author

**Sushma C Sarganachari**
