from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(State)
admin.site.register(Category)
admin.site.register(Job)
@admin.register(ApplyJob)
class ApplyJobAdmin(admin.ModelAdmin):
    list_display=['user','job']
