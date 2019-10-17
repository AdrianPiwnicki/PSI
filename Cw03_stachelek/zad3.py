print("Podaj litere: ")
letter = input()

up_letter = str.upper(letter)
low_letter = str.lower(letter)

print("Podaj teks: ")
text = input()
str(text)
wynik = ""
str(wynik)

for i in text:
    if i != low_letter and i != up_letter:
        wynik += i

print(wynik)
