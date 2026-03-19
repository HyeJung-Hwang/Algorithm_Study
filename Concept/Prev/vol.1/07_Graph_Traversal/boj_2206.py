"""
6 4
0100
1110
1000
0000
0111
0000
"""
# 입력: 그래프(이차원 배열)
# 알고리즘: BFS <- 최단거리라서
# 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.
# 1) 안부수면 이동 못할 떄
# 2) 아직 부수지 않았다면, 부수고 가는 경우의수도 따지기 ?? 상하좌우 + 부수기 
# 탐색 중에 현재 부서졌는지 여부를 알기위해 상태를 저장해야한다.!
# 도달 출력 안되는 경우, 이미 부수기찬스썼는데 또 안 부수면 못갈 떄
# 출력: (N,M) 도착했을 때의 업데이트된 그래프 값


import sys
input = sys.stdin.readline
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs():
    queue = deque([(0,0,0)]) # 큐에 들어가는 상태 (x좌표, y좌표,플래그) 플래그가 탐색에 쓰여야한다.
    dist[0][0][0] = 1
    graph[0][0] = 1

    flag = False
    while queue:
        u,v,flag = queue.popleft()
        # print(u,v,flag) 
        if u == N-1 and v == M-1:
            return dist[u][v][flag] # 모든케이스는 여기서 나올테니 
        for i in range(4):
            nx,ny = u + dx[i], v+dy[i]
            if 0 <= nx < N and 0<=ny <M: # [TIL]: 범위에 맞는지 -> 방문 가능한 노드인지 -> Flag별 로직 -> 넣기 직전에 방문 여부 보기

            # 일단 미방문 노드의 경우
                # 다음칸이 0 일때 
                if graph[nx][ny] == 0:
                    if dist[nx][ny][flag] == float('inf'):
                        dist[nx][ny][flag] = dist[u][v][flag] + 1
                        queue.append((nx,ny,flag))

                # 다음칸이 1일 떄 복잡해짐
                else: 
                    if flag == 1:
                        pass
                    else:
                        if dist[nx][ny][flag] == float('inf'):
                            # flag = 1
                            dist[nx][ny][1] = dist[u][v][0] + 1
                            queue.append((nx,ny,1))


    if graph[N-1][M-1] == 0:
        return -1

if __name__ == "__main__":
    N,M = map(int,input().split(" "))
    graph = [ list(map(int,input().strip())) for _ in range(N)]
    # visited = [ [0]*M for _ in range(N)]
    # [TIL] 거리 저장용 배열 원본 입력 배열과 다르게 관리하기 , float("inf") 사용해서 초기화하기
    dist = [ [ [float('inf')]*2 for _ in range(M)] for _ in range(N)] # [TIL] Flag에 따라 distance 저장하기 위해 리스트 사용 (머리로 잘 상상 안됨)
    ans = bfs()
    print(ans)