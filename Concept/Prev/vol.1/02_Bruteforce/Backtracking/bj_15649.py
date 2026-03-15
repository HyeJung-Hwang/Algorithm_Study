"""
3 1
"""
## 브루트포스 풀이 vs 백트래킹 풀이
# 탐색 범위 구성에 차이
# 브루트포스 = 1~N 사이 숫자로 M길이 수열 전부다 만들기 / 만드는 방식,M길이 맨 앞자리 부터 1부터 채우고 다음 자리 넘어가고 해서 string에 계속 더하면서 확인
# 벡트레킹 = 수열 만드는 중에 중복 있는지 없는 지 체크 / 만드는 방식,,M길이 맨 앞자리 부터 1부터 채우고 다음 자리에서는 1빼고 탐색 ..
# [Check] 그냥 라이브러리 풀이
# from itertools import permutations
import sys
input = sys.stdin.readline

n, m = map(int, input())

