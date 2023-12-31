from django.db.models import Sum
from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from cars.models import Car, CarInvetory

# import pywhatkit as wa (não vai ser necessário no momento. Somente testes)

'''
# Importações para disparar ao cadastrar um objeto no model Car
# import pyautogui as pg
# import webbrowser as web
# import time
# import pandas as pd
'''

def car_invetory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        all_value=Sum('value')
    )['all_value']
    CarInvetory.objects.create(cars_count=cars_count, cars_value=cars_value)
@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_invetory_update()

@receiver(post_delete, sender=Car)
def car_delete_save(sender, instance, **kwargs):
    car_invetory_update()
@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        instance.bio = "Biografia gerada por IA"

'''
# método com signails para enviar mensagem via whatsapp

@receiver(post_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    phone = '55_84999685922'
    name_car = instance.model
    message = f'Esse é um teste com o cadatro do carro {name_car}'
    time.sleep(4)
    web.open(f'https://web.whatsapp.com/send?phone={phone}&text={message}')
    time.sleep(6)
    width, height = pg.size()
    pg.click(width/2, height/2)

    time.sleep(8)
    pg.press('esc')
    time.sleep(5)
    pg.press('enter')
    time.sleep(10)
    pg.hotkey('ctrl', 'w')
'''

'''
# Uma maneira de enviar com a biblioteca pywhatkit
@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    phone = '+5584998181036'
    name_car = instance.model
    message = f'Esse é um teste com o cadatro do carro {name_car}'
    wa.sendwhatmsg_instantly(phone, message, tab_close=True, wait_time=20, close_time=5)
    # return instance
'''
