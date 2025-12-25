from pathlib import Path
from typing import List

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap

    return chunks


if __name__ == "__main__":
    input_file = Path("../output/requirements_text.txt")
    text = input_file.read_text(encoding="utf-8")

    chunks = chunk_text(text)

    output_file = Path("../output/chunks.txt")
    output_file.write_text("\n\n---\n\n".join(chunks), encoding="utf-8")

    print(f"Created {len(chunks)} text chunks.")
