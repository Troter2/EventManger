from django.shortcuts import render

from Dj.models import Dj


# Create your views here.

def dj_list(request):
    # rename the view function
    djs = Dj.objects.all()
    return render(request, 'dj/list.html', {'djs': djs})


def dj_detail(request, id):
    dj = Dj.objects.filter(id=id).first()
    return render(request, 'dj/detail.html', {'dj': dj})
