from django.db import models

from django.contrib.staticfiles.templatetags.staticfiles import static

from apps.authors_manager.models import Author
from apps.tags_manager.models import Tag


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=35)
    post_slug = models.SlugField(max_length=40)
    post_image = models.ImageField(
        upload_to=static('post_content\\images\\thumbnails\\')[1:],
        default=static('img\\bitmap\\no_image.png')[1:]
    )
    post_content = models.TextField()
    date_add = models.DateField(auto_now_add=True)
    authors = models.ManyToManyField(Author)
    tags = models.ManyToManyField(Tag)
