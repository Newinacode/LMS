from django.db import models
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    membership_date = models.DateField(auto_now_add=True)
