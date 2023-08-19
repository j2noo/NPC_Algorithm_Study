'''
대략 코드설명

"I\'m Sorry Hansoo"의 출력조건 : 
  홀수인 문자의 갯수가 2개 이상이면 팰린드롬을 만들 수 없다.
사전순으로 앞서는 팰린드롬의 출력방법

ABCDE
46021 이라고 가정할 때
AA BBB D E D BBB AA
를 출력하면 된다

=> 
1) 덱을 하나 만들어서 먼저 홀수개인 문자를 전부 집어넣고
2) 위의 팰린드럼 조건을 검사하고 안나오면 예외처리하고
3) 팰린드럼 나오면 먼저 홀수개인 문자하나를 덱에 넣고, 배열에서 해당 문자 갯수 1 감소시키고
   나머지는 거꾸로 배열을 순회하면서 처음과 끝에 반반씩 집어넣는다.
4) 이후 덱을 for문 순회하면서 StringIO에 집어넣고, 한번에 write한다.
'''

import io
import sys
import collections

# 빠른 입력(엔터키 제거)
def input():
    return sys.stdin.readline().rstrip()
# 빠른 출력('\n' 없이)
def print(arg):
    sys.stdout.write(str(arg))
def isOdd(num):
    return num&1 == 1 # 특정문자 + 비트연산자 & + 1의 결과가 1이면 홀수 0이면 짝수 

def main():
    # 팰린드럼 출력 못할 때 출력할거
    MSG_ERROR = "I'm Sorry Hansoo"
    # StringBuilder같은거
    sio = io.StringIO()
    # 위에 설명한 덱
    deque = collections.deque()
    # A의 아스키 숫자 값
    ASCII_A = ord('A')
    # 대문자 알파벳들의 배열('A' ~ 'Z')
    alphabet_array = [0] * 26

    # 위의 1)
    for i in input():
        idx = ord(i) - ASCII_A
        alphabet_array[idx] += 1
    
    # 위의 2)
    odd_count = 0 # 홀수 갯수 세기
    odd_idx = None # 홀수의 인덱스
    for idx in range(26):
        if isOdd(alphabet_array[idx]):
            odd_count += 1
            odd_idx = idx
    
    if odd_count >= 2:
        print(MSG_ERROR)
        return
    
    # 위의 3)
    if odd_idx != None:
        deque.append(odd_idx) # 하나만 넣음
        alphabet_array[odd_idx] -= 1
    
    for idx in range(25, -1, -1):
        num = alphabet_array[idx]
        for _ in range(num//2):
            deque.append(idx)
            deque.appendleft(idx)

    # 위의 4
    for idx in deque:
        sio.write(chr(idx + ASCII_A)) 
        # 덱에는 65 뺀 값들이 들어간 것이기에 다시 넣어줘야 함
    print(sio.getvalue())
#####
main()