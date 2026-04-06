from langchain_community.vectorstores import FAISS
from .read_file import get_text
from langchain_community.llms import Ollama
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain.prompts import PromptTemplate

import time


class vectorStoreHandle():
    def __init__(self):
        from langchain_huggingface import HuggingFaceEmbeddings

        self.embeddings = HuggingFaceEmbeddings(model_name=r"/home/nhatlong/demo/PTPMMNM-P/BE/simply/myapp/hf_models")

        try:
            self.vector_store = FAISS.load_local(
                r"./demo_index",
                self.embeddings,
                allow_dangerous_deserialization=True
            )
        except:
            self.vector_store = None

        self.retriever = None
        if self.vector_store:
            self.retriever = self.vector_store.as_retriever(search_kwargs={"k":2})

        self.llm = Ollama(model="llama3:8b")

        self.prompt = PromptTemplate(
            input_variables=["context", "question"],
            template="""
                Bạn là trợ lý AI.

                BẮT BUỘC: Luôn trả lời bằng TIẾNG VIỆT, không được dùng tiếng Anh
                Chỉ được trả lời dựa trên tài liệu dưới đây.
                Nếu không có thông tin, hãy nói: "Tôi không biết".
                
                Tài liệu:
                {context}

                Câu hỏi:
                {question}

                Trả lời:
"""
        )

        if self.retriever:
            self.qa_chain = RetrievalQA.from_chain_type(
                llm=self.llm,
                retriever=self.retriever,
                chain_type="stuff",
                chain_type_kwargs={"prompt": self.prompt}
            )

    def ask(self, question):
        if not self.vector_store:
            return "Chưa có dữ liệu"

        docs = self.retriever.get_relevant_documents(question)

        context = "\n".join([doc.page_content for doc in docs])

        prompt = self.prompt.format(
            context=context,
            question=question
        )

        answer = self.llm.invoke(prompt)
        return answer

    def create_store(self, texts):
        chunks = self.spliter_chunks(texts)
        
        # tạo vector store
        self.vector_store = FAISS.from_documents(chunks, self.embeddings)
        self.retriever = self.vector_store.as_retriever(search_kwargs={"k": 2})

        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            retriever=self.retriever,
            chain_type="stuff",
            chain_type_kwargs={"prompt": self.prompt}
        )
        self.saveVectorStore()

    def spliter_chunks(self, texts):
        from langchain_text_splitters import RecursiveCharacterTextSplitter

        if isinstance(texts, str):
            texts = [texts]

        return RecursiveCharacterTextSplitter(
            chunk_size=300,
            chunk_overlap=50
        ).create_documents(texts)

    def saveVectorStore(self):
        self.vector_store.save_local("./demo_index")
        print("da luu vector store")

    def add_data(self, texts):
        chunks = self.spliter_chunks(texts)

        if self.vector_store is None:
            self.vector_store = FAISS.from_documents(chunks, self.embeddings)
        else:
            self.vector_store.add_documents(chunks)

        self.retriever = self.vector_store.as_retriever(search_kwargs={"k": 2})

        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            retriever=self.retriever,
            chain_type="stuff"
        )
        self.saveVectorStore()




start = time.time()
VTH = vectorStoreHandle()

# with open("./RRTO.pdf","rb")as f:
#     fileB = f.read()

# texts = get_text(fileB,".pdf")
# print(texts)


# e = time.time()
# print(f"thoi gian khoi tao {e-start:.2f}")
# VTH.create_store(texts) 

# ee = time.time()
# print(f"thoi gian load text {e-start:.2f}\nthoi gian tao store {ee-e}")

# texts = get_text(fileB,".pdf")
# print(texts)
# VTH.add_data(texts)


e1= time.time()
a1 = VTH.ask("nội dung của câu truyện rắc rối tình ơi là gì?")
e2=time.time()
print(a1)
print(f"thoi gian truy van la {e2-e1:.2f}")
# a2 =  VTH.ask("nội dung nói về nhân vật nào nhiều nhất?")
# e3=time.time()
# print(a2)
# a3=VTH.ask("truyện có bao nhiêu nhân vật?")
# e4=time.time()
# print(a3)
# print(f"thoi gian khoi tao {e-start:.2f}\nthoi gian khoi tao {e1-start:.2f} \nthoi gian tra loi lan 1 la {e2-e1:.2f}" )
# print("thoi gian tra loi cau hoi thu 2 la: {e3-e2:.2f}\nthoi gian tra loi cau hoi thu 3 la: {e4-e3:.2f}")