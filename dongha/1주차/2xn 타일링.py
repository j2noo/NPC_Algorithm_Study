import sys
def main():
    NUM = int(sys.stdin.readline().rstrip())
    n1 = 1
    n2 = 2
    tmp = -1
    if NUM <= 2:
        sys.stdout.write(str(NUM))
        return
    for _ in range(NUM-2):
        tmp = n1 + n2
        n1 = n2
        n2 = tmp
    sys.stdout.write(str(n2%10007))
    return
#####
main()
