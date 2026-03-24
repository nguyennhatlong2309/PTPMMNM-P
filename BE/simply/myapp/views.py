from django.shortcuts import render

# Create your views here.

# myapp/views.py

from django.http import JsonResponse
# from .vector_store_manage import vectorStoreHandle
from .read_file import get_text 



# class service():
#     def __init__(self):
#         self.VStoreHanle = vectorStoreHandle()
#         self.VStoreHanle.loadVectorStore()

#     def saveStore(self):
#         self.VStoreHanle.saveVectorStore()

#     def addData(self,texts):
#         self.VStoreHanle.add_data(texts)

#     def answer(self,question):
#         return self.VStoreHanle.querry(question)



# service_instance  = service()
def embed_text(request):
    text = request.GET.get("text", "")
    
    # vector = service.answer(text)
    return JsonResponse({
        "content": text
    })


