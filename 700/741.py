N = int(input())

if N == 0:
    print(2)

else:
    ans = (10 + 9 * (N - 1)) % (10 ** 9 + 7)
    print(ans)