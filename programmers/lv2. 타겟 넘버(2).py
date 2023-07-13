from itertools import product

def solution(numbers,target):
    l = [(x, -x) for x in numbers]
    print(l)