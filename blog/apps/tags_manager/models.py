from django.db import models


class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=30, unique=True)
    tag_slug = models.SlugField(max_length=20, unique=True)
