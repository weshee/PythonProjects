def hourglassSum(arr):
    i = 0
    j = 0
    hgs_list = []
    for i in range(4):
        for j in range(4):
            sum_glass = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            hgs_list.append(sum_glass)
    return max(hgs_list)