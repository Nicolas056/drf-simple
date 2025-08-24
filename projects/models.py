from django.db import models

# Create your models here.
# creando modelo de la base de datos


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.TextField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
