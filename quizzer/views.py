from django.shortcuts import render, get_object_or_404
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
    quiz = get_object_or_404(Quiz, slug=slug)
    return render(request, 'quizzer/detail.html', {'quiz': quiz})
