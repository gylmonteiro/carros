from django.db import models

class Brand(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return f"{self.name}"
# Create your models here.
class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=150)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name="car_brand" )
    factory_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=20, blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.model} | {self.brand}"


class CarInvetory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.cars_count} -  {self.cars_value}'
