t = int(input())
for _ in range(t):
    s = input().strip()
    if sum(int(c) for c in s) <= 9:
        print(0)
        continue

    first_digit = int(s[0])

    other_digits = []
    for char in s[1:]:
        other_digits.append(int(char))
    other_digits.sort()

    a = 9 - first_digit
    saved_a = 1
    for d in other_digits:
        if a >= d:
            a -= d
            saved_a += 1
        else:
            break

    b = 8
    saved_b = 0
    for d in other_digits:
        if b >= d:
            b -= d
            saved_b += 1
        else:
            break

    best_saved = max(saved_a, saved_b)

    ans = len(s) - best_saved
    print(ans)