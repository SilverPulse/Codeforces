t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    z = True
    for i in range(n):
        val = a[i]
        pos = i + 1

        while val % 2 == 0:
            val //= 2
        t_pos=pos
        while t_pos % 2 == 0:
            t_pos //= 2
        if val != t_pos:
            z = False
            break
    if z:
        print("YES")
    else:
        print("NO")
