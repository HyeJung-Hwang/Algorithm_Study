"""
9
0
12345678
1
2
0
0
0
0
32
"""
# 고, x가 0이라면 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우이다. -> 반복해서 최소값을 조회해야하는 상황

# 0-쌍 부터 검사해서 NOT 고르기 
import heapq
import sys
input = sys.stdin.readline

N = int(input())
num_list = list( int(input().strip()) for i in range(N))
heap_list = []
heapq.heapify(heap_list)

for n in num_list:
    if n>0: # [Mistake] 자연수라는 조건 있음 0 아니면 그럼 대소비교 
        heapq.heappush(heap_list,n)
    else:
        if heap_list: # [Mistake] 0이 들어왔을 때 배열이 비어있을 수 있음 -> 예외처리 필요
            min = heapq.heappop(heap_list)
            print(min)
        else:
            print(0)