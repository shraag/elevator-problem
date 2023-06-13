from .models import Elevator

def assign_elevator(floor):
    # Find the nearest elevator which is stopped or moving towards the request
    elevators = Elevator.objects.exclude(state='M')
    optimal_elevator = None
    optimal_distance = float('inf')
    for elevator in elevators:
        distance = abs(elevator.current_floor - floor)
        if elevator.state == 'S' or (elevator.state == 'U' and elevator.current_floor < floor) or (elevator.state == 'D' and elevator.current_floor > floor):
            if distance < optimal_distance:
                optimal_elevator = elevator
                optimal_distance = distance

    if optimal_elevator is not None:
        optimal_elevator.add_request(floor)
        return optimal_elevator
    else:
        return None