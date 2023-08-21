t = int(input())
for _ in range(t):
    arr = []
    n = int(input())
    for i in range(n):
        arr.append(input())
    arr.sort()

    flag = 0
    for i in range(n - 1):
        before = arr[i]
        after = arr[i + 1][: len(before)]
        if before == after:
            print("NO")
            flag = 1
            break
    if flag == 0:
        print("YES")
