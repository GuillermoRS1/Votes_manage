from django.contrib import admin
from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


# We create the class to store the data of the question created by the administrator
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        # To rename or create the text of a question
        (None, {'fields': ['question_text']}),
        # To put the date and the time in which the question was created
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    # To create the different answer options of a question
    inlines = [ChoiceInline]
    # To see when the question was created, go to the page where all the questions are created
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # To create a filter according to the date on which each question has been created
    list_filter = ['pub_date']
    # To search for a specific question with the question text
    search_fields = ['question_text']


# To tell the admin that Question objects have an admin interface
admin.site.register(Question, QuestionAdmin)
