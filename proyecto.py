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
    return fecha

def pedir_ingreso():
    print("Escribe tu ingreso: ")
    return float(input())

def pedir_gasto():
    print("Escribe tu gasto: ")
    return float(input())

lista = [26,500,64,167,385]

def minimo(lista):
    min = lista[0]
    for num in lista:
        if num < min:
            min = num
    return min

def maximo(lista):
    max = lista[0]
    for num in lista:
        if num > max:
            max = num
    return max

def longitud(lista):
    cont = 0
    for cont in lista:
        cont = cont + 1
    return cont

def prom(lista):
    promedio = sum(lista) / len(lista)
    return promedio

historial = []
    
def menu():
    print("\nMENU")
    print("1) Budget")
    print("2) Cambio del Dia")
    print("3) Introducir Fecha")
    print("4) Historial")
    print("5) Datos de Gastos")
    print("6) Salir")

menu()

opcion=int(input())

while opcion != 6: 
    if(opcion == 1):
        print("Introduce tu ingreso para armar tu budget")
        ingreso = float(input())
        if ingreso < 0:
            print("La cantidad no puede ser negativa")
        else:
            budget(ingreso)
            menu()
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
            menu()
            opcion=int(input())

    elif(opcion == 3):
        armar_fecha()
        menu()
        opcion=int(input())

    elif(opcion == 4):
        fecha = armar_fecha()
        ingreso = pedir_ingreso()
        gasto = pedir_gasto()
        datos_dia = [fecha, ingreso, gasto]
        historial.append(datos_dia)
        for dia in historial:
            print(f"el dia es {dia[0]} el ingreso fue de {dia[1]} el gasto fue de {dia[2]}")
        menu()
        opcion=int(input())

    elif(opcion == 5):
        print("Tu gasto mayor es:", maximo(lista))
        print("Tu gasto menor es:", minimo(lista))
        print("Tu gasto promedio es:", prom(lista))
        menu()
        opcion=int(input())

    elif(opcion < 1 or opcion > 6):
        print("elige opcion del 1 al 6")
        menu()
        opcion=int(input())