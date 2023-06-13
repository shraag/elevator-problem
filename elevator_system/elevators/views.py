from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Elevator
from .serializers import ElevatorSerializer
from .utils import assign_elevator

class ElevatorViewSet(viewsets.ModelViewSet):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer

    @action(detail=True, methods=['post'])
    def move_up(self, request, pk=None):
        elevator = self.get_object()
        elevator.move_up()
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def move_down(self, request, pk=None):
        elevator = self.get_object()
        elevator.move_down()
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def stop(self, request, pk=None):
        elevator = self.get_object()
        elevator.stop()
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def open_door(self, request, pk=None):
        elevator = self.get_object()
        elevator.open_door()
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def close_door(self, request, pk=None):
        elevator = self.get_object()
        elevator.close_door()
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def add_request(self, request, pk=None):
        elevator = self.get_object()
        floor = request.data.get('floor')
        if floor is not None:
            elevator.add_request(floor)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class RequestViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def make_request(self, request):
        floor = request.data.get('floor')
        if floor is not None:
            elevator = assign_elevator(floor)
            if elevator is not None:
                return Response({'elevator_id': elevator.id}, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)