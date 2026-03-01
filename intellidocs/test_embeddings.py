import numpy as np
from openai import OpenAI
import os
from dotenv import load_dotenv
from document_processor import DocumentProcessor

load_dotenv()
client = OpenAI()
processor = DocumentProcessor()

sample_text = """
The cat sits on the mat.
A dog is playing in the park.
A carpet lies under the sleeping feline.
"""

chunks = processor.split_text(sample_text)

embeddings = []

for chunk in chunks:
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=chunk
    )
    embeddings.append(response.data[0].embedding)

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

print("Similarity Matrix:\n")

for i in range(len(embeddings)):
    for j in range(len(embeddings)):
        sim = cosine_similarity(embeddings[i], embeddings[j])
        print(f"{sim:.4f}", end=" ")
    print()