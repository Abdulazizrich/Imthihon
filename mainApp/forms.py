from django import forms
from mainApp.models import *


class KitobForm(forms.ModelForm):
    class Meta:
        model=Kitob
        fields='__all__'