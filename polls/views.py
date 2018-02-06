from django.shortcuts import render, get_object_or_404
from . models import Question

#display a message to the world
def index(request):
    latest_question_list = Question.objects.order_by('publication_date')[:5]
    template = 'polls/index.html'
    context = {
        'latest_question_list':latest_question_list
    }
    return render(request, template, context)

def details(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/details.html', {'question':question})