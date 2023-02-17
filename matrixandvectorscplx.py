# Calculadora de Matrices y Vectores de Numeros Complejos
# Por Santiago Sánchez Monroy
# Febrero 2023.

import mathcplx
from tkinter import messagebox
import math

def sum_vex(a,b):
    if len(a)!=len(b):
        messagebox.showerror("ERROR!","Los vectores ingresados no tienen el mismo tamaño, por lo tanto no es posible operarlos")
    else:
        rsltVex = [[None for fila in range(1)] for column in range(len(a))]

        fila = len(a)
        
        for i in range(fila):
            rsltVex[i][0] = mathcplx.sumacplx(a[i][0],b[i][0])

        return rsltVex

def resta_Vex(a,b):
    if len(a)!=len(b):
        messagebox.showerror("ERROR!","Los vectores ingresados no tienen el mismo tamaño, por lo tanto no es posible operarlos")
    else:
        rsltVex = [[None for fila in range(1)] for column in range(len(a))]

        fila = len(a)
        
        for i in range(fila):
            rsltVex[i][0] = mathcplx.restacplx(a[i][0],b[i][0])

        return rsltVex

def inverseAditive_Vex(a):
    rsltVex = [[None for fila in range(1)] for column in range(len(a))]

    fila = len(a)
    
    for i in range(fila):
        rsltVex[i][0] = mathcplx.productocplx(a[i][0],[-1,0])

    return rsltVex

def productEscalar_Vex(a,b):
    fila = len(a)

    rta = [[None for column in range(len(a[0]))] for row in range(len(a))]

    for i in range(fila):
        rta[i][0] = mathcplx.productocplx(a[i][0],b)

    return rta

def sum_Matrix(a,b):
    fila = len(a)
    columna = len(a[0])
    
    if len(a)!=len(b) or len(a[0])!=len(b[0]):
        messagebox.showerror("ERROR!","Las matrices ingresadas no tienen el mismo tamaño, por lo tanto no es posible operarlas")
    else:
        rsltMatrix = [[None for column in range(columna)] for row in range(fila)]

        for i in range(fila):
            for j in range(columna):
                rsltMatrix[i][j] = mathcplx.sumacplx(a[i][j],b[i][j])

        return rsltMatrix

def inverseAditive_Matrix(a):
    fila = len(a)
    columna = len(a[0])
    
    for i in range(fila):
        for j in range(columna):
            a[i][j] = mathcplx.productocplx(a[i][j],[-1,0])

    return a

def productEscalar_Matrix(a,b):
    fila = len(a)
    columna = len(a[0])

    rta = [[None for column in range(columna)] for row in range(fila)]

    for i in range(fila):
        for j in range(columna):
            rta[i][j] = mathcplx.productocplx(a[i][j],b)

    return rta

def trans_Matrix_Vex(a):
    fila = len(a)
    columna = len(a[0])

    trans = [[None for column in range(fila)] for row in range(columna)]

    for i in range(fila):
        for j in range(columna):
            trans[j][i] = a[i][j]

    return trans

def conjug_Matrix_Vex(a):
    fila = len(a)
    columna = len(a[0])

    rta = [[None for j in range(columna)] for i in range(fila)]

    if columna>1:
        for i in range(fila):
            for j in range(columna):
                rta[i][j] = mathcplx.conjugado(a[i][j])

    else:
        for i in range(fila):
            rta[i][0] = mathcplx.conjugado(a[i][0])

    return rta

def adj_Matrix_Vex(a):
    conj = a[:]
    newConj = conjug_Matrix_Vex(conj)
    trans = trans_Matrix_Vex(newConj)

    return trans

def product_Matrix(a,b):
    filaA = len(a)
    filaB = len(b)
    columnaA = len(a[0])
    columnaB = len(b[0])

    if columnaA!=filaB:
        messagebox.showerror("ERROR!","Las matrices no pueden ser operadas, no son compatibles con los tamaños para realizar la multiplicación")
    else:
        rta = [[[0,0] for columna in range(columnaB)] for fila in range(filaA)]

        for i in range(filaA):
            for j in range(columnaB):
                for k in range(filaB):
                    rta[i][j] = mathcplx.sumacplx(rta[i][j],mathcplx.productocplx(a[i][k],b[k][j]))

        return rta

def accion_MatrixSobreVex(a,b):
    return product_Matrix(a,b)

def productIntern_Vex(a,b):
    newVex = adj_Matrix_Vex(a)

    return product_Matrix(newVex,b)

def normaVex(a):
    fila = len(a)
    columna = len(a[0])

    rta = 0

    for i in range(fila):
        for j in range(columna):
            rta += a[i][j][0]**2+a[i][j][1]**2

    return math.sqrt(rta)

def distanceVex(a,b):
    crestacplx = resta_Vex(a,b)

    norma = normaVex(crestacplx)

    return norma

def matrixUnit(a):
    daga = adj_Matrix_Vex(a)
    operacion = product_Matrix(a,daga)

    fila = len(a)
    columna = len(a[0])

    matrixIdentity = [[[1,0] if x==y else [0,0] for y in range(columna)] for x in range(fila)]

    for i in range(fila):
        for j in range(columna):
            operacion[i][j] = [round(operacion[i][j][0]),round(operacion[i][j][1])]

    if operacion==matrixIdentity:
        return True
    else:
        return False

def matrixHermitiana(a):
    daga = adj_Matrix_Vex(a)

    if daga==a:
        return True
    else:
        return False

def productTensor_Matrix_Vex(a,b):
    filaM1,filaM2 = len(a),len(b)
    columnaM1,columnaM2 = len(a[0]),len(b[0])

    newMatrix = [[[0,0] for column in range(columnaM1*columnaM2)] for row in range(filaM1*filaM2)]

    for i in range(len(newMatrix)):
        for j in range(len(newMatrix[0])):
            newMatrix[i][j] = mathcplx.productocplx(a[i//filaM2][j//columnaM2],b[i%filaM2][j%columnaM2])


    return newMatrix

