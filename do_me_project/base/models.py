from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank=True), 
    title = models.CharField(max_length=200, null = True, blank=True)
    description = models.TextField(null = True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["complete"]


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
    def get_area(self):
        return self.width * self.height
 
    def set_width(self, width):
        self.width = width
 
    def set_height(self, height):
        self.height = height

    def calculate_area_rectangle(width, height):
        return width * height

    print (calculate_area_rectangle(10, 2))