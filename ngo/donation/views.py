from django.shortcuts import render
from django.views.generic import CreateView
from donation.models import donateUs
from donation.forms import fform
# Create your views here.


class donation(CreateView):
    form_class=fform
    model=donateUs
