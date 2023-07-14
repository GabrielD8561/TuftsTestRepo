def uniquePaths(m: int, n: int):
    if(m == 1 or n == 1):
        return 1
    return uniquePaths(m-1, n) + uniquePaths(m, n-1)

print(uniquePaths(3, 7))