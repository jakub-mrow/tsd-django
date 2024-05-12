from rest_framework import serializers
from . import models


class TaskSerializer(serializers.ModelSerializer):
    #description = serializers.CharField(help_text="description")

    class Meta:
        model = models.Task
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    #model = serializers.CharField(help_text="model")
    #year = serializers.IntegerField()
    #price = serializers.FloatField()
    mileage = serializers.IntegerField(required=False)

    class Meta:
        model = models.Car
        fields = '__all__'