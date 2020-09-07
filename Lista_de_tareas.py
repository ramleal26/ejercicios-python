from datetime import datetime

meses = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre",
}

dias = {
    0: "Domingo",
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado",
}

ahora = datetime.now()
numero_mes = ahora.month
# A entero para quitar los ceros a la izquierda en caso de que existan
numero_dia = int(ahora.strftime("%w"))
# Leer diccionario
dia = dias.get(numero_dia)
mes = meses.get(numero_mes)
# Formatear
fecha = "{}, {} de {} del {}".format(dia, ahora.day, mes, ahora.year)
#Imprimir
print(fecha)
