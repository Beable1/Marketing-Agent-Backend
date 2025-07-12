"""PDF → metin parçaları (≤1000 karakter)"""

from io import BytesIO
from pypdf import PdfReader

CHUNK_SIZE = 1000  # karakter

def extract_chunks(pdf_bytes: bytes) -> list[str]:
    reader = PdfReader(BytesIO(pdf_bytes))
    full_text = " ".join(page.extract_text() or "" for page in reader.pages)
    return [full_text[i : i + CHUNK_SIZE] for i in range(0, len(full_text), CHUNK_SIZE)]
