from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from .models import *

#class JoukkueView(TemplateView):
#    template_name  = "joukkue/joukkue.html"

class JoukkueListView(ListView):
    model =  Joukkue

class JoukkueCreateView(CreateView):
    model = Joukkue
    fields = ["name"]
    success_url = "/"

class JoukkueDeleteView(DeleteView):
    model = Joukkue
    success_url = "/"

class JoukkueUpdateView(UpdateView):
    model = Joukkue
    fields = ['name']
    success_url = "/"
    
