"""
7 3
"""

# 1234567
# 12,4567 - 3
# 456,712 - 6
# 712,45 - 2
# 457,1 - 7
# 145, - 5
# 14
# 자료구조는 큐를 쓰는게 맞고 1~3 자리르 ㄹpop하고, 1~2를 append 하는 방식 

# 1234
# 12,34 - 2
# 34,1 -4
# 31, - 1
# 3

# 입력 예외: N = 1, K >= 1 그냥 1
# N = 2, K = 1 그냥 1 -> 루프안에서 고려 

import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
queue_list = deque(range(1,n+1))
ans = []
# print(f"first queue {queue_list}")
while queue_list:
    q_length = len(queue_list)

    pop_list = []
    for i in range(k-1):
        pop_num = queue_list.popleft()
        queue_list.append(pop_num)
    del_num = queue_list.popleft()
    ans.append(del_num)



print( "<" + ", ".join(map(str,ans)) + ">")



# print(f"<{ans[:]}>")