def countingValleys(n, s):
    path = 0
    prev_path = 0
    if s[0] == 'U':
        status = 'Uphill'
    elif s[0] == 'D':
        status = 'Downhill'
    valley = 0
    for step in s:
        if step == 'U':
            path += 1
        elif step == 'D':
            path -= 1
        if path == -1 and prev_path == 0:
            status = 'Downhill'
        if path == 1 and prev_path == 0:
            status = 'Uphill'
        if path == 0 and prev_path == -1 and status == 'Downhill':
            valley += 1
        prev_path = path
    return valley