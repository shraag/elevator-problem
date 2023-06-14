from django.db import models

# Create your models here.
class Elevator(models.Model):
    STATE_CHOICES = [
        ('U', 'Moving Up'),
        ('D', 'Moving Down'),
        ('S', 'Stopped'),
        ('M', 'Maintenance'),
    ]

    DOOR_CHOICES = [
        ('O', 'Open'),
        ('C', 'Closed'),
    ]

    state = models.CharField(max_length=1, choices=STATE_CHOICES, default='S')
    door = models.CharField(max_length=1, choices=DOOR_CHOICES, default='C')
    current_floor = models.IntegerField(default=0)
    destination_floor = models.IntegerField(null=True, blank=True)
    requests = models.JSONField(default=list, blank=True) # store as list of integers

    def move_up(self):
        if self.state != 'M':
            self.current_floor += 1
            self.state = 'U'
            self.save()

    def move_down(self):
        if self.state != 'M':
            if self.current_floor > 0:
                self.current_floor -= 1
                self.state = 'D'
                self.save()

    def stop(self):
        self.state = 'S'
        self.save()

    def open_door(self):
        self.door = 'O'
        self.save()

    def close_door(self):
        self.door = 'C'
        self.save()

    def add_request(self, floor):
        if floor not in self.requests:
            self.requests.append(floor)
            self.requests.sort()
            self.save()

    def remove_request(self, floor):
        if floor in self.requests:
            self.requests.remove(floor)
            self.save()