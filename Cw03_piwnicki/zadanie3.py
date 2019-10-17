def usuwanie1(text, letter):
    new_text = text.replace(letter, '')
    return new_text


def usuwanie2(text2, letter2):
    new_text = ''
    for i in text2:
        if i != letter2:
            new_text += i
    return new_text


print(usuwanie1("AdrianPiwnicki", 'a'))
print(usuwanie1("AdrianPiwnicki", 'a'))
