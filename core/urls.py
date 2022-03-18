from django.urls import include, path
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'pages-list', PageViewSet, basename="pages-list"),
router.register(r'servers-list', PageViewSet, basename="servers-list"),

urlpatterns = [
    path('', IndexView),
    path('page/<slug>/', DetailView),
    path('server/<slug>/', ServerDetailView),
    path('api/', include(router.urls)),
    # path('reseller-hosting/', TemplateView.as_view(template_name="reseller-hosting.html")),
    # path('cheap-vps-hosting/', TemplateView.as_view(template_name="cheap-vps-hosting.html")),
    # path('payments/', TemplateView.as_view(template_name="payments.html")),
    # path('affiliates/', TemplateView.as_view(template_name="affiliates.html")),
]
