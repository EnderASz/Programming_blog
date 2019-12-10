from django.shortcuts import render
from django.conf import settings

from apps.posts_manager.models import Post
from apps.tags_manager.models import Tag

from assets.python import std_template_loads


def start_page(request, page_number=0):
    print(page_number)
    max_posts_per_page = settings.POSTSLISTING['MAX_POSTS_PER_PAGE']
    page_number = request.POST.get('page_index', 0)
    first_index = page_number*max_posts_per_page
    last_index = first_index+max_posts_per_page

    all_posts = Post.objects.order_by('-date_add')
    posts_wrap = all_posts[first_index:last_index]

    return render(
        request,
        'standard_template.html',
            {
                'title': "Strona Startowa",
                'page_destination' : 'start-page',
                'avaible_tags' : std_template_loads.get_all_tags(),
                'recent_posts' : std_template_loads.get_recent_posts(all_posts),
                'display_content': ['post_wrapper'],
                'posts_wrap': posts_wrap,
            }
    )
