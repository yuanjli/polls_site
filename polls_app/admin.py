# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.contrib import admin
# from .models import Choice, Question
from . import models

admin.AdminSite.site_header = 'My Awesome Polls Admin Panel!'

class ChoiceInline(admin.TabularInline):
    model = models.Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question Information', {'fields': ['question_text']}),
        ('Date and Time', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ['question_text', 'pub_date', 'was_published_recently']
    list_filter = ['pub_date']

# Register your models here.
admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.Choice)






