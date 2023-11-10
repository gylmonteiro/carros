from django import forms
from .models import Brand, Car

all_brands = Brand.objects.all()


class CarFormCreate(forms.Form):
    model = forms.CharField(max_length=150)
    brand = forms.ModelChoiceField(all_brands)
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    value = forms.FloatField()
    photo = forms.ImageField()

    def save(self):
        car = Car(
            model=self.cleaned_data['model'],
            brand=self.cleaned_data['brand'],
            factory_year= self.cleaned_data['factory_year'],
            model_year=self.cleaned_data['model_year'],
            plate=self.cleaned_data['plate'],
            value=self.cleaned_data['value'],
            photo=self.cleaned_data['photo'],
        )

        car.save()
        return car
