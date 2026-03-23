# from django.test import TestCase

# GOOGLE_API_KEY = "AIzaSyBbpq1fP8Z0xliSJVar1MmPvokSQOOxrWw"


# from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
# from langchain_community.vectorstores import FAISS
# from langchain_core.prompts import PromptTemplate
# from langchain_community.document_loaders import PyPDFLoader


 
# video_id = "L7Jp38FvmnM"
# api = YouTubeTranscriptApi()
# try:
#   transcript_list = api.fetch(video_id, languages=['vi'])
#   transcript = " ".join(chunk.text for chunk in transcript_list)
# except TranscriptsDisabled:
#   print("No transcripts available for this video.") 



  
# #CHUYỂN THÀNH CÁC CHUNK
# splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
# chunks = splitter.create_documents([transcript])
# print("Số lượng chunks:", len(chunks)) 

# embeddings = GoogleGenerativeAIEmbeddings(
#     model="models/gemini-embedding-001" ,api_key=GOOGLE_API_KEY
# )

# # Tạo lại vector_store
# vector_store = FAISS.from_documents(chunks, embeddings)
# print("Vector store đã được tạo thành công!")

# #lẤY THIẾT LẬP SỐ LƯỢNG VECTOR SỬ DỤNG 
# retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})

# # CHỌN MODEL VÀ ĐỘ SÁNG TẠO
# llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2,api_key=GOOGLE_API_KEY)

# # THIẾT KẾ PROMPT
# prompt = PromptTemplate(
#     template="""
#       you are a helpful assitant.
#       Answer ONLY from the provided transcript context.
#       if the context is insufficient, just say you dont't know.

#       {context}
#       Question: {question}
#     """,
#     input_variables = ['context','question']
# )

# #TEST
# question = "nội dung của file nói về gì??"
# retrieved_docs = retriever.invoke(question)

# context = "\n\n".join([doc.page_content for doc in retrieved_docs])

# final_prompt = prompt.invoke({"context": context, "question": question})

# answer = llm.invoke(final_prompt)
# print(answer.content)
