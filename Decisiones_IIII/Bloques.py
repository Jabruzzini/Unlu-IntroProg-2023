

# Sueldo basico USD 800

# Adicional 
# Sec_1 = +120 + 10% antiguedad < 5 años o 20% <= 5 años

# Sec_2 = +250 sin antiguedad


# basico = int(800)
# adicional1 = 120 
# adicional2 = 250
# nombre = str(input ("Ingrese su nombre: "))
# sector = int(input("Ingrese su numero de sector : \t 1 o 2 \n"))
# antiguedad = int(input("Ingrese su antiguedad: "))

# def calculo_sueldo ():

#     if (sector == 1 ) and (antiguedad < 5): 
#         return "Usted pertenece al sector 1, su sueldo incluye basico + U$D 120 + 10%", (basico + adicional1) * 1.10
#     elif (sector == 1 ) and (antiguedad >= 5):
#         return "Usted pertenece al sector 1, su sueldo incluye basico + U$D 120 + 20%", (basico + adicional1) * 1.20
#     else:
#         return "Usted pertenece al sector 2, su sueldo incluye basico + U$D 250", (basico + adicional2)
    
# print (calculo_sueldo())
    


# nombre_empleado= input ("Ingrese nombre de empleado: ")
# sector= int(input("Ingrese sector al que pertenece: "))
# antiguedad= int(input("Ingrese antiguedad: "))

# sueldo= 800

# if sector == 1 and antiguedad < 5 : 
#     recibo= int((sueldo+120)*1.10)
#     print (f'Hola {nombre_empleado}, su sueldo es {recibo}')
# elif sector==1: 
#     recibo= int((sueldo+120)*1.20)
#     print (f'Hola {nombre_empleado}, su sueldo es {recibo}')
# elif sector == 2:
#     recibo=int((sueldo+250))
#     print (f'Hola {nombre_empleado}, su sueldo es {recibo}')
# else: 
#     print ("Sector erroneo")

    
def potenciacion(base, exponente):
    
    resultado=pow(base, exponente)
    return f"La potencia de {base} ^ {exponente} es igual a: {resultado}"

print(potenciacion(10,5))
