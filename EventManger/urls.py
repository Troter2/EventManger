"""
URL configuration for EventManger project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from EventManger.views import homepage
from Dj.views import dj_list, dj_detail, dj_create
from Club.views import club_detail, club_list, club_create
from Event.views import events

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', homepage, name='home'),
    path('eventos/', events, name='eventspage'),
    path('djs/', dj_list, name='dj-list'),
    path('dj/<int:id>/', dj_detail, name='dj-detail'),
    path('dj/create', dj_create, name='dj-create'),
    path('clubs/', club_list, name='club-list'),
    path('club/<int:id>', club_detail, name='club-detail'),
    path('club/create', club_create, name='club-create')

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #new

