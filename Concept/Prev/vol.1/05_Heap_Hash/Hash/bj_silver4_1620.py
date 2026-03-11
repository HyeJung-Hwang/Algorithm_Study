'''
26 5 N=포켓몬의 개수 M=문제의 개수 
Bulbasaur
Ivysaur
Venusaur
Charmander
Charmeleon
Charizard
Squirtle
Wartortle
Blastoise
Caterpie
Metapod
Butterfree
Weedle
Kakuna
Beedrill
Pidgey
Pidgeotto
Pidgeot
Rattata
Raticate
Spearow
Fearow
Ekans
Arbok
Pikachu
Raichu
25
Raichu
3
Pidgey
Kakuna
'''
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
pocket_list = list(input().strip() for intput_try in range(n))

number_pocket_dict = dict(zip(list(range(1, n + 1)), pocket_list))
pocket_number_dict = dict(zip(pocket_list, list(range(1, n + 1))))

test_list = list(input().strip() for input_test in range(m))
for test in test_list:
    if test.isdigit():
        print(number_pocket_dict[int(test)])
    else:
        print(pocket_number_dict[test])