def d(num):
    sum = num
    li = list(str(num))
    for i in li:
        sum += int(i)
    return sum


isSelfNumber = [True] * 20000
for i in range(10000):
    isSelfNumber[d(i)] = False

for i in range(10000):
    if isSelfNumber[i] == True:
        print(i)