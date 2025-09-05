from django.urls import path

from apps.healthz.api.views import HealthzView

urlpatterns = [
    path('healthz/', HealthzView.as_view(), name='healthz'),
]
