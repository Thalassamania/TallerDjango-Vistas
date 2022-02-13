import datetime
from ..models import Measurement
from ..models import Variable

def get_measurements():
    measurements = Measurement.objects.all() 
    return measurements

def get_measurement(mes_pk):
    measurement = Measurement.objects.get(pk=mes_pk)
    return measurement

def delete_measurement(mes_pk):
    measurement = Measurement.objects.get(pk=mes_pk)
    measurement.delete()
    return measurement

def update_measurement(mes_pk, mes):
    new_variable = Variable.objects.get(pk=mes["variable"])
    Measurement.objects.filter(id = mes_pk).update(variable = new_variable )
    Measurement.objects.filter(id = mes_pk).update(value = mes["value"])
    Measurement.objects.filter(id = mes_pk).update(unit = mes["unit"])
    Measurement.objects.filter(id = mes_pk).update(place = mes["place"])
    Measurement.objects.filter(id = mes_pk).update(dateTime= mes["dateTime"])
    measurement = Measurement.objects.get(pk=mes_pk)
    return measurement

def create_measurement(mes): 
    measurement = Measurement(
        variable = Variable.objects.get(pk=mes["variable"]),
        value = mes["value"],
        unit = mes["unit"],
        place = mes["place"],
        dateTime = mes["dateTime"]
    )
    measurement.save()
    return measurement