from django.db import models

# Create your models here.

class User(models.Model):
    discord_id = models.BigIntegerField(unique=True)
    email = models.CharField(max_length=30, unique=True)
    user_tag = models.CharField(max_length=10, unique=True) 
    created_at = models.DateTimeField(auto_now_add=True)