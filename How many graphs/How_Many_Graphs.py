N = int(input())
S = 0
n = (N * (N - 1)) // 2

for i in range(N+1) :

    res = 1
    if (i > n - i):
        i = n - i

    for j in range(i):
        res *= (n - j)
        res //= (j + 1)


    S = S + res


print(S)
