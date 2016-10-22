from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet

from tests.models import TestModel


class TestSerializer(ModelSerializer):
    class Meta:
        model = TestModel
        fields = ('id', 'n')


class TestViewSet(ReadOnlyModelViewSet):
    queryset = TestModel.objects.all()
    serializer_class = TestSerializer
    ordering = 'id'
