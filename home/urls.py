# pages/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # if using function‑based:
    path('', views.index, name='index'),
    path('payment/', views.payment, name='payment'),

  
]
