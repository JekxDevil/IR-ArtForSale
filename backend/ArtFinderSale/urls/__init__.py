from django.urls import path, include

urlpatterns = [
    path("documents/", include(".search"))
]