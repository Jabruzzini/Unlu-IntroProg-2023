""" DECISIONES  CONDICIONALES

1)DATO BOOLEANO
2)OPERADOR RELACIONAL
3)OPERADORES LOGICOS
4)ESTRUCTURA CONDICIONAL SIMPLE


1) tipo de dato primitivo, ya esta implementado
    Es de tipo Verdadero o Falsa ( True or False )
    Es Case-Sensitive ( escribir con la T y la F mayuscula)
    Estos valores no son Literales, no llevan comillas, son primitivos. 

    Sirve para expresar si un predicado es verdadera o falsa
    Ayuda para tomar decisiones

    
2)  Operadores relacionales : Devuelven un valor Booleano  
    como resultado

    Ejemplos:

    10 < 20 
    n1 >= n2
    cadena == "Hola" ( ATENCION ESTO NO ES VARIABLE ES COMPARACION )

    len(nombre1) != len(nombre2)

    se puede aplicar a texto , numeros 

3) Operaciones logicas basicas 
    Conjuncion, disyuncion , negacion .  
    
    se aplican entre booleanos y como resultado dan
    UN NUEVO BOOLEANO


    CONJUNCION    AND
    DISYUNCION    OR
    NEGACION      NOT

    TOMA DOS VALORES BOOLEANOS Y RETORNA 

    AND : TRUE SI Y SOLO SI LOS DOS SON VERDADEROS
    OR  : TRUE SI AL MENOS UNO DE LOS DOS ES VERDADERO
    NOT : RETORNA EL VALOR INVERSO, SI ES TRUERETORNA      
        FALSE (INVIERTE EL VALOR)

    
    
    """

def valor_bool (x,y):
    if x>y:
        return True
    else:
        return False
    

print (valor_bool(23,20))

def valor_mayor(x,y):
    """Recibe dos parametros y retorna verdadero si el primer numero es mayor, si no , false"""
    return x>y

print (type(valor_mayor(10,5)))
print (valor_mayor(10,5))


""" Estructa CONDICIONAL SIMPLE DE PYTHON """

# if (condicion):
    # [codigo a ejecutar si y solo si la condicion es verdadera]


    