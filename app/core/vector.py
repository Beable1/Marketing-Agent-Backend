from typing import Iterable

class DummyVectorDB:
    """Bellek‑içi basit vektör saklama – Pinecone yerine yer tutucu"""

    def __init__(self):
        self.store: dict[str, list[tuple[str, list[float]]]] = {}

    def upsert(self, namespace: str, items: Iterable[tuple[str, list[float]]]):
        self.store.setdefault(namespace, []).extend(items)
        print(f"[VectorDB] Upserted {len(list(items))} embeddings into {namespace}")

vector_db = DummyVectorDB()