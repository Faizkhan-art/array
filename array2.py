arr=[1,8,9,78,25]
def diagonalDifference(arr):
    n = len(arr)

    left = 0
    right = 0

    for i in range(n):
        left = left + arr[i][i]
        right = right + arr[i][n - 1 - i]

    return abs(left - right)