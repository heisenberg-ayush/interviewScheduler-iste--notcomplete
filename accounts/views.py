from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from calendar import HTMLCalendar
from datetime import datetime
from .models import Scheduled
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You can now Login')
            return redirect("account-login")
    else :
        form = UserRegisterForm()
    
    return render(request, 'accounts/register.html', {"form": form})

@login_required
def scheduler(request):
    if request.method == "POST":
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_branch = request.POST['your-branch']
        your_email = request.POST['your-email']
        your_schedule_time = request.POST['your-schedule-time']
        your_schedule_date = request.POST['your-schedule-date']

        # cal = HTMLCalendar().formatmonth(year, month)

        messages.success(request, f'Your interview has been successfully scheduled!')
        messages.success(request, f'Check Your Email to see the details!')

        # send an email
        # send_mail(
        #     'ISTE Interview Scheduled', #subject
        #     'You have scheduled your interview on ' + your_schedule_date + ' at ' + your_schedule_time, #message
        #     settings.EMAIL_HOST_USER, #from email
        #     [your_email], #to email
        # )

        # Scheduled Details
        scheduled = Scheduled.objects.create(
            user= your_name,
            phone= your_phone,
            your_branch= your_branch,
            email= your_email,
            scheduled_time= your_schedule_time,
            scheduled_date= your_schedule_date,
        )
        scheduled.save()

        return render(request, 'accounts/interviewConfirmed.html', {
            'your_name': your_name,
            'your_phone': your_phone,
            'your_branch': your_branch,
            'your_email': your_email,
            'your_schedule_time': your_schedule_time,
            'your_schedule_date': your_schedule_date,
        })

    else:
        return render(request, 'accounts/interviewScheduler.html')
