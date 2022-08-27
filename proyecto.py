print("Escribe la cantidad de dinero ahorrada: ")
ahorro1=float(input())

print("Escribe la fecha de hoy en formato dd/mm/aaaa uno por uno")
dia=input()
mes=input()
año=input()
fecha=f"{dia}/{mes}/{año}"

print(fecha)

print("Si hay ingresos, escribe aqui la cantidad: ")
ingreso=float(input())

print("Si hay gastos, escribe aqui la cantidad: ")
gasto=float(input())

ahorro2=ahorro1+ingreso-gasto
cambio=ahorro2-ahorro1
escenciales=ingreso*0.6
guardar=ingreso*0.3
lujo=ingreso*0.1

print(f"Tu dinero actual el dia de hoy es:  ${ahorro2:.2f}")
print(f"El cambio que hubo del dia de ayer al dia de hoy es de:  ${cambio:.2f}")
print("La distribucion recomendad de tus ingresos es la siguinete")
print(f"Escenciales = ${escenciales:.2f}")
print(f"Guardar en ahorros = ${guardar:.2f}")
print(f"Lujos y/o diversion = ${lujo:.2f}")

