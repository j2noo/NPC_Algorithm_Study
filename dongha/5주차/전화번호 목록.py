import sys

def input(): return sys.stdin.readline().rstrip()
def print(arg) : sys.stdout.write(str(arg)); sys.stdout.write('\n')

def isFirstInSecond(arg_first, arg_second):
    if len(arg_first) > len(arg_second):
        return False
    for i in range(len(arg_first)):
        if arg_first[i] != arg_second[i]:
            return False
    return True

def main_sub() :
    str_list = []
    N = int(input())
    for _ in range(N):
        str_list.append(input())
    str_list.sort()
    for i in range(len(str_list)):
        for k in range(i+1, len(str_list)):
            if isFirstInSecond(str_list[i], str_list[k]):
                return "NO"
            else:
                break
    return "YES"
            

def main():
    T = int(input())
    for _ in range(T):
        print(main_sub())
main()