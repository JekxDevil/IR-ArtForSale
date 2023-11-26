from django.urls import path, include

urlpatters = [
    path("documents/", include("ArtFinderSale.urls.search"))
]