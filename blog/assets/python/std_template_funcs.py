from django.conf import settings

from apps.posts_manager.models import Post
from apps.tags_manager.models import Tag

def get_recent_posts(posts_list=None):
    if posts_list == None:
        return Post.objects.order_by('-date_add')[:settings.POSTSLISTING['MAX_RECENT_POSTS']]
    else:
        return posts_list[:settings.POSTSLISTING['MAX_RECENT_POSTS']]

def get_tags_list():
    return Tag.objects.order_by('tag_name')



def get_sidebar_values(posts_list=None):
    if not posts_list:
        posts_list = Post.objects.order_by('-date_add')
    return {
        'avaible_tags' : get_tags_list(),
        'recent_posts' : get_recent_posts(posts_list),
    },
