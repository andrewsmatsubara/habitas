from django.shortcuts import render
from .models import Tree, Post
from django.db.models import Count


def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}s

    trees = Tree.objects.all().annotate(n_posts=Count("posts"))
    context = {
        "trees": trees,
        "eco_stats": {
            "Toneladas de CO<sub>2</sub> retido": {
                'value': '{:,.2f}'.format(sum(t.stored_co2 for t in trees)),
                'value_text': 'ton.',
                'money': "{:.2f}".format(0).replace(".", ",")
            },
            "Água de chuva interceptada por ano": {
                'value': '{:,.0f}'.format(sum(t.stormwater_intercepted for t in trees)),
                'value_text': 'L',
                'money': "{:.2f}".format(0).replace(".", ",")
            },
        },
    }

    return render(request, "index.html", context)
