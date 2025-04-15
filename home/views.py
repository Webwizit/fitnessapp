# views.py
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Video, Payment
import stripe



def index(request):
    videos = Video.objects.all()
    return render(request, 'templates/index.html', {'videos': videos})


def stripe_success(request):
    session_id = request.GET.get('session_id')
    context = {'session_id': session_id}
    return render(request, 'templates/stripe_success.html', context)


def stripe_cancel(request):
    return render(request, 'templates/stripe_cancel.html')

def paypal_payment(request, video_id):
    
    video = get_object_or_404(Video, pk=video_id)
    # You could optionally create a Payment record here,
    # but typically you may want to create it after a successful payment.
    return render(request, 'templates/paypal_payment.html', {
        'video': video,
        'paypal_client_id': settings.PAYPAL_CLIENT_ID
    })

def paypal_success(request):
    # Here you could confirm the payment by retrieving payment details
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')
    # In production, retrieve the payment and execute it.
    # For example:
    # payment = paypalrestsdk.Payment.find(payment_id)
    # if payment.execute({"payer_id": payer_id}):
    #    print("Payment executed successfully.")
    return render(request, 'templates/paypal_success.html', {"payment_id": payment_id, "payer_id": payer_id})


def paypal_cancel(request):
    return render(request, 'templates/paypal_cancel.html')
