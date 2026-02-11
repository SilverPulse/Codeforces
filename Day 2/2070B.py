t = int(input())

for _ in range(t):
    n, x, k = map(int,input().split())
    s = input()

    first_touch = -1
    curr = x
    for i in range(n):
        if s[i] == 'L': curr -= 1
        else: curr += 1
        if curr == 0:
            first_touch = i + 1
            break
    if first_touch == -1 or first_touch > k:
        print(0)
        continue
    count = 1
    time_left = k - first_touch

    loop_time = -1
    curr = 0
    for i in range(n):
        if s[i] == 'L':
            curr -= 1
        else:
            curr += 1
        if curr == 0:
            loop_time = i + 1
            break
    if loop_time != -1:
        count += (time_left // loop_time)
    print(count)


