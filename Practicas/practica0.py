# n1=(int(input("Escriba un  numero : ")))
# n2=(int(input("Escriba un segundo numero : ")))

# res=n1+n2

# print ("El resultado de sumar",n1,"+",n2,"  dio como resultado",res)

# ----------------------------------------------------------------------

# Variables que almacenan datos


# x = 47
# y = 68

# Variable que almacena la operacion entre las dos variables anteriores
# z = x+y

# Lo que se imprime en pantalla y ve el usuario

# print ("El resultado de sumar",x,"+",y,"  dio como resultado",z)


# """
#     FUNCIONES >>>  es importante recordar que :

#     1 ) Se debe documentar una funcion detallando
#         parametros de entrada y resultado de salida ( que devuelve )
#     2) Hacerlo de este forma usando triple comilla
#      3) es mas reutilizable si las funciones reciben los datos como parametros y no los escribimos dentro de la funcion
# """


# def multi_parametros(x, y):
#     """Esta funcion recibe dos parametros y como resultado da su multiplicacion"""
#     multiplicacion = x*y
#     return multiplicacion


# x = multi_parametros(10, 2)

# print("Multiplicacion de numeros: ", x)


# def area_perimetro_rectangulo (base,altura):
#     """
#     Esta funcion toma dos parametros y devuelve su perimetro y su area
#     """
#     perimetro=0
#     area=0
#     perimetro=base*2 + altura *2
#     area= base*altura
#     return perimetro , area

# x=int(input("Base: "))
# y=int(input("Altura: "))

# a, b = area_perimetro_rectangulo(x,y)

# print ( "El area de ",x,"y",y,"es igual a ",b)
# print ( "El perimetro de ",x,"y",y,"es igual a ",a)

# print("Convierte medidas inglesas a sistema metrico")

# millas = int(input("Cuántas millas?: "))
# pies = int(input("Y cuántos pies?: "))
# pulgadas = int(input("Y cuántas pulgadas?: "))

# metros = 1609.344 * millas + 0.3048 * pies + 0.0254 * pulgadas
# print("La longitud es de ", metros, " metros")


# x="""Aquí me pongo a cantar
# al compás de la vigüela,
# que al hombre que lo desvela
# una pena estraordinaria,
# como el ave solitaria
# con el cantar se consuela."""

# print (x)

# def add(a, b):
#     """
#     Retorna el resultado de a + b.
#     """
#     return a + b

# print(add.__doc__)
# help(add)

# a=15

# a+=25
# print (a)

# def hola_marta(x,y,z):
# """Esta funcion lo que hace es recibir 3 parametros y devolver  un saludo"""
#     return "Hola Marta! Estoy programando en Python."

# Esto es un comentario fuera de una funcion

# x="vos sabes hacerlo"
# y="te gustaria aprender"
# z=str("te enseño a hacerlo")

# w=hola_marta(x,y,z)


# print(w,x)
# print(w,y)
# print(w,z)

# def devolver_segundos(horas, minutos, segundos):

#     """Transforma en segundos una medida de tiempo expresada en
#     horas, minutos y segundos"""
#     return 3600 * horas + 60 * minutos + segundos

# def imprimir_segundos(horas, minutos, segundos):

#     """Imprime una medida de tiempo expresada en horas, minutos y
#     segundos, luego de transformarla en segundos"""
#     return(3600 * horas + 60 * minutos + segundos)


# segundos=imprimir_segundos(3,20,45)
# segundoS=imprimir_segundos(3,20,45)

# print(segundos)
# print(segundoS)


