from django.urls import path
from authentication.views import register, login_user, logout_user, login_flutter, register_flutter, logout_flutter, show_json_by_id,\
    user_data



app_name = 'authentication'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('login_flutter/', login_flutter, name='login_flutter'),
    path('register_flutter/', register_flutter, name='register_flutter'),
    path('logout_flutter/', logout_flutter, name='logout_flutter'),
    path('json/', show_json_by_id, name='show_json_by_id'),
    path('user_data/', user_data, name='user_data'),

]