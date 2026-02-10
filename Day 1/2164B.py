a = int(input())

for _ in range(a):
    n = int(input())
    arr = list(map(int,input().split()))

    x = arr[0]
    y = arr[1]

    if y % x % 2 == 0:
        print(x,y)
    else:
        found = False
        for i in range(n):
            for j in range(i + 1, n):
                x = arr[i]
                y = arr[j]
                if (y % x) % 2 == 0:
                    print(x, y)
                    found = True
                    break
            if found:
                break
        if not found:
            print(-1)