from django.urls import path
from main.views import show_main

app_name = 'profile'

urlpatterns = [
    path('profile/', show_main, name='show_profile'),
]