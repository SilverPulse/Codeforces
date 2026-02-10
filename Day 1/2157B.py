import sys

input = sys.stdin.read

def func():
    data = input().split()
    if not data:
        return
    t = int(data[0])
    point = 1

    for _ in range(t):
        n = int(data[point])
        x = abs(int(data[point + 1]))
        y = abs(int(data[point + 2]))
        s = data[point + 3]
        point += 4

        count8 = s.count('8')
        count4 = n - count8

        max_distance = max(x,y)

        max_target = (count8 * 2) + count4

        if n >= max_distance and (x + y) <= max_target:
            print("YES")
        else:
            print("NO")
func()
