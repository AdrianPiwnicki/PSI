def wczytaj_liste(lista):
    while True:
        wejscie = input()
        if wejscie == 'stop':
            break
        lista.append(int(wejscie))


a_list = []
print('Podaj liczby całkowite, które chcesz umieścić w A_LISCIE.')
print('Wpisz stop aby zakończyć')
wczytaj_liste(a_list)

b_list = []
print('Podaj liczby całkowite, które chcesz umieścić w B_LISCIE.')
print('Wpisz stop aby zakończyć')
wczytaj_liste(b_list)

print(a_list, b_list)

a = len(a_list)
b = len(b_list)
wyn_list = []

if a > b:
    c = a
else:
    c = b

for i in range(0, c, 2):
    if i < a:
        wyn_list.append(int(a_list[i]))
    if (i+1) < b:
        wyn_list.append(int(b_list[i + 1]))

print(wyn_list)
