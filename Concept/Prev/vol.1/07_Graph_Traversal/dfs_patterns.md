# DFS 패턴 정리

## 패턴 1: 누적합 (경로 합)

```python
def dfs(node, total):
    total += value[node]
    if 리프:
        result.append(total)
        return
    for neighbor in graph[node]:
        dfs(neighbor, total)
```

## 패턴 2: 백트래킹 (선택/취소)

```python
def dfs(depth, path):
    if 완성:
        result.append(path[:])
        return
    for choice in choices:
        path.append(choice)   # 선택
        dfs(depth+1, path)
        path.pop()            # 취소
```

## 패턴 3: 영역 크기 (연결된 노드 수)

```python
def dfs(i, j):
    visited[i][j] = 1
    cnt = 1
    for 4방향:
        if 유효하고 미방문:
            cnt += dfs(nx, ny)  # 누적
    return cnt
```

---

## BFS vs DFS 패턴 차이

|  | BFS | DFS |
|--|-----|-----|
| 주로 구하는 것 | 시작점→목적지 거리 | 모든 노드 누적값 |
| 값 전파 방식 | 이전칸 + 1 | 재귀로 누적 후 리턴 |

---

## 자주 헷갈리는 BFS 실수

### 1. 멀티소스 BFS - 시작점을 따로따로 돌리면 안 됨

시작점들이 **동시에** 퍼져야 할 때는 큐에 한꺼번에 넣고 BFS 한 번만 돌려야 해요.

```python
# 틀린 방식 - 시작점마다 따로 BFS
for i in range(M):
    for j in range(N):
        if graph[i][j] == 1:
            bfs(i, j)  # 독립적으로 퍼짐 → 동시성 없음

# 올바른 방식 - 멀티소스 BFS
queue = deque()
for i in range(M):
    for j in range(N):
        if graph[i][j] == 1:
            queue.append((i, j))  # 전부 한꺼번에
bfs(queue)  # 한 번만
```

언제 쓰나: "시작점들이 서로 영향을 주며 동시에 퍼지는" 문제 (토마토, 불 번지기 등)

---

### 2. 날짜/거리 카운팅 - cnt로 세면 안 됨

`cnt += 1`은 **노드 수**를 세는 거라 거리(날짜)가 아니에요.
graph에 거리를 직접 기록하고 마지막에 최댓값을 구해야 해요.

```python
# 틀린 방식
cnt += 1  # 노드 수 = 날짜 아님

# 올바른 방식
graph[nx][ny] = graph[u][v] + 1  # 이전 칸 거리 + 1

# BFS 끝난 후
ans = max(graph[i][j] for i in range(M) for j in range(N) if graph[i][j] > 0)
print(ans - 1)  # 시작점이 1부터라 -1
```

왜 최댓값이 답이냐: 가장 늦게 익는 칸 = 가장 먼 칸 = 최댓값

---

## 멀티소스 BFS 추천 문제

### 유형 1. 여러 출발점에서 동시 전파
- **7576 토마토** (실버1)
- **4179 불!** (골드4)

### 유형 2. 여러 출발점 중 최단거리
- **18405 경쟁적 전염** (골드5)
- **7569 토마토 3D** (골드5)

### 유형 3. 특정 구역에서 거리 계산
- **14940 쉬운 최단거리** (실버1)
- **2146 다리 만들기** (골드3)