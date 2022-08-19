# Proyecto TC1028 "Administrador de Finanzas"
## Contexto
Muchas personas no llevan buen control de sus finanzas y esto puede llevar a problemas como meterse en deudas, no poder pagar pagos importantes o gastar más de lo que ahorran. Los malos hábitos financieros tienen consecuencias severas sobre las personas ya que estos pueden facilmente arruinar sus vidas al destruir familias, empeorar creditos hipotecarios, pérdida de bienes, etc. Este programa también sirve para ayudar a los jóvenes adultos que van empezando a tener flujo de dinero constante y que no saben como manejarlo de una manera optimizada.

Los objetivos de este programa son:
  - control de ahorros, gastos e ingresos
  - mostrar tendencias del flujo de dinero del usuario
  - educación financiera

Los detalles clave de este programa son:
  - fecha de cada transacción
  - guardado de historial por un archivo
  - acceso al historial de cada tipo de transacción
  - graficación de las tendencias del usuario
  - posibilidad de hacer un budget personalizado

## Funcionalidad
El programa inicalmente contará con un menú donde mostrará todas las opciones y cada submenú ejectara cada una de las características previamente mencionadas. La primera vez que se ejecute el programa este pedirá su cantidad de ahorros inicial y desde ahi se desplegarán las opciones para introducir cambios (gastos, ingresos, etc.) Las demás opciones son acceso al historial (con fechas), acceso a la gráfica de tendencia diaria y opción para que el programa genere un budget recomendado para el usuario.

1) si es la primera vez que se accesa, el programa pide ahorros iniciales
2) pedir fecha actual (formato dd/mm/aaaa)
3) despelgar menu con las opciones:
    1. registrar cambio (cada cambio es guardado en un archivo con su respectiva fecha)
        - ingreso (ahorro+cantidad) 
        - gasto (ahorro-cantidad)
        - gasto recurrente (ahorro-cantidad-rec)
        
    2. acceso a historial (desplegar cambios guardados en el archivo)
    3. graficar tendencia diaria (comparación del dia en eje x y el cambio de dinero en el eje y)
    4. budget recomendado segun los ingresos (ejemplo: 60%-gastos escenciales, 30%-ahorros y 10%-lujos/diversión)
    5. salir
