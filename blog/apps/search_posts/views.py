from django.shortcuts import render

from apps.posts_manager.models import Post
from apps.tags_manager.models import Tag
from apps.authors_manager.models import Author

from assets.python import std_template_funcs as template_funcs

def tag_search(request, tag_slug):
    return render(
        request,
        'standard_template.html',
            {
                'title': "#tag name#",
                'page_destination': 'search',
                'search_by': 'tag',
                'searching_object': "#tag name#",
                'avaible_tags' : template_funcs.get_all_tags(),
                'recent_posts' : template_funcs.get_recent_posts(),
                'display_content': [],
            }
    )

def author_search(request, tag_slug):
    return render(
        request,
        'standard_template.html',
            {
                'title': "#author name#",
                'page_destination': 'search',
                'search_by': 'author',
                'searching_object': "#author name#",
                'avaible_tags' : template_funcs.get_all_tags(),
                'recent_posts' : template_funcs.get_recent_posts(),
                'display_content': [],
            }
    )
