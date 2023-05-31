#from django.urls import path, include
#from django.contrib.auth.views import LoginView, LogoutView
#from .views import *

#app_name = 'turnaus'

#urlpatterns = [
#    path('', TurnausListView.as_view()),
#    path('turnaus/uusi', TurnausCreateView.as_view()),
#    path('turnaus/<int:pk>', TurnausUpdateView.as_view()),
#    path('turnaus/<int:pk>/poista', TurnausDeleteView.as_view()),

#    path('accounts/login/', LoginView.as_view()),
#    path('logout/', LogoutView.as_view(next_page="/")),
#    
#]
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

app_name = 'turnaus'

urlpatterns = [
    path('', TurnausListView.as_view(), name='frontpage'),
    path('turnaus/uusi', TurnausCreateView.as_view(), name='turnaus-create'),
    path('turnaus/<int:pk>', TurnausUpdateView.as_view(), name='turnaus-update'),
    path('turnaus/<int:pk>/poista', TurnausDeleteView.as_view(), name='turnaus-delete'),

    path('logout/', LogoutView.as_view(next_page="/"), name='logout'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/profile/', LoginView.as_view(), name='profile'),
]
