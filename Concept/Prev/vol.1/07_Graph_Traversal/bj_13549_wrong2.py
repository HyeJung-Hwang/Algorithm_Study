# 입력: 일차원 배열(리스트)
# 알고리즘: 최단 거리이면 BFS, 시작점에서 한 레벨씩(단쉰히 상하 좌우가 아니라, 앞, 뒤, 점프에 대해 다해보기 ) 이동하면서, 최단거리 업데이트 하기 ?
# 고려해야하는 점 : -1이 된다.

"""
5 17
"""
# 입력: 그래프 (1차원 배열)
# 알고리즘: BFS (가장 빠른 시간 = 거리), 시작점은 수빈 위치
# 출력: 현재 위치 = 동생위치가 되었는지 검사해서 동생위치 되었을 때, 그지점까지의 최소 거리를 출력

import sys
from collections import deque
input = sys.stdin.readline
MAX_LEN = 100001

def bfs(v,K):
    # BFS의 큐 = "방문 예정인 노드들을 저장하는 자료구조"
    # 큐에 추가 = 방문 예약 (visited 체크로 중복 방지)
    # 큐에서 popleft = 실제 방문/탐색
    queue = deque([v])  # 시작 노드를 방문 예정 목록에 추가
    graph[v] = 0
    # visited[v] = 1
    while queue:
        x = queue.popleft()  # 큐에서 꺼냄 = 지금 실제로 방문/탐색
        # print(x)
        if x == K: #[Answer]
            # print(x,nx,queue,graph[x])
            return graph[x]
        # ↑ 여기서 체크해야 함! 큐에서 꺼낸 시점 = 실제 방문 완료
        # BFS는 레벨 순서대로 탐색하므로, 처음 꺼낸 K가 최단 거리를 보장

        for i in [0,1,2]:
            if i == 0:
                nx = 2*x
                if 0 <= nx < MAX_LEN and graph[nx] == -1: #[Mistake] 수의 범위와 인덱스의 범위느 ㄴ다르다.
                    # visited[nx] = 1  # 방문 예약
                    graph[nx] = graph[x]   # 오는데 걸리는 시간 업데이트
                    queue.appendleft(nx)  # 큐에 추가 = 나중에 방문 예정


            elif i == 1:
                nx = x + 1
                if 0 <= nx < MAX_LEN and graph[nx] == -1:#[Mistake] 수의 범위와 인덱스의 범위느 ㄴ다르다.
                    # visited[nx] = 1  # 방문 예약
                    graph[nx] = graph[x] + 1  # 오는데 걸리는 시간 업데이트
                    queue.append(nx)  # 큐에 추가 = 나중에 방문 예정
            else:
                nx = x - 1 
                if 0 <= nx < MAX_LEN and graph[nx] == -1: #[Mistake] 수의 범위와 인덱스의 범위느 ㄴ다르다.

                    # visited[nx] = 1  # 방문 예약 (중복 방지)
                    graph[nx] = graph[x] + 1  # 오는데 걸리는 시간 업데이트
                    queue.append(nx)  # 큐에 추가 = 나중에 방문 예정

            # if nx == K: #[Mistake]
            #     print(x,nx,queue)
            #     break
            # ↑ 여기서 체크하면 안됨!
            # 이유: nx == K일 때 K를 큐에 추가만 하고, 아직 큐에서 꺼내지 않은 상태
            #       즉, K를 "방문 예약"만 한 것이지 "실제 방문"은 안한 상태에서 종료
            #       큐에 있는 K = 방문 예정, popleft한 K = 방문 완료
            #       최단 거리는 K를 처음으로 큐에서 꺼낸(방문한) 시점에 확정됨

        # break


        
                
if __name__ == "__main__":
    graph = [-1 for _ in range(MAX_LEN)] # [Mistake]0으로 하면 안됨 거리가 0인경우 있음
    visited = [0 for _ in range(MAX_LEN)]

    N, K = map(int, input().split())
    # graph[N] =
    ans = bfs(N,K)
    print(ans)