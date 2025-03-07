from django.db import models

dependencies = [

]
class Profiles(models.Model):
    name = models.CharField(max_length = 16)
    password = models.CharField(max_length = 16)
    time_registration = models.DateTimeField(auto_now_add=True)
