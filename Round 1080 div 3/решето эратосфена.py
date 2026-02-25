n = input().strip()
if n:
    t = int(n)
    for _ in range(t):
        k = input().strip()
        while not k:
            k = input().strip()

        z = int(k)
        a = list(map(int, input().split()))

        if 67 in a:
            print("YES")
        else:
            print("NO")