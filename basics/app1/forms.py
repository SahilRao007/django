from django import forms
from .models import Data

class Dataform(forms.ModelForm):
    
    class Meta:
        model =Data
        fields = [
            'title',
            'content',
        ]

