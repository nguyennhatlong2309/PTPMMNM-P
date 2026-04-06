from django.shortcuts import render
# Create your views here.

# myapp/views.py

from django.http import JsonResponse
from .read_file import get_text
from .vector_store import vectorStoreHandle as VTH

store = VTH()

def upload_file(request):
    if request.method == 'POST':
        file = request.get("file")

        if not file :
            return JsonResponse({"error" : "No file"}, status=400)
        
        data = get_text(file,"")
        store.add_data(data)



def ask(request):
    text = request.GET.get("text", "")
    
    return JsonResponse({
        "content": store.ask(text)
    })


