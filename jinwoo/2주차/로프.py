N = int(input())
arr=[]
for i in range(N):
    arr.append(int(input()))

arr.sort()

sum = -1

for i in range(N):
    sum= max(sum,arr[i]*(N-i))
    
print(sum)
