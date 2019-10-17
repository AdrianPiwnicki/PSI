def parzysty(a_list, b_list):
    lista = []
    for i, val in enumerate(a_list):
        if i % 2 == 0:
            lista.append(val)
    for i, val in enumerate(b_list):
        if i % 2 != 0:
            lista.append(val)
    return lista

a1 = [1, 2, 3, 4, 5, 6, 7]
b1 = [11, 22, 33, 44, 55, 66, 77, 88]
print(parzysty(a1, b1))
