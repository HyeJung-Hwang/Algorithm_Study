"""
5
12 7 9 15 5
13 8 11 19 6
21 10 26 31 16
48 14 28 35 25
52 20 32 41 49
"""

# N 번쨰 큰수 
# [Idea] 반복해서 최대값을 4번 뺴면 4*O(1)

import sys
import heapq
input = sys.stdin.readline

N = int(input())
array = []
# array.append(list(map(int, input().split()) for i in range(N))) # [Check]

for i in range(N):
    array.extend(map(int, input().split()))
# [Mistake] 최대힙  
array = [-i for i in array]
heapq.heapify(array)
for i in range(N-1):
    heapq.heappop(array)
print(-heapq.heappop(array))

# [Mistake] 메모리ㅣ 초과 , 공간복잡도, 고려 안한 점 = 모든 수는 자신의 한 칸 위에 있는 수보다 크다는 것이다. 

'''

⏺ N×N개 원소를 전부 메모리에 올리기 때문에 메모리 초과가 납니다.

  N=1500이면 1500×1500 = 2,250,000개를 다 저장하게 됩니다.                                                             
   
  개선: 크기 N짜리 최소 힙만 유지                                                                                      
                  
  "모든 수는 자신의 한 칸 위에 있는 수보다 크다"는 조건을 활용하면, 힙에 N개만 유지하면서 풀 수 있습니다.

  import sys
  import heapq
  input = sys.stdin.readline

  N = int(input())
  heap = list(map(int, input().split()))  # 첫 줄로 힙 초기화 (N개)
  heapq.heapify(heap)

  for i in range(N - 1):
      row = map(int, input().split())
      for num in row:
          if num > heap[0]:          # 현재 최솟값보다 크면
              heapq.heapreplace(heap, num)  # 최솟값 빼고 새 값 넣기

  print(heap[0])  # N번째 큰 수 = 힙의 최솟값

  핵심: 크기 N짜리 최소 힙에 큰 값만 남기면, 힙의 최솟값이 곧 N번째 큰 수입니다. 메모리는 항상 **O(N)**만 사용합니다
'''