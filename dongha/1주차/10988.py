import sys
import io
sio = io.StringIO()
#sys.stdin = open("input.txt", "r")
input_str = sys.stdin.readline()
length = len(input_str) - 1
finding_num = (len(input_str) - 1) // 2
for i in range(finding_num):
    if input_str[i] != input_str[length - 1 - i]:
        sio.write("0")
        break
else:
    sio.write("1")
sys.stdout.write(sio.getvalue())
#...혹은 그냥 (lambda x : print(int(len(x)<=1 or x == x[::-1])))(input())
