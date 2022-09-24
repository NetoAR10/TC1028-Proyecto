from datetime import datetime

def cambio_dia(ingreso, ahorro_1, gasto):
    ahorro_2 = ahorro_1 + ingreso - gasto
    cambio = ahorro_2 - ahorro_1
    return cambio

def budget(ingreso):
    esenciales = ingreso * 0.6
    guardar = ingreso * 0.3
    lujo = ingreso * 0.1
    print("esenciales: ", esenciales)
    print("guardar en ahorros: ", guardar)
    print("lujos y/o diversión: ", lujo)

def armar_fecha():
    try:
        fecha = input("Ingresa una fecha en el formato YYYY-MM-DD: ")
        datetime.strptime(fecha, '%Y-%m-%d')
        print("Fecha válida", fecha)
    except ValueError:
        print("Fecha inválida")
    
def menu():
    print("MENU")
    print("1) Budget")
    print("2) Cambio del Dia")
    print("3) Introducir Fecha")
    print("4) Historial (aun no sirve)")
    print("5) Salir")

print(menu())

opcion=int(input())

while opcion != 5: 
    if(opcion == 1):
        print("Introduce tu ingreso para armar tu budget")
        ingreso = float(input())
        if ingreso < 0:
            print("La cantidad no puede ser negativa")
        else:
            budget(ingreso)
            print(menu())
            opcion=int(input())

    elif(opcion == 2):
        print("escribe la cantidad ahorrada: ")
        ahorro_1 = float(input())
        print("escribe tu ingreso: ")
        ingreso = float(input())
        print("escribe tus gastos: ")
        gasto = float(input())
        if ahorro_1 < 0 or ingreso < 0 or gasto < 0:
            print("Ninguna cantidad puede ser negativa")
        else:
            print("el cambio del dia fue: ")
            print(cambio_dia(ingreso, ahorro_1, gasto))
            print(menu())
            opcion=int(input())

    elif(opcion == 3):
        armar_fecha()
        print(menu())
        opcion=int(input())

    elif(opcion == 4):
        print("el historial aun no existe")
        print(menu())
        opcion=int(input())

    elif(opcion < 1 or opcion > 5):
        print("elige opcion del 1 al 5")
        print(menu())
        opcion=int(input())