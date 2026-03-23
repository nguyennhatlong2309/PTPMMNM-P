



from langchain_community.vectorstores import FAISS

class vectorStoreHandle():
    def __init__(self):
        from langchain_huggingface import HuggingFaceEmbeddings
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        self.vector_store = None


    def create_store(self,texts):
        chunks = self.spliter_chunks(texts)
        self.vector_store = FAISS.from_texts(chunks,self.embeddings)
    
    def spliter_chunks(self,text):
        from langchain_text_splitters import RecursiveCharacterTextSplitter
        chunks = RecursiveCharacterTextSplitter(chunk_size=4000, chunk_overlap=300).create_documents(text)
        return chunks

    def saveVectorStore(self):
        self.vector_store.save_local("demo_index")

    def loadVectorStore(self):
        try: 
            self.vector_store = FAISS.load_local("demo_index",self.embeddings)
        except:
            self.vector_store = None

    def add_data(self,texts):
        if self.vector_store is None:
            self.create_store(texts)
        else :
            chunks = self.spliter_chunks(texts)
            self.vector_store.add_data(chunks)

    def querry(self,quesstion):
        if self.vector_store is not None:
            return self.vector_store.similarity_search(quesstion,k=3)
        else :
            return "Vector Store không có dữ liệu."
        
        



    





    
    

