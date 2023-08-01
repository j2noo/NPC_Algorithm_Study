import sys

def main():
    radix_array = [0] * 10001
    N = int(sys.stdin.readline())
    for _ in range(N):
        radix_array[int(sys.stdin.readline())] += 1
    count = N
    max_val = 0;
    for i in range(1, 10001):
        if i * count > max_val:
            max_val = i * count
        count -= radix_array[i]
    sys.stdout.write(str(max_val))
main()
