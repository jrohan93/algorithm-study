def solution(a, b):
    answer = 0
    c = int(str(a) + str(b))
    d = 2 * a * b
    
    if c > d :
        answer = c
    else :
        answer = d
    return answer