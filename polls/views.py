from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import generic

from . models import Question, Choice

#display a message to the world
# def index(request):
#     latest_question_list = Question.objects.order_by('publication_date')[:5]
#     template = 'polls/index.html'
#     context = {
#         'latest_question_list':latest_question_list
#     }
#     return render(request, template, context)

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    #define an IndexView.Queryset to get the questions to publish
    def get_queryset(self):
        #return the last five questions published
        return Question.objects.filter(
            publication_date__lte = timezone.now()
        ).order_by('publication_date')

# def details(request, question_id):
#     question = get_object_or_404(Question, pk = question_id)
#     return render(request, 'polls/details.html', {'question':question})

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/details.html'

    def get_queryset(self):
        """
        :return:
        Excludes any questions that are not published yet.
        """
        return Question.objects.filter(publication_date__lte = timezone.now())

def vote(request, question_id):
    #get a question from Question model
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #Redisplay the question voting form.
        return render(request, 'polls/details.html', {'question':question,
                                                      'error_message': "The question doesn't have"
                                                                       " a choice(s)"})

    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args = (question.id,)))

# def results(request, question_id):
#     question = get_object_or_404(Question, pk = question_id)
#     return render(request, 'polls/results.html', {'question':question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    def get_queryset(self):
        """
        Excludes future questions that are not published yet.
        :return:
        """
        return Question.objects.filter(publication_date__lte = timezone.now())