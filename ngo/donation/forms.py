from donation.models import donateUs
from django import forms

class fform(forms.ModelForm):

    class Meta():
        model=donateUs
        fields=('name','email','money','phone')
