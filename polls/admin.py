from django.contrib import admin
from . models import Question, Choice

#create the ability to add a bunch of Choices
#with every Question added.

#Choice objects are edited in the Question admin page.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# create a model admin class, and pass it as the second argument
#to admin.site.register(Question) each time you need to change
#the admin options for a model

class QuestionAdminClass(admin.ModelAdmin):
    #splitting the fields in fieldsets
    fieldsets = [
        ('Question to publish', {'fields':['question_text']}),
        ('Date information', {'fields':['publication_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]

    #we can display individual fields using list_display as a tuple of columns
    #to display on the change list page.
    list_display = ('question_text','publication_date','was_published_recently')

    #filters using the list_filter
    #adds a FILTER sidebar that lets people filter by publication_date
    list_filter = ['publication_date']

    #let us add some search capability
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdminClass)
