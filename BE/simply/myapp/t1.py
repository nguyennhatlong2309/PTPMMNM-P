import time

start_time = time.time()
from langchain_huggingface import HuggingFaceEmbeddings
endt = time.time()
embeddings = HuggingFaceEmbeddings(model_name="./hf_models")

endt2 = time.time()

print(f'time 1: {endt - start_time:.2f}  /n time2: {endt2 - start_time:.2f}')