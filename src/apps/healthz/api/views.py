from rest_framework.response import Response
from rest_framework.views import APIView

from apps.healthz.services import get_health_status

from apps.healthz.api.serializers import HealthzSerializer


class HealthzView(APIView):
    """Return application health status."""

    def get(self, request):
        data = get_health_status()
        serializer = HealthzSerializer(data)
        return Response(serializer.data)
