import requests

# Create some elevators
for i in range(5):
    response = requests.post('http://127.0.0.1:8000/api/elevators/', data={'current_floor': i})
    print(response.json())
    print("--------------------")
# List all elevators
response = requests.get('http://127.0.0.1:8000/api/elevators/')
elevators = response.json()
print(elevators)
print("--------------------")
# If there are any elevators, retrieve the first one and move it up
if elevators:
    elevator_id = elevators[0]['id']
    response = requests.get(f'http://127.0.0.1:8000/api/elevators/{elevator_id}/')
    print(response.json())
    print("--------------------")
    response = requests.post(f'http://127.0.0.1:8000/api/elevators/{elevator_id}/move_up/')
    print(response.json())
    print("--------------------")