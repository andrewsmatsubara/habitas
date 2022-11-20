from django.shortcuts import render
from django.http import JsonResponse
from .models import Tree, Post
from django.db.models import Count


def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}s

    trees = Tree.objects.all().annotate(n_posts=Count("posts"))
    posts = Post.objects.all()
    context = {
        "trees": trees,
        "stats": {
            "Árvores cadastradas": trees.count(),
            "Espécies": trees.aggregate(
                n_species=Count("nome_cientifico", distinct=True)
            )["n_species"],
            "Ton. de CO<sub>2</sub> retido": round(sum(t.stored_co2 for t in trees), 1),
            "Comentários": posts.count(),
        },
    }

    return render(request, "index.html", context)
