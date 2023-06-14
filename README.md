# Elevator System API

This is a Django-based REST API for managing an elevator system. 

## Architecture
The application is built using the Django framework and Django Rest Framework. The data is stored in a SQLite database that comes with Django by default. The logic of elevator control is kept in the `Elevator` model in the `elevators` app. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You'll need to have Python 3 and Django installed on your local machine. If you don't have Python or Django installed, you can find the downloads and instructions here:
- Python: https://www.python.org/downloads/
- Django: https://docs.djangoproject.com/en/4.0/intro/install/

### Installing

1. Clone this repository by running the following command in your terminal:
    ```bash
    git clone https://github.com/your_username/elevator-problem.git
    ```

2. Navigate into the project directory:
    ```bash
    cd elevator_system
    ```

3. Install the necessary Python packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the migrations:
    ```bash
    python manage.py migrate
    ```

5. You're ready to go! Start the server:
    ```bash
    python manage.py runserver
    ```

## Usage

Below are the available API endpoints and their functions:

1. `GET /elevators/`: Fetch all elevators
2. `GET /elevators/<id>/`: Fetch a specific elevator
3. `GET /elevators/<id>/state/`: Fetch the state of a specific elevator
4. `GET /elevators/<id>/door/`: Fetch the door status of a specific elevator
5. `GET /elevators/<id>/current_floor/`: Fetch the current floor of a specific elevator
6. `GET /elevators/<id>/destination_floor/`: Fetch the destination floor of a specific elevator
7. `GET /elevators/<id>/requests/`: Fetch all requests for a specific elevator
8. `POST /elevators/`: Create an elevator
9. `POST /elevators/<id>/move_up/`: Move a specific elevator up by one floor
10. `POST /elevators/<id>/move_down/`: Move a specific elevator down by one floor
11. `POST /elevators/<id>/stop/`: Stop a specific elevator
12. `POST /elevators/<id>/open_door/`: Open the door of a specific elevator
13. `POST /elevators/<id>/close_door/`: Close the door of a specific elevator
14. `POST /elevators/<id>/add_request/`: Add a floor request for a specific elevator
15. `POST /requests/make_request/`: Make a floor request

Note: Replace `<id>` with the actual ID of an elevator.

## Testing
Open Terminal and Navigate to the project directory 'elevator_system' as above. To run the test_api.py file, type the following command:
    ```bash
    python3 test_api.py
    ```

test_api.py initializes 5 elevators and store their IDs. It also sends GET and POST requests to most of the API endpoints mentioned above.     

To run the tests in tests.py, navigate to the project directory and type the following command:
    ```bash
    python manage.py test
    ```

## Built With

* [Python 3](https://www.python.org/) - The programming language used.
* [Django](https://www.djangoproject.com/) - The web framework used.
* [Django Rest Framework](https://www.django-rest-framework.org/) - Toolkit used to build the API.

## Authors

* **Shranay Agarwal** - *Initial work* - [shraag](https://github.com/shraag)

## Acknowledgments

* This project is part of a coding assignment for JumpingMinds.
