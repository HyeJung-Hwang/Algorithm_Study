



"""
5 7
WLLWWWL
LLLWLLL
LWLWLWW
LWLWLLL
WLLWLWW
"""
# 입력: 그래프
# 알고리즘: 멀티소스 BFS 
# 고민: 가장 긴 시긴이 걸리는 육지 두곳을 어떻게 찾을지 ?
# 아이디어 1) 그래프를 한 시작점에서 만들면, 그래프에 속한 각 노드 마다 각 노드까지의 최단거리는 보장되니까. 한번 다 탐색을 하고, max값을 찾으면 보물 위치 후보로 보고 , 모든 육지에 대해 다 bfsㄹ르 돌아야하나?
# 출력: 그래프의 max값?
import sys
input = sys.stdin.readline
from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(u,v,dist):
    queue = deque([(u,v)])
    dist[u][v] = 0
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<= nx < N and 0 <= ny < M:
                if graph[nx][ny] == "L":
                    if dist[nx][ny] == -1:
                        dist[nx][ny] = dist[x][y] + 1 # 육지인 경우는 bfs 통해 레벨별로 탐색하며 최단거리를 구해 나가고, 
                        queue.append((nx,ny))
                        # print(f"add {nx, ny} and update {dist[nx][ny]} ")
    unrolled_dist = [x for row in dist for x in row]
    # print(dist)
    # print(unrolled_dist)
    return max(unrolled_dist)
if __name__ == "__main__":
    N, M = map(int,input().strip().split(" "))
    graph = [ list(input().strip()) for _ in range(N) ]
    dist = [ [0]*M for _ in range(N) ]
    # 큐에 육지 다 넣기 
    # queue = deque([])
    ans_list = []
    for n in range(N):
        for m in range(M):
            if graph[n][m] == "L":
                # [Mistake] dist 초기화 필요, 방문 안한걸 -1, 하면서 0으로 시작
                new_dist = [[-1]*M for _ in range(N)] 
                ans = bfs(n,m, new_dist)
                ans_list.append(ans)
    # dist 만들기
    print(max(ans_list)) 
