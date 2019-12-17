from django.urls import path
from . import views

urlpatterns = [
    path('<int:post_slug>', views.post_view, name='post_view'),
]
