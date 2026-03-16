"""
7
3 1 6 2 7 30 1
"""
#  측정할 수 없는 양의 정수 무게 중 최솟값
# 브루트포스 라면?
# 1. 탐색 범위 1~
# 2. 루프 작업: N - (c1) - (c2),추의 무게 큰 순으로 계속 뺴기 0 될 떄까지,  # [Check] 추의 무게순서대로 채우지 않아야, N이 채워지는 케이스가 있지 않을ㄲ?
# N - (c2) - (c3) 
# -> 21 - 7 - 6 - 3 -2 -1 -1 0 이 안되면 break
# -> 6 - 3 - 2 - 1
# -> 3 -2 -1
# -> 20 - 7 - 6 
# 2. 루프 break: N을 찾았을 떄, 가장 작은 추 순서로 다 뻈는데 안 될떄 -> 21 - 1 - 1 - 2 - 3 -6 -7 
"""
  그리디인 이유

  네가 말한 것처럼 탐색 범위 자체가 다른 게 핵심이야.

  - 브루트포스: "무게 N을 만들 수 있나?"라는 질문을 반복
  - 그리디: "이 추를 쓰면 범위가 어디까지 늘어나나?"라는 확장을 반복

  그리디가 가능한 이유는 **"작은 추부터 보면, 이전까지의 결과(측정 가능 범위 S)만으로 다음 판단이
  가능하다"**는 성질 때문이야.

  S=0 → 추1 ≤ S+1? → Yes → S 확장
  S=새값 → 추2 ≤ S+1? → Yes → S 확장
  ...
  S=20 → 추30 ≤ 21? → No → 답은 21

  매 순간 "지금 가장 작은 추를 쓴다"는 선택이 전체 최적이고, 이전 선택을 되돌릴 필요가 없으니
  그리디야.
"""

import sys
input = sys.stdin.readline

N  = int(input())
c_list = list(map(int,input().strip().split(" ")))
print(N,c_list)
num = 1
left_num = 1
while True:

    candidate_c_list = sorted(list(filter(lambda n: n <= num,c_list)),reverse=True)
    print(candidate_c_list)
    print(num,left_num)
    for i,c in iterate(candidate_c_list): # [Mistake] 4 - 3 - 2 했을 떄 4 - 3 - 1로 넘어가게 하기 o(n*2)
        check = left_num - c
        if check > 0:
            left_num -= c
            pass
        elif check == 0:
            print(f"{num} is measurable")
            left_num -= c
            break
        else:
            print(f"move to next canddiate")
            pass
    print(f"{num} -> {left_num}")
    if left_num ==0:
        num += 1
        left_num = num
    else:
        break
print(f"최솟값 {num}")
