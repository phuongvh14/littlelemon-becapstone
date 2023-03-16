from django.test import TestCase
from API.models import Menu, Booking

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(f"{item.title}: {item.price}", "IceCream: 80")

class BookingTest(TestCase):
    def test_get_item(self):
        item = Booking.objects.create(name="Phuong test", guests_num="120", bookingdate="2023-03-24 11:51:00")
        self.assertEqual(f"{item.name} - {item.guests_num} - {item.bookingdate}", "Phuong test - 120 - 2023-03-24 11:51:00")