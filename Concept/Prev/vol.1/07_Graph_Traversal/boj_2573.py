"""
5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0
"""
# 입력: 그래프
# 알고리즘: BFS()
# 1) 1년 진행 후 , 멀티소스 BFS로 빙산 전부 탐색하기 ,(다른 빙산이 바다가 되는 거로 인해 녹는게 달라져서 ) 
# 2) 덩어리 개수 세기 (dfs로 방문해서 방문경로에 현재 빙산 노드들 다 안들어가면 덩아리가 2개 이상인거로 간주 )

import sys
input = sys.stdin.readline

def bfs():
    pass
def dfs():
    pass

if __name__ == "__main__":
    N, M = map(int,input().strip().split(" "))
    graph = [ list(map(int,input().strip().split(" "))) for _ in range(N)]
    dist = graph.copy()
    # print(N,M)
    # print(graph)
    year_cnt = 1
    while True:
        # dist에 대해 bfs

        # dfs로 덩어리 수 세가 (아무 시작점에 대해 )
        year_cnt += 1