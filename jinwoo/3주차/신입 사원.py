from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    N = int(stdin.readline())
    arr = []
    for _ in range(N):
        data = list(map(int, stdin.readline().split()))
        arr.append(data)

    arr.sort()

    min = 0x3F3F3F3F
    cnt = 0
    for data in arr:
        if data[1] < min:
            min = data[1]
            cnt += 1

    print(cnt)
