from django.db import models
from dataclasses import dataclass


@dataclass
class BlogPost:
    title: str = 'Hello World'
    content: str = 'This is cool'


class Article(models.Model):
    title = models.TextField()
    content = models.TextField()
