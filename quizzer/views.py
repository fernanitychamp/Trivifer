from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Quiz


def index(request):
    latest_quizes_list = Quiz.objects.order_by('-pub_date')[:3]
    template = loader.get_template('quizzer/index.html')
    return HttpResponse(template.render(
        {'latest_quizes_list': latest_quizes_list},
        request
    ))


def detail(request, slug):
    try:
        quiz = Quiz.objects.filter(slug=slug)
        if ( len(quiz) == 0 ):
            raise Quiz.DoesNotExist
    except Quiz.DoesNotExist:
        raise Http404("The selected quiz could not be found")
    return render(request, 'quizzer/detail.html', {'quiz': quiz[0]})
