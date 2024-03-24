from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from Club.models import Club
from Club.forms import ClubForm


# Create your views here.

def club_list(request):
    clubs = Club.objects.all()
    return render(request, 'Club/list.html', {'clubs': clubs})


def club_detail(request, id):
    clubs = Club.objects.filter(id=id).first()
    return render(request, 'Club/detail.html', {'clubs': clubs})


@login_required
def club_create(request):
    if request.method == 'POST':
        form = ClubForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('club-list')
    else:
        form = ClubForm()
    return render(request, 'Club/add.html', {'form': form})
