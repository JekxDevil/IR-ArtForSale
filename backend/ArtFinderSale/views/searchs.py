import json
import os
import pandas as pd
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
        # with open('ArtFinderSale/views/final_result.json', 'r') as json_file:
        #     data = json.load(json_file)
        #
        # # Assuming the JSON structure is a list of dictionaries
        # for row in data:
        #
        #     new_document = Document(
        #         image=row['img'],
        #         author=row['author'],
        #         title=row['title'],
        #         description=row['description'],
        #         price=row['price'],
        #         tags=row['tags'],
        #         url=row['url'],
        #         docno = row['docno']
        #     )
        #     new_document.save()

        json_response = response.json()


        documents = []
        for docno in json_response["docno"].values():
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
        print(documents)
        return JsonResponse({"documents": documents})
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
