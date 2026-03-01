import re
class DocumentProcessor:
    def __init__(self, chunk_size: int = 200, overlap: int = 50):
        self.chunk_size = chunk_size
        self.overlap = overlap

class DocumentProcessor:
    def __init__(self):
        pass

    def split_text(self, text: str) -> list[str]:
        """
        Splits text by sentences, handling spaces and newlines.
        """
        sentences = re.split(r'(?<=[.!?])\s+', text.strip())
        return [s.strip() for s in sentences if s.strip()]