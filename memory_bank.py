import os
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.schema import Document
from datetime import datetime

# ------------------------
# 1. Cấu hình
# ------------------------

CHROMA_DIR = "./chroma_db"  # Thư mục lưu trữ dữ liệu vector

# ------------------------
# 2. Khởi tạo Embedding
# ------------------------
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001", google_api_key=GEMINI_API_KEY
)

# ------------------------
# 3. Kết nối tới Chroma (tự động load lại dữ liệu nếu đã tồn tại)
# ------------------------
vector_store = Chroma(
    collection_name="memory_bank",
    persist_directory=CHROMA_DIR,
    embedding_function=embeddings
)

# ------------------------
# 4. Thêm dữ liệu vào Memory Bank
# ------------------------
def add_memory(content: str, metadata: dict = None):
    """
    Lưu một thông tin mới vào Memory Bank.
    metadata có thể chứa kiểu dữ liệu, ngày lưu, user_id,...
    """
    if metadata is None:
        metadata = {}
    metadata["timestamp"] = datetime.now().isoformat()

    doc = Document(page_content=content, metadata=metadata)
    vector_store.add_documents([doc])
    vector_store.persist()
    print(f"✅ Đã lưu vào Memory Bank: {content[:60]}...")

# ------------------------
# 5. Tìm kiếm trong Memory Bank
# ------------------------
def search_memory(query: str, k: int = 3):
    """
    Truy vấn thông tin từ Memory Bank dựa trên độ tương đồng ngữ nghĩa.
    """
    results = vector_store.similarity_search(query, k=k)
    return results

# ------------------------
# 6. Xóa dữ liệu
# ------------------------
def clear_memory():
    """
    Xóa toàn bộ dữ liệu trong Memory Bank.
    """
    vector_store.delete_collection()
    print("🗑 Memory Bank đã bị xóa sạch.")

