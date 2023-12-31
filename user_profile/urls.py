from django.urls import path
from user_profile.views import show_profile,get_planned_json, get_reading_json, get_completed_json, get_planned_json_flutter, get_reading_json_flutter, get_completed_json_flutter

app_name = 'profile'

urlpatterns = [
    path('<int:id>/', show_profile, name='show_profile'),
    path('get-planned/', get_planned_json, name='get_planned_json'),
    path('get-reading/', get_reading_json, name='get_reading_json'),
    path('get-completed/', get_completed_json, name='get_completed_json'),
    path('get-planned-flutter/', get_planned_json_flutter, name='get_planned_json_flutter'),
    path('get-reading-flutter/', get_reading_json_flutter, name='get_reading_json_flutter'),
    path('get-completed-flutter/', get_completed_json_flutter, name='get_completed_json_flutter'),
]