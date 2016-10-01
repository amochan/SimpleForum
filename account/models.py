from datetime import date
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.signals import post_save


class UserProfile(models.Model):
  user = models.OneToOneField(User)
  created_date = models.DateField(default=date.today)
