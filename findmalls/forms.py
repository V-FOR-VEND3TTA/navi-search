from django import forms 
from .models import Search


class SearchForm(forms.ModelForm):
    address = forms.CharField(label='', initial='Enter a name of a mall')

    class Meta:
        model = Search
        fields = ['address',]