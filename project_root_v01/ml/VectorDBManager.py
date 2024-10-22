import chromadb

class VectorDBManager:
    def __init__(self):
        self.client = chromadb.Client()

    def add_vectors(self, vectors, metadata):
        # 벡터와 메타데이터를 ChromaDB에 저장
        self.client.add(vectors=vectors, metadata=metadata)

    def search_similar(self, query_vector, top_k=5):
        # 쿼리 벡터와 유사한 데이터 검색
        return self.client.search(query=query_vector, top_k=top_k)
