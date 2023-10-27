from django.urls import path
from .views import show_xml

app_name = 'dataset'

urlpatterns = [
    path('xml/', show_xml, name='xml'),
]