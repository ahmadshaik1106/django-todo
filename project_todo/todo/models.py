from django.db import models
from django.contrib.auth.models import User

# class Usr(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

class Task(models.Model):
    user        = models.ForeignKey(User,on_delete=models.CASCADE) 
    name        = models.CharField(max_length=200)
    time_added  = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.name
