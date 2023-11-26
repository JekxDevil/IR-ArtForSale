from django.db import models

class Document(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    url = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    tags = models.JSONField(default=list)
    price = models.CharField(max_length=20)

    def __str__(self):
        return self.title