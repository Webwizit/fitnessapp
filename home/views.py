# pages/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

# Option A: Function-based
def index(request):
    return render(request, 'pages/index.html')

def payment(request):
    return render(request, 'pages/payment.html')


