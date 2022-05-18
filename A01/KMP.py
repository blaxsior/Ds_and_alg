    
def create_table(P: str) :
    '''
    최대 접두부 테이블을 생성하는 함수

    i : 현재까지 일치하는 길이
    j : 현재 인덱스
    O(m) 시간 내로 처리 가능.(i는 증가, k는 감소)
    '''
    count = 0
    table = []
    table.append(0) # 첫번째 원소는 0
    i = 0 # 현재까지 일치하는 길이를 의미
    # j = 0은 비교 대상 아니고, 마지막 원소까지 모두 비교한다.
    for j in range(1, len(P)):

        while i > 0 and P[i] != P[j]: 
            i = table[i - 1] # 자기 앞 인덱스에 저장된 위치로 이동
        # 탈출 조건 : i = 0 이 되거나, P[i] == P[j] 를 찾음

        count += 1 #비교 횟수
        if (P[i] == P[j]): # 값이 같다면
            i += 1 # 같은 부분 있으므로 현재 i 값에 +1
        table.append(i) # 현재 동일

    assert(len(table) == len(P))

    return (count, table)
    
            
def KMP(T: str, P: str):
    '''
    알고리즘 자체는 테이블 생성과 유사. 
    
    i: 현재 인덱스까지 일치하는 길이
    j: 현재 T의 인덱스
    O(n) 시간 내로 처리 가능 (인덱스를 단순히 보기만 한다.)
    '''
    t_count, table = create_table(P) # 최대 접두부 테이블
    len_P = len(P) # 우리 패턴의 길이
    len_T = len(T) # 전체 문자열의 길이

    result = [] # 결과 배열
 
    i = 0 # 일치하는 길이를 의미하는 변수

    count = 0

    for j in range(0, len_T) : # j 인덱스는 T의 현재 인덱스를 의미.
        count += 1
        while i > 0 and P[i] != T[j] :
            i = table[i - 1] # i 인덱스 바로 전까지 일치. 테이블 상 해당 위치에 저장된 위치로 이동!
            # 탈출 조건은 1 == 0 혹은 P[i] == T[j]
        if P[i] == T[j]: # 패턴이 일치해서 탈출한 경우
            if i == len_P - 1 : # 패턴이 일치 + 거리 만족
                result.append(j - len_P + 1) # j 인덱스는 패턴의 마지막 위치. 원하는 값은 패턴이 시작되는 위치.
                # STRING : G의 위치는 5, 시작 위치는 0. 5 - 6 + 1 = 0으로, 시작 위치를 얻을 수 있다.
                i = table[i]
            else : 
                i += 1
    return (t_count, count, result)
            
            


if __name__ == '__main__':
    p = 'acbdacba'
    rb = [0,0,0,0,1,2,3,1]
    # 00001231 나와야
    rt = create_table(p)
    print(rt)
    assert(rt == rb)