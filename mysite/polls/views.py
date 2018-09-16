from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
# to call the templates in our polls/templates/polls/index.html file w/o render shortcut

from .models import Question

def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  template = loader.get_template('polls/index.html')
  context = {
    'latest_question_list': latest_question_list
  }
  return render(request,'polls/index.html', context,)
# Create your views here.
def detail(request, question_id):
  try:
    question = Question.objects.get(pk=question_id)
  except Question.DoesNotExist:
    raise Http404("Question does not exist")
  return render(request, '/polls/detail.html', {'question': question})

def results(request, question_id):
  response = f" you're looking at the results from question {question_id}"
  return HttpResponse(response)

def vote(request, question_id): 
  response = f" You're voting on question {question_id}"
  return HttpResponse(response)