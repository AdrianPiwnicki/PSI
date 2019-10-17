def slowa(data_text):
    slownik = {}
    dlugosc = len(data_text)
    litery = []
    for i in data_text:
        litery.append(i)
    duze = data_text.upper()
    male = data_text.lower()
    slownik["length"] = dlugosc
    slownik["letters"] = litery
    slownik["big_letters"] = duze
    slownik["small_letters"] = male
    return slownik

print(slowa("DoGi"))
