from django.shortcuts import render
from django.views.generic import CreateView
from contact.forms import gform
from contact.models import feedback

# Create your views here.
class Contactus(CreateView):

    form_class=gform
    model=feedback
