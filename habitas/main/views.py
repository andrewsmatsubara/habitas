from django.shortcuts import render
from django.http import JsonResponse
from .models import Tree, Post

# Create your views here.


def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}s

    trees = (Tree.objects.all().values())
    context = {'trees': trees}

    return render(request, 'index.html', context)
