t = int(input())
for _ in range(t):
    x,y = map(int, input().split())
    if (x+y) % 3 == 0 and (x+y) // 3 >= 0 and (abs(y) <= (x + y) // 3) :
        print("YES")
    else:
        print('NO')

