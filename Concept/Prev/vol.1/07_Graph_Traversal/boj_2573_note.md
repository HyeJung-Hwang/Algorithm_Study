# BOJ 2573 빙산 - 풀이 노트

## 알고리즘 흐름
1. 매 년 빙산 녹이기 (주위 바다 개수만큼 감소, 음수 방지)
2. BFS로 덩어리 체크 (첫 빙산에서 시작해서 연결된 수 vs 전체 빙산 수 비교)
3. 다 녹을 때까지 분리 안 되면 0 출력

---

## 버그 모음

### 1. melt_cnt 위치 오류
```python
# 잘못됨: 바다 칸에 카운트
melt_cnt[i+dx[_]][j+dy[_]] += 1

# 올바름: 빙산 칸에 카운트
melt_cnt[i][j] += 1
```

### 2. DFS가 바다도 탐색
```python
# 빙산인 경우만 탐색해야 함
if graph[nx][ny]:
    if (nx,ny) not in visited:
        dfs(nx, ny, visited)
```

### 3. ice_list에 모든 칸 추가
```python
# 빙산만 추가해야 함
if graph[i][j]:
    ice_list.append((i,j))
```

### 4. mutable 기본 인자
```python
# 잘못됨: 호출 간 리스트 공유됨
def dfs(u, v, visited=[]):

# 올바름
def dfs(u, v, visited=None):
    if visited is None:
        visited = []
```

### 5. DFS 시작점을 하나만 써야 함
```python
# 첫 번째 빙산에서만 시작해야 하므로 flag로 이중 break
found = False
for i in range(N):
    for j in range(M):
        if graph[i][j]:
            now_ice_list = bfs(i, j)
            found = True
            break
    if found:
        break
```
- `break`는 바로 감싸는 루프 하나만 탈출
- Python에는 `break 2` 같은 문법 없음
- flag 변수로 바깥 루프도 탈출

### 6. 음수 방지
```python
graph[i][j] = max(0, graph[i][j] - melt_cnt[i][j])
```

### 7. now_ice_list NameError
- 빙산이 다 녹은 후 now_ice_list 사용 시 NameError 발생
- ice_list가 비어있으면 먼저 break 처리

```python
if not ice_list:
    year_cnt = 0
    break
```

### 8. found 초기화 누락
- while 루프 매 반복마다 `found = False` 초기화 필요
- 초기화 안 하면 이전 반복의 True 값이 남아서 오동작

---

## 시간 초과 원인들

### 재귀 DFS → BFS로 교체
- Python 재귀는 함수 호출 오버헤드가 큼
- `sys.setrecursionlimit`으로도 한계 있음
- BFS(deque) 또는 반복문 DFS(stack)로 교체

### BFS 시작 노드를 visited에 추가 안 함 → 무한루프
```python
visited = set()
visited.add((u,v))  # 반드시 추가
queue = deque([(u,v)])
```

### N*M 전체 순회 → 빙산 위치 set으로 관리
```python
ice_set = {(i,j) for i in range(N) for j in range(M) if graph[i][j]}

# 매 반복마다 O(N*M) 대신 O(빙산수)만 순회
for (i,j) in ice_set:
    ...
```

---

## Python 문법 정리

### all / any
```python
all(조건 for x in 리스트)  # 전부 True면 True (and 느낌)
any(조건 for x in 리스트)  # 하나라도 True면 True (or 느낌)

# 조기 종료(short-circuit) 있음 → set보다 효율적
```

### list vs set (not in 체크)
```python
(x,y) not in list  # O(N) - 전체 탐색
(x,y) not in set   # O(1) - 해시 탐색
```

---

## BFS vs DFS 선택 기준
| 목적 | 선택 |
|------|------|
| 최단거리 | BFS |
| 경로 추적, 사이클 탐지 | DFS |
| 연결 여부, 덩어리 세기 | 아무거나 (결과 동일) |

- Python에서 재귀 DFS는 느림 → **BFS 또는 반복문 DFS(stack) 사용**

---

## 최종 풀이 핵심
```python
ice_set = {(i,j) for i in range(N) for j in range(M) if graph[i][j]}

while True:
    year_cnt += 1
    # melt
    melt_cnt = {(i,j): sum(1 for k in range(4) if not graph[i+dx[k]][j+dy[k]]) for (i,j) in ice_set}
    new_ice_set = set()
    for (i,j) in ice_set:
        graph[i][j] = max(0, graph[i][j] - melt_cnt[(i,j)])
        if graph[i][j]:
            new_ice_set.add((i,j))
    ice_set = new_ice_set
    # 다 녹음
    if not ice_set:
        year_cnt = 0; break
    # 덩어리 체크
    si, sj = next(iter(ice_set))
    if len(bfs(si, sj, ice_set)) != len(ice_set):
        break
```
