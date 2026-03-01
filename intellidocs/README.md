IntelliDocs – AI Knowledge Engine (Work in Progress)

Overview:
IntelliDocs is a production-style AI Knowledge Engine being built from first principles.

The goal of this project is to deeply understand how Retrieval-Augmented Generation (RAG) systems work, and deploy the final system on AWS with proper architecture and DevOps practices.

Instead of starting with high-level AI frameworks, this project begins with foundational concepts such as embeddings, cosine similarity, and semantic search.

Day 1 – Understanding Embeddings
What Was Implemented:
1. Generated text embeddings using OpenAI API
2. Implemented cosine similarity manually using NumPy
3. Compared semantic similarity between sentences
4. Observed how contextual meaning becomes measurable geometry

Key Learning:
1. Embeddings convert language into high-dimensional numerical vectors.
2. Cosine similarity measures the angular closeness between these vectors, allowing semantic comparison beyond keyword matching.

Example observation:
- "The cat sits on the mat"
- "A carpet lies under the sleeping feline"
These sentences show higher similarity than:
- "A dog is playing in the park"

This demonstrates that embeddings capture statistical usage patterns and contextual meaning, not just shared words.

Technical Stack (Current):
1. Python 3.11
2. OpenAI Embeddings API
3. NumPy (Cosine Similarity)
4. Git

Roadmap:
1. Document loading and chunking
2. FAISS vector storage
3. Full Retrieval-Augmented Generation pipeline
4. FastAPI backend
5. Dockerization
6. AWS deployment
7. CI/CD setup

Project Status:
Work in progress – actively building foundational components before integrating full RAG architecture.