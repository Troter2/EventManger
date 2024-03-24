from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from Event.forms import EventForm
from Event.models import Event


# Create your views here.
def event_list(request):
    # rename the view function
    djs = Event.objects.all()
    return render(request, 'event/list.html', {'djs': djs})


def event_detail(request, id):
    dj = Event.objects.filter(id=id).first()
    return render(request, 'event/detail.html', {'dj': dj})


@login_required
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('dj-list')
    else:
        form = EventForm()
    return render(request, 'event/add.html', {'form': form})

