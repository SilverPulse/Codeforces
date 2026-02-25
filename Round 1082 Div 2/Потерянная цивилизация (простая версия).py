t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    parents = set()
    count = 0

    for x in a:
        if (x - 1) in parents:
            parents.remove(x - 1)
        else:
            count += 1
        parents.add(x)

    print(count)