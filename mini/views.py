from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import *
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse

class TurnausListView(ListView):
    model = Turnaus

class TurnausBaseView(LoginRequiredMixin, TemplateView):
    template_name = 'turnaus/base.html'
            
class TurnausCreateView(UserPassesTestMixin, CreateView):
    model = Turnaus
    fields = ['name']
    success_url = "/"

    def test_func(self):
        return self.request.user.is_superuser
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
        # User is authenticated but not a superuser
           messages.error(self.request, "Vain pääkäyttäjä voi lisätä turnauksia.")            
           return redirect('/')
        else:
        # User is not authenticated
           messages.error(self.request, "Kirjaudu sisään pääkäyttäjänä, että voit luoda turnauksen")
           return redirect('/')

class TurnausUpdateView(UserPassesTestMixin, UpdateView):
    model = Turnaus
    fields = ['name']
    success_url = "/"

    def test_func(self):
        return self.request.user.is_superuser
        
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
        # User is authenticated but not a superuser
            messages.error(self.request, "Vain pääkäyttäjä voi muokata turnauksia.")            
            return redirect('/')
        else:
        # User is not authenticated
             messages.error(self.request, "Kirjaudu sisään pääkäyttäjänä, että voit muokata turnausta")
             return redirect('/')


class TurnausDeleteView(UserPassesTestMixin, DeleteView):
    model = Turnaus
    success_url = "/"
    
    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
        # User is authenticated but not a superuser
            messages.error(self.request, "Et voi poistaa turnauksia.")            
            return redirect('/')
        else:
        # User is not authenticated
            messages.error(self.request, "Kirjaudu sisään pääkäyttäjänä jos haluat poistaa turnauksia.")
            return redirect('/')

    

