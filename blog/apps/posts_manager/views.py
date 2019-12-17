from django.shortcuts import render
from .models import Post

def post_view(request, post_slug):
    post = Post.objects().get(post_slug=post_slug)
    return render(
        request,
        'standard_template.html',
        {
            'title': post.post_title,
            'page_destinations': ['post_view'],
            'display_elements': ['sidebar', 'post_viewer'],
            'sidebar': get_sidebar_values(),
            'post': post,
        }
    )
