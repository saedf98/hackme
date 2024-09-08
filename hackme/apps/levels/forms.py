from django import forms
from .models import Level


class LevelForm(forms.ModelForm):

    class Meta:
        model = Level
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Beginner'
            })
        }
