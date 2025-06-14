from django import forms
from .models import NewData

class DataForm(forms.ModelForm):
    class Meta:
        model=NewData
        fields="__all__" #remeber this to use :)

from django.forms import ModelForm
from .models import valid
class validform(ModelForm):
    class Meta:
        model=valid

        fields="__all__"
    
    # this part is used for validation
    def clean(self):
        super(validform,self).clean()

        username=self.cleaned_data.get('username')
        text=self.cleaned_data.get('text')

        if len(username)<5:
            self._errors['username']=self.error_class(['Minimum 5 characters required'])
        
        if len(text)<10:
            self._errors['text']=self.error_class(['Post Should Contain a minimum of 10 characters'])

        return self.cleaned_data