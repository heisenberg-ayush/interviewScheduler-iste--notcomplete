from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from users.models import CustomUser

# Create your models here.
class Scheduled(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    email= models.CharField(max_length=25)
    phone = models.CharField(max_length=12)
    your_branch = models.CharField(max_length=12, null=True)
    scheduled_date = models.CharField(max_length=25)
    scheduled_time = models.CharField(max_length=25)
    date = models.DateField(auto_now_add= True)
    

    def __str__(self):
        return f'{self.user} scheduled on {self.scheduled_date} at {self.scheduled_time}'

    class Meta:
        ordering = ["-date"]

