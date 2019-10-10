lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Przed zmianą")
print(lista)

lista2 = lista[5:10]
for i in range(5, 10, 1):
    lista.pop()

print("Po zmianie")
print(lista)
print(lista2)
