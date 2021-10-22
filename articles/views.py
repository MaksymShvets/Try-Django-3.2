from django.shortcuts import render
from .models import Article


def article_detail_view(request, id=None):
    article_obj = None
    if id:
        article_obj = Article.objects.get(id=id)
    context = {
        "object": None,
    }
    return render(request, "articles/detail.html", context=context)
