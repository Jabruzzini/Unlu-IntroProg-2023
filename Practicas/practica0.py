n1=(int(input("Escriba un  numero : ")))
n2=(int(input("Escriba un segundo numero : ")))

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


def area_perimetro_rectangulo (base,altura):
    """
    Esta funcion toma dos parametros y devuelve su perimetro y su area 
    """
    perimetro=0
    area=0
    perimetro=base*2 + altura *2
    area= base*altura
    return perimetro , area

x=int(input("Base: "))
y=int(input("Altura: "))

a, b = area_perimetro_rectangulo(x,y)

print ( "El area de ",x,"y",y,"es igual a ",b)
print ( "El perimetro de ",x,"y",y,"es igual a ",a)
