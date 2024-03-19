from django.shortcuts import render


# Create your views here.

def clubpage(request):
    return render(request, 'local.html')
