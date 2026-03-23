from django.urls import path
from .views import embed_text

urlpatterns = [
    path('embed/', embed_text),
]