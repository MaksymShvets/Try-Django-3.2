from django.shortcuts import render
from .models import Article


def article_search_view(request):
    query_dict = request.GET  # this is a dict

    try:
        query = int(query_dict.get("q"))
    except:
        query = None

    article_obj = None
    if query:
        article_obj = Article.objects.get (id=query)
    context = {
        "object": article_obj,
    }
    return render(request, "articles/search.html", context=context)


def article_detail_view(request, id=None):
    article_obj = None
    if id:
        article_obj = Article.objects.get(id=id)
    context = {
        "object": article_obj,
    }
    return render(request, "articles/detail.html", context=context)
