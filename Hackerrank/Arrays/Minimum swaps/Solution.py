def minimumSwaps(arr):
    swap = 0
    swap_status = True
    while swap_status:
        init_swap = swap
        for i in range(len(arr)):
            if arr[i] != i+1:
                temp = arr[arr[i]-1]
                arr[arr[i] - 1] = arr[i]
                arr[i] = temp
                swap += 1

        if init_swap == swap:
            swap_status = False
#        print('swap:', swap)
    return swap

p = [1, 3, 5, 2, 4, 6, 7]
swap = minimumSwaps(p)
print(swap)