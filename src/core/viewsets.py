from typing import Any, Protocol, Type

from django.core.exceptions import ImproperlyConfigured
from rest_framework.serializers import Serializer

from src.core.validators import Validator


class ViewsetWithValidationProtocol(Protocol):
    validator_class: Type[Validator] | None


class ValidationMixin(ViewsetWithValidationProtocol):
    def get_validator_class(self) -> Type[Validator]:
        if self.validator_class is None:
            raise ImproperlyConfigured("Please set validator_class class variable")

        return self.validator_class

    def validate(self, data: dict, context: dict | None = None) -> None:
        Validator = self.get_validator_class()
        Validator.do(data, context=self.get_validator_context())

    def get_validator_context(self) -> dict[str, Any]:
        return {
            "request": self.request,  # type: ignore
        }


class MultiSerializerMixin:
    def get_serializer_class(self, action: str | None = None) -> Type[Serializer]:
        """
        Look for serializer class in self.serializer_action_classes, which
        should be a dict mapping action name (key) to serializer class (value),
        i.e.:

        class MyViewSet(MultiSerializerViewSetMixin, ViewSet):
            serializer_class = MyDefaultSerializer
            serializer_action_classes = {
               'list': MyListSerializer,
               'my_action': MyActionSerializer,
            }

            @action
            def my_action:
                ...

        If there's no entry for that action then just fallback to the regular
        get_serializer_class lookup: self.serializer_class, DefaultSerializer.
        """
        if action is None:
            action = self.action  # type: ignore

        try:
            return self.serializer_action_classes[action]  # type: ignore
        except (KeyError, AttributeError):
            return super().get_serializer_class()  # type: ignore
