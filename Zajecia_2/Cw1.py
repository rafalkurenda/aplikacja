
lista1 = [1,2,3,4,5,6,7,8,9,10]
lista2 = [1,2,3,4,5,6,7,8,9,10]

def func(lista1,lista2):
    lista_temp = []
    for i in lista1:
        if i%2==0:
            lista_temp.append(i)
    for i in lista2:
        if i%2==1:
            lista_temp.append(i)
    print(lista_temp)


func(lista1,lista2)