from django.urls import path
from .views import show_xml, show_json

app_name = 'dataset'

urlpatterns = [
    path('xml/', show_xml, name='xml'),
    path('json/', show_json, name='json'),
]