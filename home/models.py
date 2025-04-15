from django.db import models
from django.utils import timezone
class Video(models.Model):
    # Package choices for video uploads
    PACKAGE_CHOICES = (
        ('standard', 'Standard'),
        ('premium', 'Premium'),
    )
    
    # Title of the video
    title = models.CharField(max_length=255)
    # File field to upload the video; adjust upload path as needed
    Description = models.TextField(max_length=1000,null=True)
    video_file = models.FileField(upload_to='videos/')
    # Fixed price for the video (decimal type ensures currency formatting)
    fixed_price = models.DecimalField(max_digits=10, decimal_places=2)
    # Package selection, providing a choice between 'standard' and 'premium'
    package = models.CharField(max_length=10, choices=PACKAGE_CHOICES, default='standard')

    def __str__(self):
        return self.title

class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = (
        ('paypal', 'PayPal'),
        ('stripe','Stripe'),
        ('card', 'Card'),
        ('apple_pay', 'Apple Pay'),
        ('other', 'Other'),
    )

    video = models.ForeignKey(Video, related_name='payments', on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    # amount is non-editable, and its value will be auto-populated from the video's fixed_price
    amount = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    payment_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Set the payment amount based on the video's fixed price before saving.
        if self.video:
            self.amount = self.video.fixed_price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.video.title} - {self.get_payment_method_display()}"

from django.conf import settings
from django.db import models

from django.db import models


class Review(models.Model):
    """
    Generic customer review model for collecting user remarks and ratings.
    """
    name = models.CharField(
        max_length=255,
        help_text="Name of the reviewer."
    )
    remarks = models.TextField(
        help_text="Reviewer's remarks."
    )
    rating = models.PositiveSmallIntegerField(
        choices=[
            (1, '1 - Very Poor'),
            (2, '2 - Poor'),
            (3, '3 - Average'),
            (4, '4 - Good'),
            (5, '5 - Excellent'),
        ],
        help_text="Rating from 1 to 5."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when the review was created."
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Timestamp when the review was last updated."
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f"{self.name} ({self.rating}/5)"
