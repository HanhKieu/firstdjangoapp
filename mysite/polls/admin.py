from django.contrib import admin
from polls.models import Question, Choice
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]


admin.site.register(Question, QuestionAdmin)
# Register your models here.
admin.site.register(Choice)