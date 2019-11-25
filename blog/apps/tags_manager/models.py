from django.db import models


class Tag(models.Model):
    tag = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=30)
    tag_slug = models.SlugField(max_length=20)
