from django.contrib.auth import logout
from django.shortcuts import render, redirect


def homepage(request):
    return render(request,'home.html')

def LogoutView(request):
    logout(request)
    return redirect('home')
    # Redirect to a success page.