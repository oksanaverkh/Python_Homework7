from random import randint

def get_temperature(sensor):
    return randint(-20, 0) if sensor else randint(0, 20)

def get_tel_number():
    tel = f'8-{randint(900, 999)}-{randint(100, 999)}-{randint(10, 99)}-{randint(10, 99)}'
    return tel
print(get_tel_number())

# def get_wind_speed(sensor):
#     if sensor == 1:
#         return randint(0, 30)
#     else:
#         return randint(30, 50)

# def data_collection(sensor=1):
#     return (get_temperature(sensor), get_wind_speed(sensor), get_pressure(sensor))