from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_page, name='start_page'),
    path('page/<int:page_number>', views.start_page, name='start_page_int'),
    path('about_me', views.about_me_page, name='about_me_page'),
    path('contact', views.contact_page, name='contact_page'),
]
