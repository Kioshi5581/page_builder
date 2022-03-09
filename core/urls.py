from django.urls import path
from .views import *
from django.views.generic import TemplateView


urlpatterns = [
    path('', IndexView),
    path('page/<slug>/', DetailView),
    path('server/<slug>/', ServerDetailView),
    
    # path('reseller-hosting/', TemplateView.as_view(template_name="reseller-hosting.html")),
    # path('cheap-vps-hosting/', TemplateView.as_view(template_name="cheap-vps-hosting.html")),
    # path('payments/', TemplateView.as_view(template_name="payments.html")),
    # path('affiliates/', TemplateView.as_view(template_name="affiliates.html")),
]
