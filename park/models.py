from django.db import models

class FleetOwner(models.Model):
    name = models.CharField(max_length=255)
    number_phone = models.IntegerField()

    def __str__(self):
        return self.name

class VehiclePark(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    fleet_owner = models.ForeignKey(FleetOwner, on_delete=models.CASCADE, related_name='vehicle_parks')

    def __str__(self):
        return self.name

class Car(models.Model):
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    registration_no = models.CharField(max_length=64)
    vehicle_park = models.ForeignKey(VehiclePark, on_delete=models.SET_NULL, null=True, related_name='cars')

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}), {self.registration_no}"

class Driver(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    license_number = models.CharField(max_length=64)
    car = models.OneToOneField(Car, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Route(models.Model):
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    distance_in_km = models.DecimalField(max_digits=6, decimal_places=2)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, related_name='routes')

    def __str__(self):
        return f"{self.origin} -> {self.destination}"

