from django.urls import path, include

urlpatterns = [
    path("documents/", include("ArtFinderSale.urls.search"), name="get-documents"),
    # path("recomandation/", include("ArtFinderSale.urls.search"), name="get-recommended")
]