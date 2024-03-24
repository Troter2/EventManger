from django import forms
from .models import Dj

class DjForm(forms.ModelForm):
    class Meta:
        model = Dj
        fields = ['name', 'nationality', 'style', 'best_known', 'description', 'photo']
