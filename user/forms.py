from django import forms
from .models import *


class Diary(forms.ModelForm):

    class Meta:
        model = User
        fields = ['diary']
