from django.db import models

# Create your models here.


class File(models.Model):
    name = models.FileField(default='file')

