import json
import os

from django.http import JsonResponse
from ..models import Document
import requests


def get_documents(request, query):
    IP = "http://localhost:8001"
    # query = request.GET.get('query', '')
    print(f"QUERY ----------------> {query}")
    url = f"{IP}/search?query={query} art"

    try:
        print(url)
        response = requests.get(url)
        response.raise_for_status()

        json_response = response.json()
        print(json_response)

        documents = []
        for docno in json_response.get("docno", []):
            try:
                current_doc = Document.objects.get(docno=docno)
                documents.append({
                    'docno': current_doc.docno,
                    'title': current_doc.title,
                    'description': current_doc.description,
                    'url': current_doc.url,
                    'image': current_doc.image,
                    'tags': current_doc.tags,
                    'price': current_doc.price,
                })
            except Document.DoesNotExist:
                pass

        return JsonResponse({"documents": documents})
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
