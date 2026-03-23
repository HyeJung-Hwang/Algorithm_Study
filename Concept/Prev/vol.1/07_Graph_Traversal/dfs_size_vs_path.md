# DFS - 누적합 vs 경로 저장

## 누적합 버전

```python
def dfs(i, j):
    size = 1           # 자기 자신 카운트
    visited[i][j] = 1
    for _ in range(4):
        nx, ny = i + dx[_], j + dy[_]
        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny] and graph[nx][ny] == 1:
                size += dfs(nx, ny)  # 반환값을 더함
    return size
```

## 경로 저장 버전

```python
def dfs(i, j, visited_list):
    visited_list.append((i, j))  # 자기 자신 리스트에 추가
    visited[i][j] = 1
    for _ in range(4):
        nx, ny = i + dx[_], j + dy[_]
        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny] and graph[nx][ny] > 0:
                dfs(nx, ny, visited_list)  # 리스트 공유
    return visited_list
```

## 재귀 흐름 (누적합)

```
dfs(A) → size = 1
    dfs(B) → size = 1
        dfs(C) → size = 1
                  return 1
        size = 1 + 1 = 2
        return 2
    size = 1 + 2 = 3
    return 3
```

끝단 노드부터 1로 시작해서 올라오면서 더함.

## size를 인자로 전달하면 안 되는 이유

```python
def dfs(i, j, size):  # 잘못된 방식
    size += 1
    for ...:
        dfs(nx, ny, size)  # size를 복사해서 넘김
    return size            # 이웃 결과가 반영 안 됨!
```

Python에서 `int`는 **값 복사**로 전달됨 → 이웃이 계산한 결과가 반영 안 됨.

```
dfs(A, size=0)
    size = 1
    dfs(B, size=1)  ← A의 size를 복사해서 넘김
        size = 2
        return 2    ← A는 이 결과를 안 받음!
    return 1        ← B가 센 거 반영 안 됨
```

## int vs list 전달 차이

| | int | list |
|---|---|---|
| 전달 방식 | 값 복사 | 참조 전달 |
| 이웃 변경이 반영되나? | X | O |
| 사용 방식 | 반환값으로 받아서 더함 | 인자로 넘겨서 공유 |

> **결론:** 누적합은 `size += dfs(nx,ny)` 로 반환값 받기, 경로는 리스트를 인자로 공유하기
