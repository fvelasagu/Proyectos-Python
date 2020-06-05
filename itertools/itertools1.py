from itertools import product

matriz = [
    ["A","B","C"],
    [4,10,2,8],
    ["X","Z"]
]

combinaciones = None
# ENCONTRAR TODAS LAS PROPUESTAS POSIBLES
for fila in matriz:                             # RECORRER MATRIZ
    if(combinaciones is None):                      # SI RECIÉN COMIENZA
        combinaciones = fila                            # COMBINACIONES SERÁ VALOR DE LISTA
    else:                                           # DESDE LA SIGUIENTE FILA
        combinaciones = product(combinaciones,fila)     # OBTENER PRODUCTO ENTRE COMBINACIONES ANTERIORES Y FILA ACTUAL
        
# FUNCIÓN RECURSIVA PARA TRANSFORMAR DE TUPLA A LISTA -> ((x1,x2),x3) en [x1,x2,x3]
def transformar_lista(dato):
    d = []
    if(type(dato) is tuple):                # SI ES UNA TUPLA
        for i in dato:                          # RECORRER LA TUPLA
            d.extend(transformar_lista(i))      # EL DATO QUE RETORNE EXTENDER LA LISTA
    else:                                   # SI NO ES TUPLA
        d.append(dato)                          # AGREGAR EL DATO A LISTA
    return d

# RECORRER COMBINACIONES DE TUPLAS Y TRANSFORMARLAS A LISTA
for combinacion in combinaciones:
    print(transformar_lista(combinacion))       # TRANSFORMAR ((x1,x2),x3) -> [x1,x2,x3]