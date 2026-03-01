import numpy as np
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

sentences = [
    "Python is a programming language",
    "Java is a programming language",
    "Feline resting on carpet"
]

embeddings = []

for sentence in sentences:
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=sentence
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