from django.db import models

from django.contrib.staticfiles.templatetags.staticfiles import static

from apps.authors_manager.models import Author
from apps.tags_manager.models import Tag


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=35, unique=True)
    post_slug = models.SlugField(max_length=40, unique=True)
    post_image = models.ImageField(
        upload_to=static('posts_content/images/thumbnails/')[1:],
        default=static('img/bitmap/no_image.png')[1:]
    )
    post_content = models.TextField()
    date_add = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
