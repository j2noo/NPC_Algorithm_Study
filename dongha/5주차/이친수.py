#그냥 숫자 나열하니까 피보나치 나와서 피보나치로 풉니다...
import sys
def input() : return sys.stdin.readline().rstrip()
def print(arg) : 
    sys.stdout.write(str(arg))

def main():
    MEMOIZATION = [1] * 91
    for i in range(3, 91):
        MEMOIZATION[i] = MEMOIZATION[i-1] + MEMOIZATION[i-2]
    print(MEMOIZATION[int(input())])
    return
#####
main()