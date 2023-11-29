from django.db import models


class Document(models.Model):
    docno = models.CharField(max_length=50, unique=True, primary_key=True)
    title = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=500)
    author = models.CharField(max_length=250, null=True)
    url = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    tags = models.JSONField(default=list, null=True)
    price = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.title
