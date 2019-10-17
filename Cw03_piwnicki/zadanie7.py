def od_tylu(text):
    dl = len(text)-1
    new_text = ''
    for i in range(dl, -1, -1):
        new_text += text[i]
    return new_text

print(od_tylu("AdrianPiwnicki"))
