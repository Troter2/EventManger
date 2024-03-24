from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from Club.models import Club


# Create your views here.

def club_list(request):
    club = Club.objects.all()
    return render(request, 'club/list.html', {'club': club})


def club_detail(request):
    clubs = Club.objects.filter(id=id).first()
    return render(request, 'local.html', {'clubs': clubs})


@login_required
def club_create(request):
    return render(request, 'club/add.html')
