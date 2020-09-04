def jumpingOnClouds(c):
    jump = 0
    i = 0
    length = len(c)
    while i < length - 1:
        if i < length - 2 and c[i+2] == 0:
            i += 2
        elif i < length - 1 and c[i+1] == 0:
            i += 1
        jump += 1
    return jump