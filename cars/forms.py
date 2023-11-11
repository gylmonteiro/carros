from django import forms
from .models import Brand, Car

all_brands = Brand.objects.all()

# Esse método é seria o mais bruto para criar o form na mão
# class CarFormCreate(forms.Form):
#     model = forms.CharField(max_length=150)
#     brand = forms.ModelChoiceField(all_brands)
#     factory_year = forms.IntegerField()
#     model_year = forms.IntegerField()
#     plate = forms.CharField(max_length=10)
#     value = forms.FloatField()
#     photo = forms.ImageField()
#
#     def save(self):
#         car = Car(
#             model=self.cleaned_data['model'],
#             brand=self.cleaned_data['brand'],
#             factory_year= self.cleaned_data['factory_year'],
#             model_year=self.cleaned_data['model_year'],
#             plate=self.cleaned_data['plate'],
#             value=self.cleaned_data['value'],
#             photo=self.cleaned_data['photo'],
#         )
#
#         car.save()
#         return car

# Este método faz o mesmo de cima, otimizando o serviço de criação do form
class CarFormModel(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'Valor minimo necessario de 2000')
        return value

class BrandFormModel(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data.get('name')
        result_query = Brand.objects.filter(name__icontains=name)
        if result_query:
            self.add_error('name', 'Este campo já existe')
        return name