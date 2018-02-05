from django.contrib import admin
from . models import Question, Choice

# tell admin that Question objects have an admin interface
admin.site.register(Question)
admin.site.register(Choice)
