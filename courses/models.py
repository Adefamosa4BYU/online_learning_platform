from django.db import models
from django_mongodb_backend.fields import ObjectIdAutoField


class Course(models.Model):
    id = ObjectIdAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    level = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)

    def __str__(self):
        return self.title