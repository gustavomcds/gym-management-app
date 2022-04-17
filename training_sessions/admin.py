from django.contrib import admin
from .models import TrainingSession

@admin.register(TrainingSession)
class TrainingSessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'hour', 'capacity')
    list_editable = ('date', 'hour', 'capacity')
    list_filter = ('date', 'hour')