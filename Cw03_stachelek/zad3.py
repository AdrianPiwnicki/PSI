def delete_letters(letter, text):
    up_letter = str.upper(letter)
    low_letter = str.lower(letter)
    change_text = ""
    str(change_text)
    str(text)
    for i in text:
        if i != low_letter and i != up_letter:
            change_text += i
    return change_text


print(delete_letters("a", "Damian"))
