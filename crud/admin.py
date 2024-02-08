from django.contrib import admin
from .models import Score

# Register your models here.
class ScoreAdmin(admin.ModelAdmin):
    list_display=['name', 'score']

admin.site.register(Score, ScoreAdmin)
