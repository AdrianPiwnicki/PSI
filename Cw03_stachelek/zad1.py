def zmiana(a_list, b_list):
    a = len(a_list)
    b = len(b_list)
    wyn_list = []
    if a > b:
        c = a
    else:
        c = b
    for i in range(0, c, 2):
        if i < a:
            wyn_list.append(int(a_list[i]))
        if (i+1) < b:
            wyn_list.append(int(b_list[i + 1]))
    print(wyn_list)


print([1, 2, 3, 4, 5], [10, 11, 12, 13, 14])
zmiana([1, 2, 3, 4, 5], [10, 11, 12, 13, 14])
