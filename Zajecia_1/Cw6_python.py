lista = list(range(10))

new_list = lista[5:]
lista = lista[:5]

print(new_list,lista)


lista = lista + new_list
lista.insert(0,0)

print(lista)

copy_lista = lista
lista.sort(reverse=True)

print(lista)