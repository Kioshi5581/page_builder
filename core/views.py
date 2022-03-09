from aiohttp import request
from django.shortcuts import render
from .models import *

# Create your views here.

def IndexView(request):
    model = Homepage.objects.all()
    context = {
        "template" : model,
    }
    return render(request, "index.html", context)


def DetailView(request, slug):
    model = Homepage.objects.get(slug=slug)
    model2 = pricing_table.objects.all()
    model3 = call_to_action.objects.all()
    model4 = review.objects.all()

    context = {
        "template": model,
        "tables": model2,
        "features": model3,
        "reviews": model4,
    }
    return render(request, "template.html", context)

def ServerDetailView(request, slug):
    model = Servers.objects.get(slug=slug)
    model2 = pricing_table.objects.all()
    model4 = review.objects.all()

    context = {
        "Servers": model,
        "tables": model2,
        "reviews": model4,
    }
    return render(request, "cheap-dedicated-server.html", context)