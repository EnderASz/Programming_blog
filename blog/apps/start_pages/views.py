from django.shortcuts import render
from django.conf import settings

from apps.posts_manager.models import Post, AuthorShip, TagShip
from apps.tags_manager.models import Tag
from apps.authors_manager.models import Author


def start_page(request):
    max_posts_per_page = settings.POSTSLISTING['MAX_POSTS_PER_PAGE']
    max_recent_posts = settings.POSTSLISTING['MAX_RECENT_POSTS']
    current_page = request.POST.get('page_index', 0)
    first_index = current_page*max_posts_per_page
    last_index = first_index+max_posts_per_page

    all_posts = Post.objects.order_by('-date_add')
    raw_posts = all_posts[first_index:last_index]
    recent_posts = all_posts[0:max_recent_posts]

    all_tags = Tag.objects.order_by('tag_name')

    posts_wrap = []
    for post_object in raw_posts:
        author_ships = AuthorShip.objects.select_related('author').filter(
            post=post_object
        )
        authors = [author for author in author_ships]

        tag_ships = TagShip.objects.select_related('tag').filter(
            post=post_object
        )
        tags = [tag for tag in tag_ships]

        posts_wrap.append(
            {
                'post_info': post_object,
                'meta': {
                    'authors': authors,
                    'tags': tags,
                }
            }
        )

    return render(
    request,
    'standard_template.html',
        {
            'title': "Strona Startowa",
            'page_destination' : 'start-page',
            'avaible_tags' : all_tags,
            'recent_posts' : recent_posts,
            'display_content': ['post_wrapper'],
            'posts_wrap': posts_wrap,
        }
    )
