from django.urls import include, path


urlpatterns = [
    path('', include('apps.healthz.urls')),
]
