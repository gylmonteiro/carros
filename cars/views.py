from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Car, Brand
from .forms import CarFormModel, BrandFormModel
from django.views import View
from django.views.generic import ListView

# Primeira view criada como função
'''
def carviews(request):
    data = request.GET.get('search')
    if data:
        cars = Car.objects.filter(model__icontains=data).order_by('model')
    else:
        cars = Car.objects.all().order_by('model')
    return render(request, 'cars.html', {'cars': cars})

'''

# View no formato de class based View
'''
class CarView(View):
    def get(self, request):
        data = request.GET.get('search')
        if data:
            cars = Car.objects.filter(model__icontains=data).order_by('model')
        else:
            cars = Car.objects.all().order_by('model')
        return render(request, 'cars.html', {'cars': cars})
'''

# Testanto a listagem com ListVew das views generics

class CarListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)
        return cars

# Função para criar carro com view baseada em função
'''
def create_car_views(request):
    form = CarFormModel()
    if request.method == 'POST':
        form = CarFormModel(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listCars')

    return render(request, 'form_car.html', {'forms': form})
'''


class CreateCarView(View):
    def get(self, request):
        form = CarFormModel()
        return render(request, 'form_car.html', {'forms': form})

    def post(self, request):
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

class CreateBrandView(View):
    def get(self, request):
        form = BrandFormModel()
        return render(request, 'form_brand.html', {'forms': form})

    def post(self, request):
        form = BrandFormModel(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listCars')
        return render(request, 'form_brand.html', {'forms': form})
