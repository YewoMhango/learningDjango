from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render

from myapp.models import Flower


def index(request: HttpRequest):
    q = request.GET.get('q', None)

    if q is None or q is "":
        flowers = Flower.objects.all()
        page_title = "Flowers"
    elif q is not None:
        flowers = Flower.objects.filter(title__contains=q)
        page_title = '“' + q + '” - search results'

    return render(request, "myapp/index.html", {'flowers': flowers, 'flower_count': flowers.count(), 'page_title': page_title})


def detail(request: HttpRequest, slug=None):
    flower = get_object_or_404(Flower, slug=slug)

    return render(request, 'myapp/detail.html', {'flower': flower, 'page_title': flower.title})


def tags(request: HttpRequest, slug=None):
    flowers = Flower.objects.filter(tags__slug=slug)

    return render(request, 'myapp/index.html', {'flowers': flowers, 'page_title': 'Flowers tagged with "' + slug + '"'})
