from datetime import datetime
import os


def budget(ingreso):
    esenciales = ingreso * 0.6
    guardar = ingreso * 0.3
    lujo = ingreso * 0.1
    print("esenciales: ", esenciales)
    print("guardar en ahorros: ", guardar)
    print("lujos y/o diversión: ", lujo)


def armar_fecha():
    fecha_correcta = False
    while (not fecha_correcta):
        try:
            fecha = input("Ingresa una fecha en el formato YYYY-MM-DD: ")
            datetime.strptime(fecha, '%Y-%m-%d')
            print("Fecha válida", fecha)
            fecha_correcta = True
        except ValueError:
            print("Fecha inválida")
    return fecha


def pedir_ingreso():
    print("Escribe tu ingreso: ")
    return float(input())


def pedir_gasto():
    print("Escribe tu gasto: ")
    return float(input())


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


def inicializacion():
    fe = armar_fecha()
    f = open("historial.txt", "w")
    print("Escribe tu cantidad de ahorros")
    ingreso = float(input())
    f.write(f"{fe} {ingreso} 0\n")
    f.close()


def regresar_fecha(linea_dia):
    return datetime.strptime(linea_dia[0], "%Y-%m-%d")


def obtener_datos():
    f = open("historial.txt", "r")
    datos_arr = []
    datos = f.read().split("\n")
    for linea in datos:
        if linea == "":
            continue
        linea_arr = linea.split(" ")
        linea_arr[1] = float(linea_arr[1])
        linea_arr[2] = float(linea_arr[2])
        datos_arr.append(linea_arr)

    datos_arr.sort(key=regresar_fecha)
    return datos_arr


def total_actual():
    datos = obtener_datos()
    total = 0
    for dia in datos:
        ingreso, gasto = dia[1], dia[2]
        total = total + ingreso - gasto
    return total


def menu():
    print(f"\nCantidad Actual = {total_actual()} ")
    print("MENU")
    print("1) Budget")
    print("2) Agregar Datos de Otro Dia")
    print("3) Diferencia del Dia Actual y Anterior")
    print("4) Historial")
    print("5) Datos de Gastos")
    print("6) Salir")


if os.path.exists("historial.txt") == False:
    inicializacion()

opcion = 1

while opcion != 6:

    menu()
    opcion = int(input())

    if (opcion == 1):
        ingreso = total_actual()
        if ingreso < 0:
            print("La cantidad no puede ser negativa")
        else:
            budget(ingreso)

    elif (opcion == 2):
        fe = armar_fecha()
        f = open("historial.txt", "a")
        ingreso = pedir_ingreso()
        gasto = pedir_gasto()
        f.write(f"{fe} {ingreso} {gasto}\n")
        f.close()

    elif (opcion == 3):
        datos = obtener_datos()
        numero_dias = len(datos)
        if numero_dias == 1:
            print("Solo hay un dia registrado")
            continue
        i = 0
        total = 0
        fecha = ""
        total_penultimo = 0
        fecha_penultimo = ""
        for dia in datos:
            fecha, ingreso, gasto = dia[0], dia[1], dia[2]
            total = total + ingreso - gasto
            if i == numero_dias - 2:
                total_penultimo = total
                fecha_penultimo = fecha
            i += 1
        diferencia = total - total_penultimo

        print(
            f"El dia {fecha_penultimo} tenias {total_penultimo} y hoy {fecha} tienes {total}, la diferencia es {diferencia}")

    elif (opcion == 4):
        datos = obtener_datos()
        for dia in datos:
            print(
                f"el dia {dia[0]} el ingreso fue de: {dia[1]} el gasto fue de: {dia[2]}")

    elif (opcion == 5):
        datos = obtener_datos()
        gastos = []
        for dia in datos:
            dato = dia[2]
            if dato != 0:
                gastos.append(dato)

        if len(gastos) == 0:
            gastos.append(0)
        print("Tu gasto mayor es:", maximo(gastos))
        print("Tu gasto menor es:", minimo(gastos))
        print("Tu gasto promedio es:", prom(gastos))

    elif (opcion < 1 or opcion > 6):
        print("elige opcion del 1 al 6")
