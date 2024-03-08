def findgridpath(n, m):
    if n == 1 or m == 1:
        return 1
    else:
        return findgridpath(n, m-1) + findgridpath(n-1, m)

print(findgridpath(n=9, m=7))