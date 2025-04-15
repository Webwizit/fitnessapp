# pages/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # if using function‑based:
    path('', views.index, name='index'),
    path('paypal/payment/<int:video_id>/', views.paypal_payment, name='paypal_payment'),
    path('stripe/success/', views.stripe_success, name='stripe_success'),
    path('stripe/cancel/', views.stripe_cancel, name='stripe_cancel'),
    path('paypal/success/', views.paypal_success, name='paypal_success'),
    path('paypal/cancel/', views.paypal_cancel, name='paypal_cancel'),
]
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)