def awry(text):
    new_text = ""
    str(new_text)
    for i in range(1, len(text)):
        new_text += text[-i]
    new_text += text[0]
    print(new_text)


print("koteł")
awry("koteł")
