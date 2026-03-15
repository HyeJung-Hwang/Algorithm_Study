"""
2
"""
# Brute Force -> 조건이 666이 들어가면 되는 것으로 단순하고, N이 10,000d으로 작음
# Template
# 1. 후보군을 찾는다
# 2. 후보군에 대해서 하나씩 조건에 맞는 지 확인한다.
# 3. 정답을 찾는다.
# 루프 - True로행햐ㅏㅁ (딱히 특정 길이일 때 답이 찾아지거나, 끝나야한다는 조건 없음)
# 루프에서 해랴하는 일
# 1) 666이 있는가?
# 2) 있다면 리스트에 넣기, 없다면 pass [Mistake] 리스트 필요없음 ;;
# 3) 리스트 길이가 N이 되었다면 break

import sys
input = sys.stdin.readline

N  = int(input())
cnt = 0
num = 1
while True:
    if "666" in str(num):
        cnt += 1
    if cnt == N:
        break
    num += 1
print(num)