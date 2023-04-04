# # 1. Defina con sus palabras cada uno de los siguientes conceptos:
# #     i. Programa.
# #     ii. Código fuente.
# #     iii. Algoritmo.
# #     iv. Instrucción.
# #     v. Dato.
# #     vi. Lenguaje de programación.
# #     vii. Paradigma de programación.

#     I) Un programa de computadora es una secuencia de instrucciones definidas paso a paso (como veremos
#     más adelante, un algoritmo) que le indican a una computadora cómo realizar una tarea dada. En la
#     computadora uno puede modificar un programa de acuerdo a la tarea que quiere realizar.

#     I.II)La diferencia entre un algoritmo y un programa, es que si bien ambos hacen referencia una serie de instrucciones, los algoritmos pueden estar escritos en código o en lenguaje natural, mientras que los programas sólo pueden estar escritos en lenguaje de programación

#     II)Es un archivo o conjunto de archivos, que contienen instrucciones concretas, escritas en un lenguaje de programación, que posteriormente compilan uno o varios programas.


#     III) Algoritmo es la especificación rigurosa de la secuencia de pasos (instrucciones) a realizar sobre un
#     autómata para alcanzar un resultado deseado en tiempo finito.

#     IV)Conjunto de datos (números y letras) que se insertan en una secuencia y que indican a un procesador la operación que debe ejecutar.

#     V) Secuencia de uno o más símbolos a los que se les da significado mediante actos específicos de interpretación


def print_alpha_nums (abc_list , num_list):
    for char in abc_list:
        for num in num_list:
            print ( char,"x", num)
    return 
print_alpha_nums(['a', 'b','c'] ,[1,2,3 ] )
