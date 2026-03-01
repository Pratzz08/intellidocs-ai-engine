class DocumentProcessor:
    def __init__(self, chunk_size: int = 200, overlap: int = 50):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def split_text(self, text: str) -> list[str]:
        """
        Splits text into overlapping chunks.
        """
        chunks = []
        start = 0
        text_length = len(text)

        while start < text_length:
            end = start + self.chunk_size
            chunk = text[start:end]
            chunks.append(chunk)
            start += self.chunk_size - self.overlap

        return chunks