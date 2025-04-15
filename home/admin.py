from django.contrib import admin
from .models import Video, Payment

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title','Description', 'package', 'fixed_price')
    search_fields = ('title',)
    list_filter = ('package',)
    ordering = ('title',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('video', 'payment_method', 'amount', 'payment_date')
    search_fields = ('video__title', 'payment_method')
    list_filter = ('payment_method', 'payment_date')
    ordering = ('-payment_date',)
