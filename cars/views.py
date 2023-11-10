from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Car
from .forms import CarFormCreate


# Create your views here.

def carviews(request):
    data = request.GET.get('search')
    if data:
        cars = Car.objects.filter(model__icontains=data).order_by('model')

    else:
        cars = Car.objects.all().order_by('model')
    return render(request, 'cars.html', {'cars': cars})


def create_car_views(request):
    form = CarFormCreate()
    if request.method == 'POST':
        form = CarFormCreate(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listCars')
    else:
        return render(request, 'form_car.html', {'forms': form})
