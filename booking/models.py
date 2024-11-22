from django.db import models
from django.contrib.auth.models import User


class Machine(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=50, default='available')
    ipv4 = models.CharField(max_length=50)
    ipv6 = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    spuCores = models.IntegerField()
    ram = models.IntegerField()
    ssd = models.IntegerField()
    ip = models.GenericIPAddressField()
    bandwidth = models.IntegerField()
    operating_system = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    ownedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    Start = models.DateTimeField()
    End = models.DateTimeField()
