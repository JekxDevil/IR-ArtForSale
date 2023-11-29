from django.urls import path
from ..views.searchs import get_documents, get_recommended

urlpatterns = [
    path("get-documents/<str:query>/", get_documents, name="get-documents"),
    # path("get-recomended/<str_list:query>/", get_recommended, name="get-recommended"),
]
