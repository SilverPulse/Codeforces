n = int(input())
for _ in range(n):
    t = int(input())
    x_string = input()

    if t % 2 !=0:
        end = {'aa'}
    else:
        end = {'ab'}
    flag = True

    for x in x_string:
        nend = set ()
        for eend in end:
            if x == "a" or x == '?':
                if eend == "aa": nend.add('ab')
                if eend == "ab": nend.add('bb')
            if x == "b" or x == '?':
                if eend == 'bb': nend.add('ab')
                if eend == 'ab': nend.add('aa')
        end = nend

        if not end:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print('NO')