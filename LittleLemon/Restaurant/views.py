from django.shortcuts import render
from django.http import HttpResponse
from API.models import Menu, Booking

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def menu(request):
    menu = Menu.objects.all()
    for item in menu:
        print(item.title)
    context = {"menu": menu}
    return render(request, 'menu.html', context)

def display_menu_item(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ""
    context = {"menu_item": menu_item}

    return render(request, 'menu_item.html', context)

def book(request):
    if request.method == 'POST':
        name = request.POST['name']
        guests_num = request.POST['guests_num']
        bookingdate = request.POST['bookingdate']
        new_booking = Booking.objects.create(
            name = name,
            guests_num = guests_num,
            bookingdate = bookingdate,
        )
        context = {"name": name, "guests_num": guests_num, "bookingdate": bookingdate}
        return render(request, 'booking_confirmation.html', context)
    return render(request, 'book.html', {})

