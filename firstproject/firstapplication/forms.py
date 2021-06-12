from django import forms

from .models import firstmodel

class firstform(forms.ModelForm):
    class Meta:
        model = firstmodel
        fields = [
            'first_name',
            'last_name',
            'ids',
            'contact',
        ]

