"""
5
3 1 4 3 2
"""
# 전체 필요 시간 = P1 +(P1 + P2) + (P1 + P2+P3) + ..
# [Check] 이 순간이라는게 코드에서 안 와닿음 =>  줄을 세우는 각 자리(1번째, 2번째, ...)를 채울 때마다 하는 선택
# 그러나 지금 시점에서 P1, P2를 작은 크기 순서대로 정한 해 = 최적해? -> 확인 필요
"""

  왜 최적인지 핵심 논리:

  - i번째로 줄 선 사람의 시간 Pi는 자기 포함 뒤에 있는 (N-i+1)명 전부의 대기시간에 기여해
  - 네 코드의 k * v가 정확히 이걸 표현함 — k가 "뒤에 남은 사람 수(자기 포함)"
  - 그러면 총 시간을 최소화하려면, k(가중치)가 큰 자리에 작은 Pi를 배치해야 해
  - 이건 재배열 부등식(Rearrangement Inequality) 으로 증명됨: 한쪽은 내림차순(k), 다른 쪽은
  오름차순(v)일 때 곱의 합이 최소
"""
# 1*5 + 2*4 + 3*3 +3*2 + 4*1 = 5+8+9+6+4 = 32 맞아보임

import sys
input = sys.stdin.readline

N = int(input())
p_list = sorted(list(map(int, input().strip().split(" "))))
p_dict = dict(zip(range(N,0,-1),p_list)) # [Check]range(start, stop, step)
# print(p_dict)
ans = sum([ k*v for k,v in p_dict.items() ]) # [Check] list comprehensuoins, 딕셔너리 순회
print(ans)