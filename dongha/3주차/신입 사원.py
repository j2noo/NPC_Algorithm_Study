import sys
import io

#sys.stdin = open("input.txt", 'r')

def input() : return sys.stdin.readline().rstrip()

def main():
    sio = io.StringIO()
    REPEAT = int(input())
    for _ in range(REPEAT):
        tuple_list = []
        INNER_REPEAT = int(input())
        for _ in range(INNER_REPEAT):
            tuple_element = tuple(map(int, input().split()))
            tuple_list.append(tuple_element)
        tuple_list.sort() # 첫번째 요소 기준으로 정렬

        # 뽑을 수 있는 숫자
        # 정렬된 리스트의 첫번째는 무조건 선발된다.
        amount = 0
        # 면접 성적 순위.
        # 이거보다 숫자가 낮아야(==순위가 높아야) 선발된다.
        # 만일 새로운 낮은 숫자가 등장하면 기준이 바뀐다.
        second_rank_minimum = 9999999 # 초기화용 높은 숫자
        for i in range(len(tuple_list)):
            second_now = tuple_list[i][1]
            if second_rank_minimum > second_now:
                second_rank_minimum = second_now
                amount += 1
        sio.write(str(amount))
        sio.write('\n')

    sys.stdout.write(sio.getvalue())
    return
########
main()
