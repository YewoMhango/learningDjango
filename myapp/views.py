from django.shortcuts import get_object_or_404, render

from myapp.models import Flower


def index(request):
    flowers = Flower.objects.all()

    return render(request, "myapp/index.html", {'flowers': flowers, 'page_title': 'Flowers'})


def detail(request, slug=None):
    flower = get_object_or_404(Flower, slug=slug)

    return render(request, 'myapp/detail.html', {'flower': flower, 'page_title': flower.title})


def tags(request, slug=None):
    flowers = Flower.objects.filter(tags__slug=slug)

    return render(request, 'myapp/index.html', {'flowers': flowers, 'page_title': 'Flowers tagged with "' + slug + '"'})
