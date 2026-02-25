t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    max_b = max(b)

    unique_a = set()
    for x in a:
        if x <= max_b:
            unique_a.add(x)

    if not unique_a:
        print("Bob")
        continue

    lcm = 1
    for x in unique_a:
        u, v = lcm, x
        while v > 0:
            u, v = v, u % v

        lcm = (lcm * x) // u

        if lcm > max_b:
            break

    divisible = [False] * (max_b + 1)
    for x in unique_a:
        if not divisible[x]:
            for step in range(x, max_b + 1, x):
                divisible[step] = True
    n_A = 0
    n_B = 0

    for y in b:
        if lcm <= max_b and y % lcm == 0:
            n_A += 1
        elif not divisible[y]:
            n_B += 1

    n_AB = m - n_A - n_B

    if n_A + (n_AB % 2) > n_B:
        print("Alice")
    else:
        print("Bob")