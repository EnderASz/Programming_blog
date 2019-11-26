from django.shortcuts import render
from django.conf import settings

from apps.posts_manager.models import Post


def start_page(request):
    max_posts_per_page = settings.POSTSLISTING['MAX_POSTS_PER_PAGE']
    max_recent_posts = settings.POSTSLISTING['MAX_RECENT_POSTS']

    current_page = request.POST.get('page_index', 0)
    first_index = current_page*max_posts_per_page
    last_index = first_index+max_posts_per_page

    all_posts = Post.objects.order_by('-date_add')

    posts_info = all_posts[first_index:last_index]
    recent_posts = all_posts[0:max_recent_posts]

    posts_wrap = []
    for post in posts_info:
        authors = []
        tags = []
        posts_wrap.append({
            'post_info': post,
            'meta': {
                'authors': authors,
                'tags': tags,
            }
        })

    return render(
    request,
    'standard_template.html',
        {
            'title': "Strona Startowa",
            'avaible_tags' : [],
            'recent_posts' : recent_posts,
            'display_content': ['post_wrapper'],
            'posts_wrap': posts_wrap,
        }
    )
