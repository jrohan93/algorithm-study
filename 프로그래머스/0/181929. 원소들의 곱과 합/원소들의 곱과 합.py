import math

def solution(num_list):
    answer = 0
    if math.prod(num_list) < sum(num_list) ** 2 :
        answer = 1
    else :
        answer = 0
    
    return answer