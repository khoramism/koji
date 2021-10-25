from django.contrib import admin
from django.db import models

# Register your models here.

from .models import Choice,Question, Vote


'''
class VoteInline(admin.TabularInline):
    model = Vote'''

class ChoiceAdmin(admin.ModelAdmin):
   # inlines = [VoteInline]
   list_display = ('question', 'choice_text')
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('q_creator','question_text', 'pub_date', 'was_published_recently')
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
        ('Question Creator ', {'fields': ['q_creator']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']
class VoteAdmin(admin.ModelAdmin):
    list_display = ('vote_date', 'voter')
    list_filter = ['choice']  
    search_fields = ['voter','choice']
    filter_horizontal = ('choice',)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Vote, VoteAdmin)