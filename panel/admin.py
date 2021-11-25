from django.contrib import admin
from .models import PanelNumber
from .models import PanelDetail
from .models import InterviewSlot

# Register your models here.
admin.site.register(PanelNumber)
admin.site.register(PanelDetail)
admin.site.register(InterviewSlot)