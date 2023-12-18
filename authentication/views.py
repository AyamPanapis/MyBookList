from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from .models import UserAuth
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required

# Create your views here.
@csrf_protect
def register(request):

    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return HttpResponseRedirect('/auth/login/')
        
    context = {'form':form}
    return render(request, 'register.html', context)

@csrf_protect
def login_user(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/') 
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')

    return render(request, 'login.html')

@csrf_protect
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

@csrf_exempt
def login_flutter(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Successful login status.
            return JsonResponse({
                "username": user.username,
                "status": True,
                "message": "Login successful!"
                # Add other data if you want to send data to Flutter.
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login failed, account disabled."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Login failed, check email or password again."
        }, status=401)

@csrf_exempt
def register_flutter(request):
    username = request.POST['username']
    password = request.POST['password']

    try:
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return JsonResponse({
            "username": user.username,
            "status": True,
            "message": "Register successful!"
        }, status=200)
    except:
        return JsonResponse({
            "status": False,
            "message": "Register failed, check email or password again."
        }, status=401)

    
@csrf_exempt
def logout_flutter(request):
    username = request.user.username

    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logged out successfully!"
        }, status=200)
    except:
        return JsonResponse({
        "status": False,
        "message": "Logout failed."
        }, status=401)
    
@csrf_exempt
def show_json_by_id(request):
    data = User.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required
@csrf_exempt
def user_data(request):
    username = request.user.username
    return JsonResponse({"username": username}, status=200)