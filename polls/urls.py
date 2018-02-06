from django.urls import path
from . import views

#name of the app
app_name = 'polls'

urlpatterns = [
    path('', views.index, name = "index"),
    path('<int:question_id>/details/', views.details, name = "details"),
    path('<int:question_id>/vote/', views.vote, name = "vote"),
    path('<int:question_id>/results/', views.results, name = "results"),
]