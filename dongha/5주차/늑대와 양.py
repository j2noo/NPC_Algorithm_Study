import sys
import io

def input() : return sys.stdin.readline().rstrip()
def print(arg) : sys.stdout.write(str(arg))

def main():
    sio = io.StringIO()
    input() # 처음 입력 버리기
    
    # 목장 맵 받아오기
    ranch = sys.stdin.read().split()

    for row in range(len(ranch)):
        for col in range(len(ranch[0])):
            if ranch[row][col] == '.':
                sio.write('D')
                continue
            elif ranch[row][col] == 'W':
                possibility_of_eaten = \
                    (row>0 and ranch[row-1][col] == 'S') \
                    or (row<len(ranch)-1 and ranch[row+1][col] == 'S') \
                    or (col>0 and ranch[row][col-1] == 'S') \
                    or (col<len(ranch[0])-1 and ranch[row][col+1] == 'S')
                if possibility_of_eaten:
                    print(0)
                    return
            sio.write(ranch[row][col])
        sio.write('\n')
    print('1\n')
    print(sio.getvalue())
    return
#####
main()
                    
