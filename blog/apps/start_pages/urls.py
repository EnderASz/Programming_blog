from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_page, name='start_page'),
    path('page/<int:page_number>', views.start_page, name='start_page_int')
]
