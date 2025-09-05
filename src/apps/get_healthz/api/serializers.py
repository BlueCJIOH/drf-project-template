from rest_framework import serializers


class HealthzSerializer(serializers.Serializer):
    status = serializers.CharField(read_only=True)
