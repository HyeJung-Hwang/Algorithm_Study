

'''
test case 1 input
5
4 1 5 2 3
5
1 3 7 9 5
'''

'''
test case 1 output
1
1
0
0
1
'''
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    # X가 여러 개일 수 있음
    # 입력 1
    N = int(input())
    # 입력 2
    n_set = set(map(int, input().split())) # iterable한 map 객체로 받아서 바로 hash 자료형으로 저장하면 검색이 쉬울 것으로 생각
    # 입력 3
    q = input()
    # 입력 4
    # [Mistake] x_list = set(map(int, input().split()))  -> x_list를 set으로 하면 순서 보장이 안된다. testcase 상으로 순서 보장은 필요
    x_list = list(map(int, input().split()))
    # [Mistake] print( 1 if x in n_set else 0 for x in x_list) -> generator 표현식이므로 바로 출력할 수 없음
    print(*(1 if x in n_set else 0 for x in x_list),sep="\n")