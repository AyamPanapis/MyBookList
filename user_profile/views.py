from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from categories.models import Book

@login_required
def show_profile(request):
    user = request.user
    date_joined_wib = user.date_joined.astimezone(timezone.get_current_timezone())
    context = {
        'username': user.username,
        'date_joined': date_joined_wib,
    }
    return render(request, 'profile.html', context)
