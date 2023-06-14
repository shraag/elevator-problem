from django.db import models

# Create your models here.
class Elevator(models.Model):
    # Choices for the state of the elevator
    STATE_CHOICES = [
        ('U', 'Moving Up'),
        ('D', 'Moving Down'),
        ('S', 'Stopped'),
        ('M', 'Maintenance'),
    ]

    # Choices for the door of the elevator
    DOOR_CHOICES = [
        ('O', 'Open'),
        ('C', 'Closed'),
    ]

    # State of the elevator: 'Moving Up', 'Moving Down', 'Stopped', or 'Maintenance'
    state = models.CharField(max_length=1, choices=STATE_CHOICES, default='S')

    # State of the elevator door: 'Open' or 'Closed'
    door = models.CharField(max_length=1, choices=DOOR_CHOICES, default='C')

    # Current floor of the elevator
    current_floor = models.IntegerField(default=0)

    # Destination floor of the elevator
    destination_floor = models.IntegerField(null=True, blank=True)

    # Requests for the elevator stored as a list of integers
    requests = models.JSONField(default=list, blank=True)

    # Function to move the elevator up by one floor
    def move_up(self):
        if self.state != 'M':
            self.current_floor += 1
            self.state = 'U'
            self.save()

    # Function to move the elevator down by one floor
    def move_down(self):
        if self.state != 'M':
            if self.current_floor > 0:
                self.current_floor -= 1
                self.state = 'D'
                self.save()

    # Function to stop the elevator
    def stop(self):
        self.state = 'S'
        self.save()

    # Function to open the door of the elevator
    def open_door(self):
        self.door = 'O'
        self.save()

    # Function to close the door of the elevator
    def close_door(self):
        self.door = 'C'
        self.save()

    # Function to add a floor to the list of requests for the elevator
    def add_request(self, floor):
        if floor not in self.requests:
            self.requests.append(floor)
            self.requests.sort()
            self.save()

    # Function to remove a floor from the list of requests for the elevator
    def remove_request(self, floor):
        if floor in self.requests:
            self.requests.remove(floor)
            self.save()