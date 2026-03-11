"""
5 11 S에 포함된 N개, 검사 대상 M개
baekjoononlinejudge
startlink
codeplus
sundaycoding
codingsh

baekjoon
codeplus
codeminus
startlink
starlink
sundaycoding
codingsh
codinghs
sondaycoding
startrink
icerink
"""

"""
4 M개의 문자열 중에 집합 S에 포함되어 있는 것의 개수 
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# [Check] s = set(input() for input_value in range(n))
s = set(list(input().split() for input_s in range(n)) )
# print(s)

# [Mistake] m_set = set(list(input()[:-1] for input_s in range(m)) ) -> 중복 가능할 수 있ㅇ므
m_set = list(input()[:-1] for input_s in range(m)) 
# [Check] Complexity O(m)
# [Check] print(len(list(same  for same in m_set if same in s)))
print(sum(1 for same in m_set if same in s ))

