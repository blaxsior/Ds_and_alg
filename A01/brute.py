    
def brute_force(T: str, P: str):
    '''
    값을 하나 하나 대입하는 코드.
    '''
    cmp_count = 0
    result = []  # 발견한 위치들...
    n = len(T)  # 입력 문자열 길이
    m = len(P)  # 패턴 문자열 길이
    # 패턴의 길이가 m 이므로 해당 범위 만큼의 숫자는 비교 X
    # 따라서 비교해야 하는 인덱스 수는 n - m

    for i in range(n - m + 1):
        cond = True
        for j in range(m):
            cmp_count += 1
            if P[j] != T[j+i]: # 현재 문자가 다르면
                cond = False  # 패턴이 아님
                break
        if cond:  # 패턴에 맞으면
            result.append(i) # 배열에 삽입

    return (cmp_count, result) # 값 반환

    # 최악의 경우 모든 값을 비교 => O(mn)의 시간 대략 발생...