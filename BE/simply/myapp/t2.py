from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os
file_path = r"C:\Users\Lenovo\ptpmmnm\demo\PTPMMNM-P\BE\simply\myapp\demo_index"
import time

start_time = time.time()

embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

end_time = time.time() 
print(f"Thời gian load vector store: {end_time - start_time:.2f} giây")

def loadVectorStore():
    import os
    path = os.path.join(os.path.dirname(file_path), "demo_index")
    print("Đang load vector store từ:", path)
    if os.path.exists(path):
        print("Folder tồn tại")
    else:
        print("Folder không tồn tại")
    try: 
        vector_store = FAISS.load_local(path, embeddings,allow_dangerous_deserialization=True)
    except Exception as e:
        print("Lỗi khi load:", e)
        vector_store = None
    
    return vector_store

start_time1 = time.time()

loadVectorStore()

end_time1 = time.time()
print(f"Thời gian load vector store: {end_time1 - start_time1:.2f} giây")
