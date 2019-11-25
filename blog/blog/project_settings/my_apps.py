# My project apps list
include(
    'base.py',
)

INSTALLED_APPS += [
    'apps.tags_manager',
    'apps.authors_manager',
    'apps.posts_manager',
    'apps.start',
]


class PostsListingSettings:
    max_posts_per_page = 10
    max_recent_posts = 5
