from django_filters import rest_framework as filters
from rest_framework import serializers
from app.models import tasks


class tasksFilter(filters.FilterSet):
    id_user = filters.CharFilter()

    class Meta:
        model = tasks
        fields = ['id']


class tasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = tasks
        fields = '__all__'
