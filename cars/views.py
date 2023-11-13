from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Car
from .forms import CarFormModel, BrandFormModel
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
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

# View modificada com ListVew das views generics


class CarListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'
    paginate_by = 10

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)
        return cars

'''
 Funções para criar carro novo abaixo!
 ------------------------------------
'''

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

'''
@method_decorator(login_required(login_url='login_user'), name='dispatch')
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

'''

@method_decorator(login_required(login_url='login_user'), name='dispatch')
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarFormModel
    template_name = 'form_car.html'
    success_url = '/carros/'

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'

@method_decorator(login_required(login_url='login_user'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarFormModel
    template_name = 'car_update.html'
    # success_url = '/carros/'

    def get_success_url(self):
        return reverse_lazy('carDetail', kwargs={'pk': self.object.pk})

@method_decorator(login_required(login_url='login_user'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/carros/'

# Função para criar marcar
''''
def create_brand_views(request):
    form = BrandFormModel()
    if request.method == 'POST':

        form = BrandFormModel(request.POST)
        if form.is_valid():

            form.save()
            return redirect('listCars')

    return render(request, 'form_brand.html', {'forms': form})
'''

# Modificando a função por Class Views Generics
@method_decorator(login_required(login_url='login_user'), name='dispatch')
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
