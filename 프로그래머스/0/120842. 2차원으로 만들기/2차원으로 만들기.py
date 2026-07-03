def solution(num_list, n):
    # 결과를 저장할 2차원 리스트
    answer = []

    # n칸씩 건너뛰며 반복
    # 예) n=2 -> 0, 2, 4, 6 ...
    for i in range(0, len(num_list), n):

        # 현재 위치부터 n개의 원소를 잘라서 answer에 추가
        answer.append(num_list[i:i+n])

    # 완성된 2차원 리스트 반환
    return answer