from django.shortcuts import render
from django.conf import settings

from apps.posts_manager.models import Post
from apps.tags_manager.models import Tag
from apps.authors_manager.models import Author

from assets.python import std_template_funcs as template_funcs

def tag_search(request, tag_slug, page_number=0):
    tag = Tag.objects.get(tag_slug=tag_slug)
    posts = Post.objects.filter(tags=tag).order_by('-date_add')
    return render(
        request,
        'standard_template.html',
            {
                'title': "#tag name#",
                'page_destination': 'search',
                'search_by': 'tag',
                'searching_object': "#tag name#",
                'sidebar': {
                    'avaible_tags' : template_funcs.get_tags_list(),
                    'recent_posts' : template_funcs.get_recent_posts(),
                },
                'display_elements': ['sidebar', 'post_wrapper', 'page_switcher'],
                'posts_wrap': posts,
                'page_info': {
                    'pages_amount': posts.count()//settings.POSTSLISTING['MAX_POSTS_PER_PAGE'],
                    'current_page': page_number,
                }
            }
    )

def author_search(request, author_slug, page_number=0):
    author = Author.objects.get(author_slug=author_slug)
    posts = Post.objects.filter(author=author).order_by('-date_add')
    return render(
        request,
        'standard_template.html',
            {
                'title': "#author name#",
                'page_destination': 'search',
                'search_by': 'author',
                'searching_object': "#author name#",
                'sidebar': {
                    'avaible_tags' : template_funcs.get_tags_list(),
                    'recent_posts' : template_funcs.get_recent_posts(),
                },
                'display_elements': ['sidebar', 'post_wrapper', 'page_switcher'],
                'posts_wrap': posts,
                'page_info': {
                    'pages_amount': posts.count()//settings.POSTSLISTING['MAX_POSTS_PER_PAGE'],
                    'current_page': page_number,
                }
            }
    )
