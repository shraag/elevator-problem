from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Elevator
from .utils import assign_elevator

class ElevatorModelTestCase(TestCase):
    """
    Test case for the Elevator model.
    """
    def setUp(self):
        """
        Set up an elevator instance for the test.
        """
        self.elevator = Elevator.objects.create(current_floor=0)

    def test_move_up(self):
        """
        Test that the `move_up` method correctly increases the `current_floor`.
        """
        self.elevator.move_up()
        self.assertEqual(self.elevator.current_floor, 1)

    def test_move_down(self):
        """
        Test that the `move_down` method correctly decreases the `current_floor` without going below zero.
        """
        self.elevator.move_down()
        self.assertEqual(self.elevator.current_floor, 0)

class AssignElevatorTestCase(TestCase):
    """
    Test case for the `assign_elevator` utility function.
    """
    def setUp(self):
        """
        Set up two elevator instances at different floors.
        """
        self.elevator1 = Elevator.objects.create(current_floor=0)
        self.elevator2 = Elevator.objects.create(current_floor=5)

    def test_assign_elevator(self):
        """
        Test that the `assign_elevator` function correctly assigns the closest elevator.
        """
        elevator = assign_elevator(1)
        self.assertEqual(elevator, self.elevator1)

        elevator = assign_elevator(6)
        self.assertEqual(elevator, self.elevator2)

class APITestCase(TestCase):
    """
    Test case for the Elevator API.
    """
    def setUp(self):
        """
        Set up an elevator instance for the test.
        """
        self.client = APIClient()
        self.elevator = Elevator.objects.create(current_floor=0)

    def test_move_up(self):
        response = self.client.post(reverse('elevator-move-up', args=[self.elevator.id]))
        self.assertEqual(response.status_code, 200)
        self.elevator.refresh_from_db()
        self.assertEqual(self.elevator.current_floor, 1)

    def test_make_request(self):
        response = self.client.post(reverse('request-make-request'), {'floor': 3})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['elevator_id'], self.elevator.id)
