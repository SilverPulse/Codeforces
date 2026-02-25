t_in = input().strip()
if t_in:
    t = int(t_in)
    for _ in range (t):
        koi = input().strip()
        while not koi:
            koi = input().strip()
        l = int(koi)

        a = list(map(int, input().split()))

        otv = 0
        y = 0
        while y < l - 1:
            if a[y] == a[y+1] or a[y] + a[y+1] == 7:
                otv+=1
                y+=2
            else:
                y+=1
        print(otv)
