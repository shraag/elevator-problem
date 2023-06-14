import requests

# Base url of your API
base_url = 'http://127.0.0.1:8000/api/'

# Initialize 5 elevators and store their IDs
elevator_ids = []
for i in range(5):
    response = requests.post(base_url + 'elevators/', data={'current_floor': 0})
    elevator_id = response.json()['id']
    elevator_ids.append(elevator_id)
    print(f"Elevator {i+1} initialized with id {elevator_id}")

# Make a request from the 3rd floor
response = requests.post(base_url + 'requests/make_request/', data={'floor': 3})
print("Request made: ", response.json())

# Perform operations on the first elevator
first_elevator_id = elevator_ids[0]

# Fetch all requests for the first elevator
response = requests.get(base_url + f'elevators/{first_elevator_id}/requests/')
print(f"Requests for elevator {first_elevator_id}: ", response.json())

# Fetch the next destination for the first elevator
response = requests.get(base_url + f'elevators/{first_elevator_id}/destination_floor/')
print(f"Next destination for elevator {first_elevator_id}: ", response.json())

# Fetch the direction of the first elevator
response = requests.get(base_url + f'elevators/{first_elevator_id}/state/')
print(f"Direction of elevator {first_elevator_id}: ", response.json())

# Set first elevator status to 'Stopped'
response = requests.patch(base_url + f'elevators/{first_elevator_id}/', data={'status': 'M'})
print(f"Status of elevator {first_elevator_id} set to Stopped: ", response.json())

# Open the door of first elevator
response = requests.post(base_url + f'elevators/{first_elevator_id}/open_door/')
print(f"Door of elevator {first_elevator_id} opened: ", response)

# Close the door of first elevator
response = requests.post(base_url + f'elevators/{first_elevator_id}/close_door/')
print(f"Door of elevator {first_elevator_id} closed: ", response)