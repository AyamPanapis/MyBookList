from django.shortcuts import render
from user_profile.models import UserProfile
from django.http import HttpResponseRedirect

def show_profile(request):
    name =UserProfile.objects.filter(user = request.user)
    context = {
        'username' : request.user.username
        }
    return render(request, 'profile.html', context)