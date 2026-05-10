def solution(numer1, denom1, numer2, denom2):

    # 분모 저장
    a = denom1
    b = denom2

    # 두 분모가 같아질 때까지 반복
    # (최소공배수 찾기)
    while a != b:
        if a < b:
            a += denom1
        else:
            b += denom2

    # 공통 분모
    denom = a

    # 통분 후 분자 계산
    numer = numer1 * (denom // denom1) + numer2 * (denom // denom2)

    # 최대공약수 구하기용 변수
    x = numer
    y = denom

    # 유클리드 호제법
    while y != 0:
        x, y = y, x % y

    # 기약분수 만들기
    numer //= x
    denom //= x

    # 분자와 분모 반환
    return [numer, denom]