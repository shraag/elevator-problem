from .models import Elevator

def assign_elevator(floor):
    # Query the database for elevators that are either 'Stopped' or 'Moving'.
    elevators = Elevator.objects.exclude(state='M') #exlude Maintenance

    # Initialize variables to keep track of the optimal elevator and its distance to the request.
    optimal_elevator = None
    optimal_distance = float('inf')

    # Iterate over all elevators.
    for elevator in elevators:
        # Calculate the absolute distance from the elevator to the floor where the request was made.
        distance = abs(elevator.current_floor - floor)

        # Check if the elevator is stopped or moving in the direction of the request.
        # If it is, and its distance to the request is less than the optimal distance found so far,
        # then update the optimal elevator and the optimal distance.
        if elevator.state == 'S' or (elevator.state == 'U' and elevator.current_floor < floor) or (elevator.state == 'D' and elevator.current_floor > floor):
            if distance < optimal_distance:
                optimal_elevator = elevator
                optimal_distance = distance

    # If an optimal elevator was found, add the floor to its requests and return the elevator.
    if optimal_elevator is not None:
        optimal_elevator.add_request(floor)
        return optimal_elevator

    # If no elevator was found that can service the request, return None.
    else:
        return None
