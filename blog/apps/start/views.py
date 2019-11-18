from django.shortcuts import render
from django.conf import settings

# Create your views here.


def start_site(request):
    return render(request, 'start_site.html',
        {
            'title': "start",
            'develop_mode': settings.DEBUG,
        }
    )
