from django.shortcuts import render
from .models import Post

from assets.python import std_template_funcs as template_funcs

def post_view(request, post_slug):
    post = Post.objects.get(post_slug=post_slug)
    return render(
        request,
        'standard_template.html',
        {
            'title': post.post_title,
            'page_destinations': ['post_view'],
            'display_elements': ['sidebar', 'post_viewer'],
            'sidebar': {
                'avaible_tags' : template_funcs.get_tags_list(),
                'recent_posts' : template_funcs.get_recent_posts(),
            },
            'post': post,
        }
    )
