from django.urls import path
from . import views

#name of the app
app_name = 'polls'

urlpatterns = [
    # path('', views.index, name = "index"),
    path('', views.IndexView.as_view(), name = "index"),
    # path('<int:question_id>/details/', views.details, name = "details"),
    path('<int:pk>/', views.DetailView.as_view(), name = "details"),
    path('<int:question_id>/vote/', views.vote, name = "vote"),
    # path('<int:question_id>/results/', views.results, name = "results"),
    path('<int:pk>/results/', views.ResultsView.as_view(), name = "results"),
]