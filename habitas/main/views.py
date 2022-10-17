from django.shortcuts import render

# Create your views here.

# from .models import Question


def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}s
    return render(request, 'index.html')