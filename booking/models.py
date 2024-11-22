from django.db import models
from django.contrib.auth.models import User


class Machine(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=50, default='available')
    ipv4 = models.GenericIPAddressField(max_length=50)
    ipv6 = models.GenericIPAddressField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50)
    cpuCores = models.IntegerField()
    ram = models.IntegerField()
    ssd = models.IntegerField(blank=True, null=True)
    hdd = models.IntegerField(blank=True, null=True)
    operatingSystem = models.CharField(max_length=50)
    bandwidth = models.IntegerField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    bookedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    bookedFrom = models.DateTimeField()
    bookedUntil = models.DateTimeField()
