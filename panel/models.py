from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from users.models import CustomUser

# Create your models here.  
class InterviewSlot(models.Model):
    slot = models.DateTimeField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return f'Date: {self.date}  Time: {self.time}'

class PanelDetail(models.Model):
    user = models.ManyToManyField(CustomUser, blank=True)
    
    email= models.CharField(max_length=25)
    phone = models.CharField(max_length=12)
    branch = models.CharField(max_length=12, null=True)
    interview_slot= models.ManyToManyField(InterviewSlot, blank=True)
    
    # Link this to Interview Detail model
    
    def __str__(self):
        return self.user
    
class PanelNumber(models.Model):
    name = models.CharField(max_length=12)
    
    members = models.ManyToManyField(PanelDetail, blank=True)

    def __str__(self):
        return self.name
    