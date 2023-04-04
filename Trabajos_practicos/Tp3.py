# Cree un script que, sabiendo cuántos pesos argentinos    tiene una persona
# ahorrada en su cuenta (almacenando ese monto en una variable), muestre
# en pantalla los montos convertidos en dólares (U$1 = $80.5), reales ($R1 =
# $14.1), y euros (€1 = $69.5). La salida del programa debe tener el siguiente
# formato: 


saldo=float(input("Ingrese un monto en pesos : "))

def conversion (x):
    x=saldo
    usd="{:.2f}".format(x/80.5)
    reales="{:.2f}".format(x/14.1)
    euros= "{:.2f}".format(x/69.5)

    return f'Usted tiene {saldo} pesos argentinos , los cuales se convierten en: \n {usd} dolares \n {reales} reales \n {euros} euros'

print (conversion(saldo))