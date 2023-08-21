name = input()
cnt = [0] * 26  # 알파벳 개수를 세기
cnt_odd = 0
odd_idx = -1
for spell in name:
    cnt[ord(spell) - ord("A")] += 1

for idx in range(26):
    if cnt[idx] % 2 == 1:
        cnt_odd += 1
        odd_idx = idx

if cnt_odd > 1:
    print("I'm Sorry Hansoo")
    quit()

ans = []
for idx in range(26):
    for j in range(cnt[idx] // 2):
        ans.append(chr(idx + ord("A")))

reverse_ans = ans[::-1]

# 홀수 인 경우 가운데 하나 추가
if cnt_odd == 1:
    ans.append(chr(odd_idx + ord("A")))


for idx in ans:
    print(idx, end="")
for idx in reverse_ans:
    print(idx, end="")
