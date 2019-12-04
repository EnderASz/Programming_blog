from django.urls import path
from . import views

urlpatterns = [
    path('/tag/<slug:tag_slug>', views.tag_search, name="search-by-tag"),
    path('/author/<slug:author_slug>', views.author_search, name="search-by-author"),    
]
