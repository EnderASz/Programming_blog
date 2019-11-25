from django.shortcuts import render
from django.conf import settings

# Create your views here.


def start_page(request):
    return render(
    request,
    'standard_template.html',
        {
            'title': "Strona Startowa",
            'avaible_tags' : [],
            'recent_posts' : [],
            'content': ['post_wrapper'],
            'posts_wrap': [
                {
                    'post_id': 2453,
                    'title': 'Java Text RPG #6 – Rest, Shop, The Final Battle and Game Ending',
                    'url': 'java-text-rpg-6-rest-shop-the-final-battle-and-game-ending',
                    'image': 'https://codestudent.net/wp-content/uploads/2019/10/alphabet-arts-and-crafts-blog-459688-768x512.jpg',
                    'meta': {
                        'add_date': '09-10-2019',
                        'author' : {'display_name': 'Aleksander Szymborski', 'url': 'aleksander-szymborski'},
                        'tags': [
                            {'display_name': 'Python', 'url': 'python'},
                            {'display_name': 'Web Development', 'url': 'web-dev'},
                        ]
                    }
                },
                {
                    'post_id': 2453,
                    'title': 'Java Text RPG #6 – Rest, Shop, The Final Battle and Game Ending',
                    'url': 'java-text-rpg-6-rest-shop-the-final-battle-and-game-ending',
                    'image': 'https://codestudent.net/wp-content/uploads/2019/10/alphabet-arts-and-crafts-blog-459688-768x512.jpg',
                    'meta': {
                        'add_date': '09-10-2019',
                        'author' : {'display_name': 'Aleksander Szymborski', 'url': 'aleksander-szymborski'},
                        'tags': [
                            {'display_name': 'Python', 'url': 'python'},
                            {'display_name': 'Web Development', 'url': 'web-dev'},
                        ]
                    }
                },
            ]
        }
    )
