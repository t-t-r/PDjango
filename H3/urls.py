from django.urls import path
from .views import *

urlpatterns = [
    path('', JoukkueListView.as_view()),
    path('joukkue/new', JoukkueCreateView.as_view()),
    path('joukkue/<int:pk>/delete', JoukkueDeleteView.as_view()),
    path('joukkue/<int:pk>', JoukkueUpdateView.as_view()),
]
