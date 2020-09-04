def rotLeft(a, d):
    new_list = []
    length = len(a)
    move_front = len(a) - d
    for j in range(move_front):
        new_list.append(a[j+d])
    for i in range(d):
        new_list.append(a[i])
    return new_list