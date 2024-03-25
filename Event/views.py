from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from Club.models import Club
from Event.forms import EventForm
from Event.models import Event


# Create your views here.
def event_list(request):
    # rename the view function
    events = Event.objects.all()
    return render(request, 'event/list.html', {'events': events})


def event_detail(request, id):
    event = Event.objects.filter(id=id).first()
    return render(request, 'event/detail.html', {'event': event})


@login_required
def event_create(request):

    clubs = Club.objects.all().order_by('name')
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('event-list')
    else:
        form = EventForm()
    return render(request, 'event/add.html', {'form': form, 'clubs': clubs})

