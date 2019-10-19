# Stwórz funkcję, która przelicza temperaturę w stopniach Celsjusza na Fahrenheit, Rankine, Kelvin.
# Typ konwersji powinien być przekazany w parametrze temperature_type i uwzględniać  błędne wartości.
def temperatura(stopnie, temperature_type):
    if temperature_type == "F":
        return (stopnie*1.8)+32
    elif temperature_type == "R":
        return (stopnie+273.15)*1.8
    elif temperature_type == "K":
        return stopnie+273.15
    else:
        return "Podałeś błędną wartość"

print("Temperatura z C -> F: "+str(temperatura(100, "F")))
print("Temperatura z C -> R: "+str(temperatura(100, "R")))
print("Temperatura z C -> F: "+str(temperatura(100, "K")))
print("Podanie błędnej wartości: "+str(temperatura(100, "C")))
