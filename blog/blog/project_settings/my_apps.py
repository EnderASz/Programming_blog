# My project apps list
include(
    'base.py',
)

INSTALLED_APPS += [
    'apps.tags_manager',
    'apps.authors_manager',
    'apps.posts_manager',
    'apps.start_pages',
    'apps.search_posts',
]


POSTSLISTING = {
    'MAX_POSTS_PER_PAGE': 10,
    'MAX_RECENT_POSTS': 5
}
