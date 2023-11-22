from django.db.models.signals import pre_save, pre_delete,post_save,post_delete
from django.dispatch import receiver
from cars.models import Car
# Importações para disparar ao cadastrar um objeto no model Car
import pyautogui as pg
import webbrowser as web
import time
import pandas as pd
@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    print("entrei no pré-save")

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