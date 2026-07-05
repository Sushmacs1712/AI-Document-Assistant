import fitz

def extract_text_from_pdf(file_path):
    pdf = fitz.open(file_path)
    pages_text = []

    for page_num, page in enumerate(pdf, start=1):
        text = page.get_text()
        pages_text.append({
            "page": page_num,
            "text": text
        })

    pdf.close()
    return pages_text


def chunk_text(pages_text, chunk_size=500):
    chunks = []

    for page in pages_text:
        text = page["text"]
        page_number = page["page"]

        for i in range(0, len(text), chunk_size):
            chunk = text[i:i + chunk_size]

            if chunk.strip():
                chunks.append({
                    "page": page_number,
                    "content": chunk
                })

    return chunks