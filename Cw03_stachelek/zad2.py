def slownik(data_text):
    lenght = len(data_text)
    str(data_text)
    letters = []
    for i in data_text:
        letters.append(i)
    big_letters = str.upper(data_text)
    small_letters = str.lower(data_text)
    _dict_ = {'lenght': lenght, 'letters': letters, 'big_letters': big_letters, 'small_letters': small_letters}
    return _dict_


print(slownik("Damian"))
