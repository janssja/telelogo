from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Gebruikersnaam"), blank=True, max_length=255)
    is_student = models.BooleanField(_("Patiënt"), default=False)
    is_teacher = models.BooleanField(_("Logopedist"), default=False)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username
