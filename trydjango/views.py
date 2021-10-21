import random
from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article


def home_view(request):
    name = "Justin"
    random_id = random.randint(1, 2)
    article_obj = Article.objects.get(id=random_id)
    article_queryset = Article.objects.all()

    context = {
        'object_list': article_queryset,
        'title': article_obj.title,
        'id': article_obj.id,
        'content': article_obj.content
    }
    html_string = render_to_string('home-view.html', context=context)

    return HttpResponse(html_string)
