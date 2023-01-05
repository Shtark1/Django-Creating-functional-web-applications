from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


from measurement.models import Sensor


@admin.register(Sensor)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['name']


# @admin.register(Tag)
# class TagAdmin(admin.ModelAdmin):
#     list_display = ['name']