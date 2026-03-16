"""
7 3
"""

# 원을 이룬다 => 큐
# 남은 사람들로 이루어진 원을 따라 => 순서 존재
# 답 역시 순서를 구해야함 
# 루프: N명의 사람들이 모두 제거될떄 까지 => 큐가 빌 때 까지 계속 진행
# 루프 내 작업: 1~2 요소 pop 후 다시 뒤로 3 요소 pop => 큐떠올리기 여기서 # [Mistake] K 번 해야함 
# 1234567
# 123,4567 => 3
# 456,712 => 6

import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int,input().split())
_queue = deque(range(1,N+1))
ans = []
while _queue:
    for i in range(1,K):
        del_num = _queue.popleft()
        _queue.append(del_num) # [Mistake] K 번 해야함 
        # print(del_num)
    ans.append(_queue.popleft())
print("<"+", ".join(map(str,ans))+">")
