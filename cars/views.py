from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Car, Brand
from .forms import CarFormModel, BrandFormModel


# Create your views here.

def carviews(request):
    data = request.GET.get('search')
    if data:
        cars = Car.objects.filter(model__icontains=data).order_by('model')
    else:
        cars = Car.objects.all().order_by('model')
    return render(request, 'cars.html', {'cars': cars})


def create_car_views(request):
    form = CarFormModel()
    if request.method == 'POST':
        form = CarFormModel(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listCars')

    return render(request, 'form_car.html', {'forms': form})


def create_brand_views(request):
    form = BrandFormModel()
    if request.method == 'POST':

        form = BrandFormModel(request.POST)
        if form.is_valid():

            form.save()
            return redirect('listCars')

    return render(request, 'form_brand.html', {'forms': form})
