from django.views.generic import TemplateView

class Home(TemplateView):
    template_name= 'index.html'


class About(TemplateView):
    template_name= 'about.html'

class Impact(TemplateView):
    template_name= 'impact.html'


class Test(TemplateView):
    template_name='test.html';
