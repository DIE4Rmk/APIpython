from rest_framework import viewsets
from app.models import tasks
from app.serializer import tasksFilter, tasksSerializer
from django_filters.rest_framework import DjangoFilterBackend


class tasksViewSet(viewsets.ModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    queryset = tasks.objects.all().order_by("id")
    serializer_class = tasksSerializer
    filterset_class = tasksFilter
    http_method_names = ['get', 'post', 'put', 'delete']
    