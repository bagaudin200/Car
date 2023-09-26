from django.core.management.base import BaseCommand
from fleet.models import FleetOwner, VehiclePark, Car, Driver

class Command(BaseCommand):
    help = 'Create a fleet of cars.'

    def handle(self, *args, **options):

        fleet_owner, _ = FleetOwner.objects.get_or_create(name='The Fleet Owner')


        vehicle_park, _ = VehiclePark.objects.get_or_create(
            name='The Vehicle Park',
            location='123 Main St',
            fleet_owner=fleet_owner,
        )


        cars_data = [
            {'brand': 'Toyota', 'model': 'Camry', 'year': 2020, 'registration_no': 'ABC123'},
            {'brand': 'Honda', 'model': 'Civic', 'year': 2019, 'registration_no': 'DEF456'},
            {'brand': 'Ford', 'model': 'Fiesta', 'year': 2018, 'registration_no': 'GHI789'},
        ]


        for car_data in cars_data:

            car, _ = Car.objects.get_or_create(
                brand=car_data['brand'],
                model=car_data['model'],
                year=car_data['year'],
                registration_no=car_data['registration_no'],
                vehicle_park=vehicle_park,
            )


            driver_name = car_data['registration_no'][-3:] 
            driver, _ = Driver.objects.get_or_create(
                first_name=f'Driver {driver_name}',
                last_name='Smith',
                license_number=car_data['registration_no'],
                car=car,
            )

        self.stdout.write(self.style.SUCCESS('Successfully created a fleet of cars!'))
