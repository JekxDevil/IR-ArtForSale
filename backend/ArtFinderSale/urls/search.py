from django.urls import path
from ..views.searchs import get_documents

urlpatterns = [
    path("get-documents/<str:query>/", get_documents, name="get-documents"),
]
