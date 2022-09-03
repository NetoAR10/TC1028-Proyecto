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

def armar_fecha(dia, mes, año):
    fecha = f"{dia}/{mes}/{año}" #este es un fstring que incorpora variables
    return fecha
    

print("MENU")
print("1) budget")
print("2) cambio del dia")
print("3) introcuir fecha")
print("4) historial (aun no sirve)")

opcion=int(input())
if(opcion == 1):
    print("Introduce tu ingreso para armar tu budget")
    ingreso = float(input())
    budget(ingreso)

elif(opcion == 2):
    print("escribe la cantidad ahorrada: ")
    ahorro_1 = float(input())
    print("escribe tu ingreso: ")
    ingreso = float(input())
    print("escribe tus gastos: ")
    gasto = float(input())
    print("el cambio del dia fue: ")
    print(cambio_dia(ingreso, ahorro_1, gasto))

elif(opcion == 3):
    print("Escribe la fecha de hoy en formato dd/mm/aaaa uno por uno")
    print("dia: ")
    dia = int(input())
    print("mes: ")
    mes = int(input())
    print("año: ")
    año = int(input()) 
    print(armar_fecha(dia, mes, año))

elif(opcion == 4):
    print("el historial aun no existe")

elif(opcion<1 or opcion>4):
    print("elige opcion del 1 al 4")