t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    res = []

    current = x
    while current > y:
        res.append(current)
        current -= 1

    current = y
    while current < x:
        res.append(current)
        current += 1

    print(len(res))
    print(*res)
