import sys
import io
#sys.stdin = open("input.txt", "r")

def toggle(num):
    return num^1 #xor연산자를 사용하여 1이면 0, 0이면 1 반환

def female(num, arg_list):
    idx1 = num+1 # 더하기
    idx2 = num-1 # 빼기
    # 받은 번호는 무조건 토글된다. + 아래 while문에서 문제 안생기게 조치용
    arg_list[num] = toggle(arg_list[num])
    while idx1 < len(arg_list) and idx2 > 0:
        if(arg_list[idx1] == arg_list[idx2]):
            arg_list[idx1] = toggle(arg_list[idx1])
            arg_list[idx2] = toggle(arg_list[idx2])
        else:
            break
        idx1 += 1; idx2 -= 1;

def male(num, arg_list):
    idx = num
    while idx < len(arg_list):
        arg_list[idx] = toggle(arg_list[idx])
        idx += num 

#####
def main():
    sio = io.StringIO()
    sys.stdin.readline() #첫번째 입력 무시
    # 두번째 입력을 배열로(0번 인덱스는 더미용)
    switch_array = [9] + list(map(int, sys.stdin.readline().split()))
    REPEAT = int(sys.stdin.readline())
    func_table = [None, male, female]
    for _ in range(REPEAT):
        func_idx, num = map(int, sys.stdin.readline().split())
        func_table[func_idx](num, switch_array)
    for i in range(1, len(switch_array)):
        sio.write(str(switch_array[i]))
        sio.write('\n')
    sys.stdout.write(sio.getvalue())
    #더미용 인덱스 제거
######
main()
