from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    guests_num = models.IntegerField()
    bookingdate = models.DateTimeField()

    def __str__(self):
        return f'{self.name} - {self.guests_num} - {self.bookingdate}'

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    inventory = models.SmallIntegerField()

    def __str__(self):
        return f'{self.title}: {str(self.price)}'
