import sys
import io
sys.stdin = open("input.txt", 'r')
'''
예시:
2 5 ?
....O
..O.O

1 | 2n | %4==3 | %4==1
1 : 입력값 그대로
2 : 전부 채워서
%4==3 : N1에서 O가 상하좌우로 퍼진 후 반전
%4==1 : N3에서 O가 상하좌우로 퍼진 후 반전
'''
def retReverse(char):
    return ".O"[char == '.']

def main():
    sio = io.StringIO()
    R, C, N = map(int, sys.stdin.readline().split())
    if N == 1:
        sys.stdout.write(sys.stdin.read()) # 1이면 들어온거 그대로 출력해준다.
        return
    elif N&1 == 0: #짝수면
        for _ in range(R):
            sio.write(''.join(['O' for _ in range(C)]))
            sio.write('\n')
        sys.stdout.write(sio.getvalue())
        return
    else:
        #상하좌우로 O가 퍼진, 반전된 N1 (반전하면 %4==3), (.를 퍼지게 하면 %4==1)
        board = []
        for _ in range(R):
            board.append(list(sys.stdin.readline().rstrip()))
        foo_set = set()
        for r in range(R):
            for c in range(C):
                if board[r][c] == 'O':
                    foo_set.add((r+1, c))
                    foo_set.add((r, c+1))
                    foo_set.add((r-1, c))
                    foo_set.add((r, c-1))
        for element in foo_set:
            r, c = element
            if r < R and r > -1 and c < C and c > -1:
                board[r][c] = 'O'
        if N%4==3:
            for row in board:
                sio.write(''.join([retReverse(i) for i in row]))
                sio.write('\n')
        else:
            foo_set2 = set()
            for r in range(R):
                for c in range(C):
                    if board[r][c] == '.':
                        foo_set2.add((r+1, c))
                        foo_set2.add((r, c+1))
                        foo_set2.add((r-1, c))
                        foo_set2.add((r, c-1))
            for element in foo_set2:
                r, c = element
                if r < R and r > -1 and c < C and c > -1:
                    board[r][c] = '.'
            for row in board:
                sio.write(''.join(row))
                sio.write('\n')
        sys.stdout.write(sio.getvalue())
#####
main()
