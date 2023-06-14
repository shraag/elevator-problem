import requests

# Base url of your API
base_url = 'http://127.0.0.1:8000/api/'

def initialize_elevators(n):
    for i in range(n):
        response = requests.post(base_url + 'elevators/', data={'current_floor': 0})
        print(f"Elevator {i+1} initialized: ", response.json())

def fetch_all_requests(elevator_id):
    response = requests.get(base_url + f'elevators/{elevator_id}/requests/')
    print(f"Requests for elevator {elevator_id}: ", response.json())

def fetch_next_destination(elevator_id):
    response = requests.get(base_url + f'elevators/{elevator_id}/destination_floor/')
    print(f"Next destination for elevator {elevator_id}: ", response.json())

def fetch_direction(elevator_id):
    response = requests.get(base_url + f'elevators/{elevator_id}/state/')
    print(f"Direction of elevator {elevator_id}: ", response.json())

def make_request(floor):
    response = requests.post(base_url + 'requests/make_request/', data={'floor': floor})
    
    if response.content:
        print("Request made: ", response.json())
    else:
        print("No response from the server for the make request API.")

def set_elevator_status(elevator_id, status):
    response = requests.patch(base_url + f'elevators/{elevator_id}/', data={'status': status})
    print(f"Status of elevator {elevator_id} set to {status}: ", response.json())

def open_door(elevator_id):
    response = requests.post(base_url + f'elevators/{elevator_id}/open_door/')
    print(f"Door of elevator {elevator_id} opened: ", response.json())

def close_door(elevator_id):
    response = requests.post(base_url + f'elevators/{elevator_id}/close_door/')
    print(f"Door of elevator {elevator_id} closed: ", response.json())

# Initialize elevators
initialize_elevators(5)

# Make a request
make_request(3)

# Fetch all requests for elevator 1
fetch_all_requests(67)

# Fetch the next destination for elevator 1
fetch_next_destination(67)

# Fetch the direction of elevator 1
fetch_direction(67)

# Set elevator 1 status to 'not working'
set_elevator_status(67, 'Stopped')

# Open the door of elevator 1
open_door(67)

# Close the door of elevator 1
close_door(67)