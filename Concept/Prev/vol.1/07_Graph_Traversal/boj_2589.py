

import sys
input = sys.stdin.readline

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
# 고민: 가장 긴 시긴이 걸리는 육지 두곳을 어떻게 찾을지 그래프를 한 시작점에서 만들면, 각 노드 마다 각 노드까지의 최단거리는 모장되니까. 한번 다 탐색을 하고, max값을 찾으면 보물 위치 후보로 보고 , 모든 육지에 대해 다 bfsㄹ르 돌아야하나?
dx = [-1,1,0,0]
dy = [0,0,-1,1]


if __name__ == "__main__":
    N, M = map(int,input().split(" "))
    graph = [ [] for _ in range(n)]
    # 큐에 육지 다 넣기
    # dist 만들기
