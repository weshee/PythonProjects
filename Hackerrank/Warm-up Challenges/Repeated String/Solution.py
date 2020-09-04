def repeatedString(s, n):
    length = len(s)
    floor = n // length
    remainder = n % length
    count_a = (s.count('a') * (floor)) + s[:remainder].count('a')
    return count_a