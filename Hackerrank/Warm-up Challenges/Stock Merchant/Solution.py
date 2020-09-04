def sockMerchant(n, ar):
    unique_ar = []
    total = 0
    for i in ar:
        if i not in unique_ar:
            unique_ar.append(i)
    for j in range(len(unique_ar)):
        items = ar.count(unique_ar[j])
        total += items//2
    return int(total)