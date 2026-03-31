"""
5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0
"""
# 입력: 그래프
# 알고리즘: BFS() [Mistake]  "일년마다 그 칸에 동서남북 네 방향으로 붙어있는 0이 저장된 칸의 개수만큼 줄어든다"  -> 탐색 아님 일괄 계산
# 1) 전부 다 0인지 체크해서 전부 0이면 프로그램 0 출력
# 2) 1년 진행 후 , 빙산 전부 녹이기 
# 3) 덩어리 개수 세기 (dfs로 아무 빙산에 대해서 방문해서 방문경로에 현재 빙산 노드들 다 안들어가면 덩아리가 2개 이상인거로 간주 )
# 출력: 2 덩어리 이상으로되는 년, (만일 다녹을 떄까지 한 덩이면 0)
# 주의해야하는 조건 음수 방지
import sys
sys.setrecursionlimit(100000)   
input = sys.stdin.readline
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]
# def bfs(queue):
#     while queue:
#         u,v = queue.popleft()

#         for i in range(4):
#             nx,ny = u+ dx[i], v+dy[i]
#             if 0<= nx < N and 0<= ny < M:
#                 if not visited[nx][ny]: # [Mistake]계속하는 실수, 갈 수 있는데 인지 체크 안하는거 
#                     if graph[nx][ny] == 0:
#                         graph[u][v] -= 1
#                         visited[nx][ny] = 1
#                         queue.append((nx,ny))
# 재귀로 구현하는 dfs, visited 배열 구하기(순서)
def dfs(u,v, visited = None):
    if visited is None:
        visited = set()
    visited.add((u,v))
    for i in range(4):
        nx,ny = u+ dx[i], v+dy[i]
        if 0<= nx < N and 0<= ny < M:
            if graph[nx][ny]:
                if (nx,ny) not in visited:
                    dfs(nx, ny,visited)
    return visited

def bfs(u,v):
    visited = set()
    visited.add((u,v))
    queue = deque([])
    queue.append((u,v))
    # visited[u][v] = 1
    while queue:
        x,y = queue.popleft()
        for _ in range(4):
            nx, ny = x+dx[_], y+dy[_]
            if 0<= nx < N and 0 <= ny < M:
                if graph[nx][ny]:
                    if (nx,ny) not in visited: # [mistake] 거리 재는게 아니면 그냥 베열에
                        queue.append((nx,ny))
                        visited.add((nx,ny))
    return visited

if __name__ == "__main__":
    N, M = map(int,input().strip().split(" "))
    graph = [ list(map(int,input().strip().split(" "))) for _ in range(N)]
    visited  = [ [0]*M for _ in range(N)] 
    # print(N,M)
    # print(graph)
    year_cnt = 0
    while True:
        # 그래프 언롤링해서 전부 0인지 검사 ?
        # unrolled_graph =  []
        # if  all( graph[i][j] == 0 for i in range(N) for j in range(M)):
        #     year_cnt = 0
        #     break
        year_cnt += 1
        # dist에 대해 bfs] [Mistake]
        melt_cnt = [ [0]*M for _ in range(N)] 
        for i in range(N):
            for j in range(M):
                if graph[i][j]: # 빙산인 경우에, 
                    sea_cnt = 0
                    for _ in range(4):
                        if not graph[i+dx[_]][j+dy[_]]: # 주위에 바다가 있으면
                            melt_cnt[i][j] += 1
        for i in range(N):
            for j in range(M):
                graph[i][j] = max(0,graph[i][j]  - melt_cnt[i][j]) # 음수 방지 없음
        # dfs 첫번쨰 노드
        found = False # [mistake] flag 사용할 때는 초기화 꼭 해주기
        for i in range(N):
            for j in range(M):
                if graph[i][j]: 
                    now_ice_list = bfs(i,j)
                    found = True
                    break
            if found:
                break
            
        ice_list = []
        for i in range(N):
            for j in range(M):
                if graph[i][j]:
                    ice_list.append((i,j))
        if not ice_list:
            year_cnt = 0
            break
        if len(now_ice_list) != len(ice_list):
            break
        # dfs로 덩어리 수 세가 (아무 시작점에 대해 
    print(year_cnt)