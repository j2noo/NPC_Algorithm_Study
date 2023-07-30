n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 123)
m = int(input())

for i in range(m):
    gender, num = map(int, input().split())

    # 남학생
    if gender == 1:
        for i in range(1, n + 1):
            if i % num == 0:
                arr[i] = 1 if (arr[i] == 0) else 0

    elif gender == 2:
        start, end = num, num
        while 1:
            if start - 1 == 0 or end + 1 > n:
                break
            if arr[start - 1] != arr[end + 1]:
                break
            start -= 1
            end += 1
        for i in range(start, end + 1):
            arr[i] = 1 if (arr[i] == 0) else 0


for i in range(1, n + 1):
    if i == 21 or i == 41 or i == 61 or i == 81:
        print()
    print(arr[i], end=" ")
