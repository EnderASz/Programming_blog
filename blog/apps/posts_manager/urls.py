from django.urls import path
from . import views

urlpatterns = [
    path('/<slug:post_slug>', views.post_view, name='post_view'),
]
