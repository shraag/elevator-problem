from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Elevator
from .serializers import ElevatorSerializer
from .utils import assign_elevator

# ElevatorViewSet is a class-based view that inherits from ModelViewSet,
# It provides the list, create, retrieve, update, and destroy actions.
class ElevatorViewSet(viewsets.ModelViewSet):
    # Define the queryset and serializer_class
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer

    # Define the custom action move_up
    @action(detail=True, methods=['post'])
    def move_up(self, request, pk=None):
        elevator = self.get_object()
        elevator.move_up()
        return Response(status=status.HTTP_200_OK)

    # Define the custom action move_down
    @action(detail=True, methods=['post'])
    def move_down(self, request, pk=None):
        elevator = self.get_object()
        elevator.move_down()
        return Response(status=status.HTTP_200_OK)

    # Define the custom action stop
    @action(detail=True, methods=['post'])
    def stop(self, request, pk=None):
        elevator = self.get_object()
        elevator.stop()
        return Response(status=status.HTTP_200_OK)

    # Define the custom action open_door
    @action(detail=True, methods=['post'])
    def open_door(self, request, pk=None):
        elevator = self.get_object()
        elevator.open_door()
        return Response(status=status.HTTP_200_OK)

    # Define the custom action close_door
    @action(detail=True, methods=['post'])
    def close_door(self, request, pk=None):
        elevator = self.get_object()
        elevator.close_door()
        return Response(status=status.HTTP_200_OK)

    # Define the custom action add_request
    @action(detail=True, methods=['post'])
    def add_request(self, request, pk=None):
        elevator = self.get_object()
        floor = request.data.get('floor')
        if floor is not None:
            elevator.add_request(floor)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    # Define the custom action state
    @action(detail=True, methods=['get'])
    def state(self, request, pk=None):
        elevator = self.get_object()
        return Response({'state': elevator.state})

    # Define the custom action door
    @action(detail=True, methods=['get'])
    def door(self, request, pk=None):
        elevator = self.get_object()
        return Response({'door': elevator.door})

    # Define the custom action current_floor
    @action(detail=True, methods=['get'])
    def current_floor(self, request, pk=None):
        elevator = self.get_object()
        return Response({'current_floor': elevator.current_floor})

    # Define the custom action destination_floor
    @action(detail=True, methods=['get'])
    def destination_floor(self, request, pk=None):
        elevator = self.get_object()
        return Response({'destination_floor': elevator.destination_floor})

    # Define the custom action requests
    @action(detail=True, methods=['get'])
    def requests(self, request, pk=None):
        elevator = self.get_object()
        return Response({'requests': elevator.requests})


# RequestViewSet is a class-based view that inherits from ViewSet,
# It doesn't provide any default actions, but allows to define custom actions
class RequestViewSet(viewsets.ViewSet):
    # Define the custom action make_request
    @action(detail=False, methods=['post'])
    def make_request(self, request):
        # Extract the floor number from the request data
        floor = int(request.data.get('floor'))
        
        # If floor number is provided in the request
        if floor is not None:
            # Assign an elevator for the request
            elevator = assign_elevator(floor)
            
            # If an elevator is available, return its id
            if elevator is not None:
                return Response({'elevator_id': elevator.id}, status=status.HTTP_200_OK)
            # If no elevators are available, return 204 No Content status
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
        # If floor number is not provided in the request, return 400 Bad Request status
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
