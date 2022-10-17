from django.shortcuts import render
from .models import Tree

# Create your views here.

# from .models import Question


def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}s

    trees = (Tree.objects.all().values())
    context = {'trees': trees}

    return render(request, 'index.html', context)