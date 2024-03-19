from django.shortcuts import render

# Create your views here.

def djpage(request):
    return render(request, 'dj.html')

