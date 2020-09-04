def minimumBribes(q):
    bribes = 0
    swap = True
    last_ind = len(q) - 1
    status = 'Normal'

    for ind, v in enumerate(q):
        if v - (ind+1) > 2:
            status = 'Too chaotic'

    while swap:
        temp_q = q.copy()
        for j in range(last_ind):
            if q[j] > q[j+1]:
                temp = q[j+1]
                q[j+1] = q[j]
                q[j] = temp
                bribes += 1
        if temp_q == q:
            swap = False

    if status == 'Too chaotic':
        print(status)
    else:
        print(bribes)