# Proyecto TC1028 "Administrador de Finanzas"
## Contexto
Muchas personas no llevan buen control de sus finanzas y esto puede llevar a problemas como meterse en deudas, no poder pagar pagos importantes o gastar más de lo que ahorran. Los malos hábitos financieros tienen consecuencias severas sobre las personas ya que estos pueden fácilmente arruinar sus vidas al destruir familias, empeorar créditos hipotecarios, pérdida de bienes, etc. Este programa también sirve para ayudar a los jóvenes adultos que van empezando a tener flujo de dinero constante y que no saben cómo manejarlo de una manera optimizada.

Los objetivos de este programa son:
  - control de ahorros, gastos e ingresos
  - mostrar tendencias del flujo de dinero del usuario
  - educación financiera

Los detalles clave de este programa son:
  - fecha de cada transacción
  - guardado de historial por un archivo
  - acceso al historial de cada tipo de transacción
  - mostrar el cambio diario de dinero del usuario
  - posibilidad de hacer un budget

## Funcionalidad
El programa inicialmente contará con un menú donde mostrará todas las opciones y cada submenú ejecutará cada una de las características previamente mencionadas. La primera vez que se ejecute el programa este pedirá su cantidad de ahorros inicial y desde ahí se desplegarán las opciones para introducir cambios (gastos, ingresos, etc.) Las demás opciones son acceso al historial (con fechas), cambio diario de los ahorros y opción para que el programa genere un budget recomendado para el usuario.

1) si es la primera vez que se accede, el programa pide ahorros iniciales
2) obtener fecha actual (formato dd/mm/aaaa)
3) desplegar menú con las opciones:
    1. registrar cambio (cada cambio es guardado en un archivo con su respectiva fecha)
        - ingreso (ahorro+cantidad)
           + `pedir cantidad --> obtener fecha --> guardar en el archivo`
        - gasto (ahorro-cantidad)
           + `pedir cantidad --> obtener fecha --> guardar en el archivo`
        
    2. acceso a historial (desplegar cambios guardados en el archivo)
       + `leer archivo --> crear una tabla --> desplegar tabla con datos`
    4. mostrar el cambio del día a día
       + `valor actual = valor ayer + ingresos - gastos --> cambio = valor actual - valor ayer`
    6. budget recomendado según el ingresos (ejemplo: 60%-gastos esenciales, 30%-ahorros y 10%-lujos/diversión)
       + `esenciales = ingreso*0.6 | ahorros = ingreso*0.3 | lujos = ingreso*0.1`
    8. salir

## Instrucciones
Descargar el archivo y correr en terminal con:
 `python proyecto.py`
 Responder a las preguntas que aparecen, el programa aún no incluye archivos ni historial.
