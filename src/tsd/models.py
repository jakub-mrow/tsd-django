from django.db import models


class Task(models.Model):
    description = models.CharField(max_length=128, help_text="Task description")


class Car(models.Model):
    model = models.CharField(max_length=128, help_text="Car model")
    year = models.IntegerField(help_text="Car year")
    price = models.FloatField(help_text="Car price")
    mileage = models.FloatField(help_text="Car mileage", default=100)
