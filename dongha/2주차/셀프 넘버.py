import io
import sys

def d(n):
    return n + sum(map(int, ("%d" % n)))

def main():
    sio = io.StringIO()
    
    # idx [0 ~ 10000]
    self_number_table = [True] * 10001
    self_number_table[0] = False
    for i in range(1, 10001):
        if not self_number_table[i]:
            continue
        now = d(i)
        while now <= 10000:
            self_number_table[now] = False
            now = d(now)
    for i in range(1, 10001):
        if self_number_table[i]:
            sio.write("%d\n" % i)
            
    sys.stdout.write(sio.getvalue())

main()
