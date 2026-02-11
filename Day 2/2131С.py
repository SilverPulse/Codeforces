z = int(input())
for _ in range(z):
    n, k = map(int,input().split())

    s = list(map(int, input().split()))
    spisok = []
    for x in s:
        r = x % k
        spisok.append(min(r, k-r))

    t = list(map(int, input().split()))
    dr_spisok = []
    for x in t:
        r = x % k
        dr_spisok.append(min(r, k-r))
    spisok.sort()
    dr_spisok.sort()

    if spisok == dr_spisok:
        print("YES")
    else:
        print ("NO")