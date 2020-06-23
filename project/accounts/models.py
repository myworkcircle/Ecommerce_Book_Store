from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255,default="meraghar")
    phonenum = PhoneNumberField()

# class admin(Abstractuser):
#     pass
# class Donor(models.Model):
#     user = models.ForeignKey('User',on_delete=models.CASCADE)
#     book_type = models.CharField(max_length=255)
#     book_quantity = models.IntegerField()
#     date = models.DateField()

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)
