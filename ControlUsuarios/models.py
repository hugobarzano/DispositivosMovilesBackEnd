from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User,primary_key=True)

    # The additional attributes we wish to include.
    dni = models.CharField(max_length=150,blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.dni

    def __dni__(self):
        return self.dni
