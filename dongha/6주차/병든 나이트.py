'''
나이트 이동 범위
ㅁㅁㅁ이ㅁ
ㅁㅁㅁㅁ이
ㅁㅁ나ㅁㅁ
ㅁㅁㅁㅁ이
ㅁㅁㅁ이ㅁ

세로가 3 이상일 경우
  가로 길이가 7 이상일 경우 - 방법 4가지 모두 사용 가능
    이동 횟수 : 가로길이  - 2(1칸위아래+2칸오른쪽 한번씩 할 때 낭비되는 가로빈칸)
     => 1칸 위아래 한번씩(2번) + 나머지칸은 모두 위아래 2칸 왔다리갔다리)
  가로 길이가 7 미만일 경우 - 방법 4가지 사용 불가능
    이동 횟수 : min(가로길이, 4)
세로가 2일 경우 - 2칸 위.아래로 가는 이동 막힘(이동제약 무조건 걸림)
    이동 횟수 : min(가로//2 + 1, 4)
세로가 1일 경우 - 무조건 이동 가능 횟수는 1
'''

def main() :
    # 세로, 가로 입력
    ROWS, COLUMNS = map(int, input().split())

    if ROWS == 1:
        print("1")
        return
    elif ROWS == 2:
        print(min(COLUMNS - COLUMNS//2, 4))
        return
    else:
        if COLUMNS >= 7:
            print(COLUMNS - 2)
            return
        else:
            print(min(COLUMNS, 4))
            return
#####
main()