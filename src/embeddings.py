from src.model import get_model
import faiss
import numpy as np

def create_vector_store(chunks):
    model = get_model()
    if not chunks:
        raise ValueError("No chunks received from chunker")

    embeddings = model.encode(chunks)
    if embeddings is None or len(embeddings) == 0:
        raise ValueError("Embeddings are empty")
    dim = embeddings.shape[1]

    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))

    print("Chunks:", len(chunks))
    print("Sample chunks:", chunks[:2])

    return index


