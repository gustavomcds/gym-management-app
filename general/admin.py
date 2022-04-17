from django.contrib import admin
from .models import Coach, Athlete

# Register your models here.
@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'age')
    list_editable = ('first_name', 'last_name', 'age')

@admin.register(Athlete)
class AthleteAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'age')
    list_editable = ('first_name', 'last_name', 'age')