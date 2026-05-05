def verificar_temperatura(motor):
    temp_atual = 38
    return temp_atual

status_temp = verificar_temperatura("motor_base")

if status_temp > 40:
    print("Alerta: motor muito quente!")
else:
    print("Temperatura normal")