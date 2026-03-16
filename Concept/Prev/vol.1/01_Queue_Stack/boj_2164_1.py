"""
6
"""

# 1 2 3 4 5 6
# 버린다 => Queue의 First Out 
# 밑으로 옮긴다 => 원형 Usecase 다시 넣는다
# 루프 탈출 조건 => 큐의 길이가 1보다 클 때 까지 
# 루프 내 작업 
# (1) popleft()
# (2) poplfett() + append