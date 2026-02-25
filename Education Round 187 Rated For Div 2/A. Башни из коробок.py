k = int(input())
for _ in range(k):
    n, m, d = map(int,input().split())
    m_sv  = d // m
    v_ba = m_sv + 1
    ans = (n+v_ba-1) // v_ba
    print(ans)