from django import forms
from .models import Data2

class data2form(forms.ModelForm):
    class meta:
        model=Data2
        fields=[
            'title',
            'content',
        ]
    