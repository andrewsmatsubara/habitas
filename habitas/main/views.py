from django.shortcuts import render
from .models import Tree, Post
from django.db.models import Count


def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}s

    trees = Tree.objects.all().select_related('species').annotate(n_posts=Count("posts"))
    context = {
        "trees": trees,
    }

    return render(request, "index.html", context)
