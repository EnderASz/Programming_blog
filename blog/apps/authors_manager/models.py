from django.db import models

from django.contrib.auth.models import User

class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    author_name = models.CharField(max_length=40)
    author_slug = models.SlugField(max_length=20)


class AuthorUserShip(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
