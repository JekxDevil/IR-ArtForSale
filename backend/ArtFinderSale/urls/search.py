from django.urls import path
from ..views.search import get_documents

urlpatterns = [
    path("get-documents/", get_documents, name="get-documents")
]