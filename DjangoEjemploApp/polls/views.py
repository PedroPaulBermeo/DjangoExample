from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Question, Choice
'''
def index(req):
    latest_question_list = Question.objects.all()
    return render(req, "polls/index.html", {
        "latest_question_list":latest_question_list
    })
    #return HttpResponse("Estas en la pagina principal de Premios Platzi App")


def detail(req, question_id):
    question = get_object_or_404(Question, pk = question_id)
    #question = Question.objects.get(pk = question_id)
    return render(req, "polls/detail.html",{
        "question": question
    })
    #return HttpResponse(f"Estas viendo la pregunta # {question_id}")


def results(req, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(req, "polls/results.html",{
        "question":question
    })
    #return HttpResponse(f"Estas viendo los resultados de la pregunta # {question_id}")
'''

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        #Return the last five published question
        #-pub_date "-" al inicio quiere decir que ordenare desde
        # las mas recientes a las mas antiguas, si no pongo me trae
        # ordenado de las mas viejas a las mas nuevas
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(req, question_id):
    #question = Question.objects.get(pk=1)
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_chocie = question.choice_set.get(pk = req.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(req, "polls/detail.html", {
            "question": question,
            "error_message": "No elegiste una respuesta"
        })
    else:
        selected_chocie.votes += 1
        selected_chocie.save()
        return(HttpResponseRedirect(reverse("polls:results", args=(question.id,))))




    #return HttpResponse(f"Estas votando a la pregunta # {question_id}")

