from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from . import serializers, models

mileage_param = openapi.Parameter('mileage', openapi.IN_QUERY, description="mileage manual param", type=openapi.TYPE_NUMBER)


class TaskViewSet(viewsets.ModelViewSet):
    """
    Return information about task.
    """
    serializer_class = serializers.TaskSerializer
    queryset = models.Task.objects.all()


@api_view(['GET', 'POST'])
def first_endpoint(request):
    if request.method == 'GET':
        # Logic for handling GET requests
        return Response({"message": "This is a GET request"}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        # Logic for handling POST requests
        return Response({"message": "This is a POST request"}, status=status.HTTP_201_CREATED)


class CarViewSet(viewsets.ModelViewSet):
    """
    Return information about car.
    """
    serializer_class = serializers.CarSerializer
    queryset = models.Car.objects.all()


    @swagger_auto_schema(request_body=serializers.CarSerializer, manual_parameters=[mileage_param])
    def create(self, request, *args, **kwargs):
        # query param to set car milage to the value of the query param
        car_mileage = request.query_params.get('mileage')

        if car_mileage is not None:
            # If mileage is provided, set it and create the car
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(mileage=car_mileage)
            return Response({"message": "Car created with provided mileage"}, status=status.HTTP_201_CREATED)
        else:
            # If mileage is not provided, create the car with default behavior
            return super().create(request, *args, **kwargs)

