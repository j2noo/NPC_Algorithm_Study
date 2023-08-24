import sys
def input() : return sys.stdin.readline().rstrip()

def main():
    # 포도주 잔의 개수 n
    GLASSES = int(input())

    # 잔에 들어있는 포도주들의 양을 나타내는 배열
    WINE_TABLE = [0] * GLASSES
    # DP테이블 - 해당 번째 포도주를 마신다고 가정했을 때, 0번째부터 해당 번째의 포도주를 마셨을 때 가장 많은 양을 마시는 경우, 그 양을 적은 배열
    dp_table = [0] * GLASSES

    # 포도주 양 입력받기
    for i in range(GLASSES):
        WINE_TABLE[i] = int(input())

    # 만일 n이 1이거나 2일 경우의 예외처리
    if GLASSES <= 2:
        if GLASSES == 1:
            print(WINE_TABLE[0])
            return
        else: #2
            print(WINE_TABLE[0] + WINE_TABLE[1])
            return

    # 1,2,3번째 경우
    dp_table[0] = WINE_TABLE[0]
    dp_table[1] = WINE_TABLE[0] + WINE_TABLE[1]
    dp_table[2] = max(
        WINE_TABLE[0]+WINE_TABLE[1],
        WINE_TABLE[0]+WINE_TABLE[2],
        WINE_TABLE[1]+WINE_TABLE[2]
    )

    # 4번째부터는 아래의 규칙을 따름
    #  dp(n) = max(
    #      dp(n-2) + w(n)
    #      dp(n-3) + w(n-1) + w(n)
    # )
    # N-1번째 와인을 포기하는 경우 -> N-2번째 DP와 N번째 와인양의 합이 N번째 DP
    # N번째 와인을 포기하는 경우 -> N번째 DP는 N-1의 DP와 동일
    for i in range(3, GLASSES):
        dp_table[i] = max(
            dp_table[i-2] + WINE_TABLE[i], 
            dp_table[i-3] + WINE_TABLE[i-1] + WINE_TABLE[i]           
        )
        # 포도주를 2번 연속 안먹을 경우도 고려
        dp_table[i] = max(dp_table[i-1], dp_table[i])
    # 최대로 마실 수 있는 포도주의 양 출력
    print(dp_table[GLASSES-1])
    return
#####
main()