from typing import Any
from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(Max_length=200)
    text=models.TextField(Max_length=Any)
    author=models.get_user_model_function=Any
    created_date=models.DateField
    published_date=models.DateTimeField
