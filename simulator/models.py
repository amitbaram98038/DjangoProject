from django.db import models

from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class profile(models.Model):

    ROLE_PASSANGER = 'Passenger'
    ROLE_STAFF = 'Staff'
    ROLE_CHOICES = [
        (ROLE_PASSANGER, 'Passenger'),
        (ROLE_STAFF, 'Airport Staff'),

    ]

user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
on_delete=models.CASCADE
related_name='profile'

role=models.CharField(max_length=20, choices="ROLE_CHOICES", default="ROLE_PASSANGER")

def __str__(self):
    return f"{self.user.username}"
@property
def is_staff_role(self):
    return self.role == self.ROLE_STAFF

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)
    else:
        profile.objects.get_or_create(user=instance) 