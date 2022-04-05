n, m = map(int, input().split())

pool = []
used = []

for i in range(1, n+1):
    pool.append(i)
    used.append(0)


chosen = []
# 조합
# visit check 안해도 됨 => 한 케이스에서 같은 숫자 나오면 안됨
# 넘길때 다음 숫자부터 넘김 => 순서가 달라도 같은 구성의 숫자면 같은 케이스로 보니까 1,2 했으면 2,1 할 필요 없으므로
def comb(pool, r):
    global chosen
    print("chosen", chosen)

    if len(chosen) == r:
        for i in chosen:
            print(i, end=' ')
        print()
        return

    for i in range(len(pool)):
        chosen.append(pool[i])

        comb(pool[i+1:], r) # perm와 다른점!
        chosen.pop()

comb(pool, m)