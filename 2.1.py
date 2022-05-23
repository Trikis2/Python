temperature = int(input("Введите температуру в комнате: "))
desired_temperature = int(input("Введите желаемую температуру: "))
air_humidity = int(input("Введите влажность воздуха: "))

if temperature > desired_temperature and air_humidity < 80:
    print("On")
else:
    print("Off")