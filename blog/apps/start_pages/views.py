from django.shortcuts import render
from django.conf import settings

from apps.posts_manager.models import Post
from apps.tags_manager.models import Tag

from assets.python import std_template_funcs as template_funcs

def start_page(request, page_number=0):
    max_posts_per_page = settings.POSTSLISTING['MAX_POSTS_PER_PAGE']
    first_index = page_number*max_posts_per_page
    last_index = first_index+max_posts_per_page

    all_posts = Post.objects.order_by('-date_add')
    posts_wrap = all_posts[first_index:last_index]

    return render(
        request,
        'standard_template.html',
            {
                'title': "Strona Startowa",
                'page_destinations' : ['start-page', 'posts_list'],
                'avaible_tags' : template_funcs.get_all_tags(),
                'recent_posts' : template_funcs.get_recent_posts(all_posts),
                'display_content': ['post_wrapper', 'page_switcher'],
                'posts_wrap': posts_wrap,
                'page_info': {
                    'pages_amount': all_posts.count()//max_posts_per_page,
                    'current_page': page_number,
                }
            }
    )
