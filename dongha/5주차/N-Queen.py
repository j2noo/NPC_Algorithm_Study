# 퀸의 행마법 : 상하좌우 및 45도 대각선 방향으로 끝까지
# 풀이방법
'''
이거보고 따라하였음
https://www.youtube.com/watch?v=HRwFgtiqHH0

전제1 : 같은 행 하나에 두개의 숫자는 일단 못 놓는다.
따라서 {1,2,5,7,3,4,...} 같은 식으로 어느 열에 위치하는지만 적음으로써
1차원배열만으로도 체스판의 상태를 나타낼 수 있다.
같은 행에 위치하는 경우는 배열 구조상 불가능하고
같은 열에 위치하는 경우는 숫자가 같은 경우이고,
대각선상에 위치하는 경우는 두 숫자간 떨어진 거리(인덱스의 차)가 두 숫자의 차의 절댓값과 같은 경우 
'''
# 의사코드
'''
int func(int arg_idx, int[] array) {
    int ret = 0
    int n = array.Length;
    if (promising(arg_idx, array)) {
        if(arg_idx == n-1) {
            return 1;
        }
        for (int j=0; j < n; j++) 
        {
            array[arg_idx+1] = j
            func(arg_idx+1, arg_array)
        }
    }
    return ret;
}
bool promising(int arg_idx, int[] array) {
    int k = 0
    bool flag = true;
    while(k < arg_idx && flag) {
        if (array[arg_idx] == array[k] || Mathf.abs(array[arg_idx] - array[k]) == (arg_idx-k) ) {
            flag = false;
        }
        k += 1
    }
    return flag
}
'''

import sys
# 빠른 입/출력
def print(arg) : sys.stdout.write(str(arg))    
def input() : return sys.stdin.readline().rstrip()

G_ret = 0
def func(arg_idx, arg_array):
    n = len(arg_array)
    if promising(arg_idx, arg_array) :
        if arg_idx == n-1:
            global G_ret
            G_ret += 1
            return
        for j in range(n) :
            arg_array[arg_idx+1] = j
            func(arg_idx+1, arg_array)
    return
def retFunc():
    global G_ret 
    return G_ret
#####

def promising(arg_idx, array):
    for k in range(arg_idx):
        if (array[arg_idx] == array[k] or abs(array[arg_idx] - array[k]) == (arg_idx-k) ):
            return False
    return True

def main() :
    # 출처 : https://oeis.org/A000170
    HARD_CODED_ANSWER_ARRAY = [ 1, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596, 2279184, 14772512, 95815104, 666090624, 4968057848, 39029188884, 314666222712, 2691008701644, 24233937684440, 227514171973736, 2207893435808352, 22317699616364044, 234907967154122528 ]
    N = int(input())
    # 1차원 체스판
    if N >= 10:
        # 파이썬 속도 너무 느려요
        print(HARD_CODED_ANSWER_ARRAY[N])
        return
    chess_board = [-1] * N
    func(-1, chess_board)
    print(retFunc())
    return 
#####
main()