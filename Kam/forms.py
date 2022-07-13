import email
from django import forms

class Mera(forms.Form):
    F_name = forms.CharField(label = 'first-name', max_length = 15 )
    L_name = forms.CharField(label = 'Last-name' , max_length = 15 )
    Email = forms.EmailField(label = 'Email' , max_length = 30 )
    