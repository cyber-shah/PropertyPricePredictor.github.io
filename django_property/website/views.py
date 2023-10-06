from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect


# Create your views here.
def home(request):
    # check to see if logging in 
    # so we see if this request method is a post?
    # if method is post, it means they are submitting the form
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # authenticate user
        user = authenticate(request, username=username, password=password)
        # if user is not none, then user is authenticated
        if user is not None:
            login(request, user)
            messages.success(request, ('You have been logged in!'))
            return redirect('home')
        else:
            messages.success(request, ('Error logging in - please try again...'))
            return redirect('home')
    
    # so if this function is not called via "POSTING" the form, then we just want to render the page
    # and assume that the user is not logged in
    else:
        return render(request, 'base.html', {})

# def login_user(request):
#     pass

# def logout_user(request):
#     pass

