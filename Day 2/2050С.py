t = int(input())

for _ in range(t):
    n = input()

    current_sum = 0
    count2 = 0
    count3 = 0

    for char in n:
        digit = int(char)
        current_sum += digit
        if digit == 2:
            count2 += 1
        elif digit == 3:
            count3 += 1

    found = False

    for i in range(min(count2, 10) + 1):
        for j in range(min(count3, 10) + 1):
            total = current_sum + (i * 2) + (j * 6)
            if total % 9 == 0:
                found = True
                break
        if found:
            break

    if found:
        print("YES")
    else:
        print("NO")