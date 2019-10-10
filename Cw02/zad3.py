#przykład 1
print("{0}+{0}={1}".format(2, 4))

#przykład2
print("Tekst napisany od lewej na 10 pól: {:>10}".format('tekst2'))

#przykład3
print("tekst do 7 pierwszych znaków: {:.7}".format("AdrianPiwnicki"))

#przykład4
print("Formaty liczbowe: {:d} {:f}".format(4, 4.32))

#przykład5
lista={'first': 'Adrian', 'last': 'Piwnicki'}
print("Pierwszy element listy: {first}, drugi element listy: {last}".format(**lista))
