def przelicz(temperatura, temperature_type):
    if temperature_type == "F":
        print("Temperatura w Fahrenheit: ", temperatura*1.8000+32.00)
    elif temperature_type == "R":
        print("Temperatura w Rankine: ", temperatura*1.8000+491.67)
    elif temperature_type == "K":
        print("Temperatura w Kelvin: ", temperatura + 273.15)
    else:
        print("Błędny wartość.")


przelicz(-24, "F")
przelicz(-24, "R")
przelicz(-24, "K")
przelicz(-24, 1)
