from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from Club.models import Club


# Create your views here.

def club_list(request):
    clubs = Club.objects.all()
    return render(request, 'Club/list.html', {'clubs': clubs})


def club_detail(request, id):
    clubs = Club.objects.filter(id=id).first()
    return render(request, 'Club/detail.html', {'clubs': clubs})


@login_required
def club_create(request):
    return render(request, 'Club/add.html')
