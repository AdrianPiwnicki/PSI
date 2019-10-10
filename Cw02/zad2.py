imie = "Damian"
nazwisko = "Stachelek"

tekst = "Jest tekstem stosowanym jako przykładowy wypełniacz " \
        "w przemyśle poligraficznym. Został po raz pierwszy użyty" \
        " w XV w. przez nieznanego drukarza do wypełnienia tekstem " \
        "próbnej książki. Pięć wieków później zaczął być używany " \
        "przemyśle elektronicznym."

print(tekst)

liczba_1 = (tekst.count(imie[2]))
liczba_2 = (tekst.count(nazwisko[3]))

print("W tekscie jest %i liter %s ... oraz %i liter %s ..." % (liczba_1, imie[2], liczba_2, nazwisko[3]))
