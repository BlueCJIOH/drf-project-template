from django.urls import include, path


urlpatterns = [
    path('', include('apps.get_healthz.urls')),
]
