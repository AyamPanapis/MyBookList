from django.shortcuts import render

def show_main(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = "Not logged in"
    
    context = {
        'username': username
    }
    return render(request, 'main.html', context)
