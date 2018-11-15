def extraerPares(lista):
    nueva=[]
    for dato in lista:
        if dato%2==0:
            nueva.append(dato)
    return nueva


def extraerMayoresPrevio(lista):
    nueva=[]
    for k in range(len(lista)-1):
        acumulado=lista[k]
        acumulado2=lista[k+1]
        k+=1

        if acumulado2>acumulado:
            nueva.append(acumulado2)
    return nueva


def intercambiarParejas(lista):
    nueva=[]

    for k in range(-1,len(lista),2):
        if k >= 1:
            nueva.append(lista[k])
            nueva.append(lista[k-1])

    largo=len(lista)
    if (largo%2)!= 0 :
        nueva.append(lista[len(lista)-1])


    return nueva



def intercambiarMM(lista):
    if len(lista)>=2:
        maximo= max(lista)
        minimo= min(lista)
        for k in range(len(lista)):
            if lista[k] == minimo:
                lista[k]=maximo
            elif lista[k] == maximo:
                lista[k]=minimo
        return lista
    return lista


def promediarCentro(lista):
    if len(lista)>2:
        lista.remove(max(lista))
        lista.remove(min(lista))
        acumulador=0
        for dato in lista:
            acumulador=dato+acumulador

        promedioCentro=acumulador//len(lista)
        return promedioCentro
    return 0


def calcularEstadisticas(lista):
    if len(lista)<=1:
        return 0,0

    acumulador=0
    for dato in lista:
        acumulador=dato+acumulador
    mean= acumulador/len(lista)

    acumulador2=0
    for dato in lista:
        suma=(dato-mean)**2
        acumulador2=acumulador2+suma
    deviation=((acumulador2)/(len(lista)-1))**(1/2)
    return(mean,deviation)


def calcularSuma(lista):

    acumulador=0
    borrar=[]

    for k in range(len(lista)-1):
        if lista[k]==13:
            if k==0 or k==(len(lista)-1):
                return 0
            borrar.append(lista[k])
            borrar.append(lista[k-1])
            borrar.append(lista[k+1])

    for dato in borrar:
        lista.remove(dato)

    for dato in lista:
        acumulador=acumulador+ dato
    return acumulador


def main():

    lista1=[1,2,3,4,5,6]
    a1= [1,2,3,4,5,6]
    a11= [1,2,3,4,5,6]
    lista2=[5,7,6]
    a2=[5,7,6]
    lista3=[]
    a3=[]
    lista4=[1,2,3,4,2,60,5,8]
    a4=[1,2,3,4,2,60,5,8]
    lista5=[5,4,3,2]
    a5=[5,4,3,2]
    lista6 =[5,9,1,8]
    a6 = [5, 9, 1, 8]
    lista7=[20,55,30,5,55,5]
    a7 = [20, 55, 30, 5, 55, 5]
    lista8=[5,8]
    a8 = [5, 8]
    lista9=[95,21,73,24,15,69,71,80,49,100,85]
    a9 = [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85]
    lista10=[13,49]
    a10 = [13, 49]
    print("""
    Problema 1, regresa una lista con los pares:
    De la lista %s, regresa %s
    De la lista %s, regresa %s
    De la lista %s, regresa %s
    """ %(a1,extraerPares(lista1),a2, extraerPares(lista2),a3,extraerPares(lista3)))
    print("""
    Problema 2, regresa una lista con los numeros que son mayores a otro previo:
    De la lista %s, regresa %s
    De la lista %s, regresa %s
    De la lista %s, regresa %s
    """ % (a4, extraerMayoresPrevio(lista4), a5, extraerMayoresPrevio(lista5), a3, extraerMayoresPrevio(lista3)))
    print("""    
    Problema 3, regresa una lista con las parejas de numeros intercambiadas:
    De la lista %s, regresa %s
    De la lista %s, regresa %s
    De la lista %s, regresa %s
    """ % (a1, intercambiarParejas(lista1), a2, intercambiarParejas(lista2), a3, intercambiarParejas(lista3)))
    print("""    
    Problema 4, intercambia el valor máximo y mínimo:
    De la lista %s, regresa %s
    De la lista %s, regresa %s
    De la lista %s, regresa %s
    """ % (a1, intercambiarMM(a11), a2, intercambiarMM(lista2), a3, intercambiarMM(lista3)))
    print("""    
    Problema 5, calcula el promedio centro:
    De la lista %s, regresa %s
    De la lista %s, regresa %s
    De la lista %s, regresa %s
    """ % (a6, promediarCentro(lista6), a7, promediarCentro(lista7), a8, promediarCentro(lista8)))
    print("""    
    Problema 6, calcula el promedio y la desviación:
    De la lista %s, regresa %s
    De la lista %s, regresa %s
    De la lista %s, regresa %s
    """ % (a1, calcularEstadisticas(lista1), a9, calcularEstadisticas(lista9), a3, calcularEstadisticas(lista3)))
    print("""    
    Extra, Realiza la suma de la lista, si hay un 13, no lo toma en cuenta ni alos numeros previo y siguiente:
    De la lista %s, regresa %s
    De la lista %s, regresa %s
    De la lista %s, regresa %s
    """ % (a1, calcularSuma(lista1), a10, calcularSuma(lista10), a3, calcularSuma(lista3)))


main()