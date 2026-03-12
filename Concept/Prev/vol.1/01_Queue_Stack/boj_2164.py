"""
6
"""
# [Mistake] 1인 경우 길이가
import sys 
# import queue
from collections import deque
input = sys.stdin.readline
# 버리는 동작이 있어서 처음 부터 주어진 카드를 바로 큐로 관리하기
# 버리는 카드 get(), 밑으로 내리느 카드는 get() + pop()
# 루프 를 while을 True로 하고, qsize가 2일 때 만 동작 다르게 하기


N = int(input())
card_queue = deque(range(1,N+1))

# [Check] 아래 for 문 vs list comprehension
# print(card_queue)
while True:
    q_length = len(card_queue)
    if q_length > 2: # [Mistake] 만약 홀수 개라면 ??, 나의 예상 결국에 반복하는 연산이 하나씩 빼느 ㄴ거니까 홀짝에 관련 없지 않을까>
        del_num = card_queue.popleft()
        insert_num = card_queue.popleft()
        card_queue.append(insert_num)
        # print(f"버리는 카드 : {del_num} 밑으로 옮기는 카드 : {insert_num} queue: {card_queue}")
    else:
        # print(f"q length = {q_length}") # 2에서 나올 것으로 예상
        break

# while문에 몯믄 처리 넣지말고 binary로(break or not) 분류해서 아닌 경우에 대해 달라져야하는 처리를 밑에서 해가 
if q_length == 2:
    card_queue.popleft()
    ans = card_queue.popleft()
else:
    ans = 1

print(ans)