from django.shortcuts import render
from .models import *
from .paginations import perpage_pagination
from rest_framework import viewsets
# from rest_framework import filters
from .serializers import *

# Create your views here.

def IndexView(request):
    model = Homepage.objects.all()
    model2 = Servers.objects.all()
    context = {
        "template" : model,
        "Servers" : model2,
    }
    return render(request, "index.html", context)


class PageViewSet(viewsets.ModelViewSet):
    queryset = Homepage.objects.all()

    serializer_class = HomepageSerializer
    # filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    # search_fields = ['^name', '=id', '^details', '^price']
    # filterset_fields = ['name', 'id', 'persons', 'details', 'price', 'price3']
    paginnation_class = perpage_pagination


class ServerSerializer(viewsets.ModelViewSet):
    queryset = Servers.objects.all()

    serializer_class = HomepageSerializer
    # filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    # search_fields = ['^name', '=id', '^details', '^price']
    # filterset_fields = ['name', 'id', 'persons', 'details', 'price', 'price3']
    paginnation_class = perpage_pagination


def DetailView(request, slug):
    model = Homepage.objects.get(slug=slug)
    # model2 = pricing_table.objects.all()
    # model3 = call_to_action.objects.all()
    # model4 = review.objects.all()

    context = {
        "template": model,
        # "tables": model2,
        # "features": model3,
        # "reviews": model4,
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