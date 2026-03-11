"""
3 
10 
20
40
"""
# (10+20) + (30+40)
"""
4
10
20
40
50
"""
"""
2
10
20
"""
# . (10+20)+ (30+40) + (70+50) = 30 + 70 +120
# = N = # of bunches

import sys
input = sys.stdin.readline

N = int(input())


# [Mistake] 한 줄 씩 입력 받는 경우 N 번 Input() 받아야함

b_list = [input().strip()  for  i in range(N)] 
b_int_list = sorted([int(i) for i in b_list ])

# [Mistake] 최솟값을 반복적으로 꺼내는 연산이 필요한 상황 .



