#brute-force, 하향식 동적 프로그래밍

#2018112070 이희준
def make_rod_cut(length: int):
    '''
    length 길이의 나무를 자르기 위한 알고리즘.
    나무를 잘라 배열에 저장.
    n에 대해, 총 나무의 조합 수는 2^(n-1)개 발생 가능

    1 | 1 | 1
    1   1 | 1
    1 | 1   1
    1   1   1

    1 | 1 | 1 | 1
    1   1 | 1 | 1
    1 | 1   1 | 1
    1 | 1 | 1   1
    1   1   1 | 1
    1   1 | 1   1
    1 | 1   1   1
    1   1   1   1

    자르면 0, 안자르면 1로 문자열 붙이기
    이후 1이 등장할 때까지 숫자 더하다가, 1 등장하면 다음 숫자 시작.
    나온 결과를 배열에 저장해서 돌려준다.
    '''
    cut = ['0', '1'] #  자르는지 여부
    all_condition = [''] #  2^(n-1) 개의 조건들
    
    for _ in range(length - 1): # 막대의 개수는 최대 길이 - 1
        inner_strs = [] # 내부처리용

        for cond in all_condition:
            for c in cut:
                inner_strs.append(cond+c) # '0' / '1' 넣기
        
        all_condition = inner_strs # 배열 바꾸기

    result : set[list[int]] = set() # 나무 잘린 길이에 대한 배열을 저장하는 배열 ...
    # 중복 제거를 위해 set으로 선언. 실제 계산할 때 중복 제거가 목적.

    for cond in all_condition: # 현재 위치에서 잘랐는지 여부에 따른 길이 조합 반환
        inner_result = []

        cur = 1 # 현재 잘린 나무의 길이. 초기값은 항상 1이 된다.
        for ch in cond: # ch 는 '0' 또는 '1'의 값.
            match ch:
                case '0': #안잘림
                    cur += 1 # 현재 나무 길이 1 증가
                case '1': # 잘렸다...
                    inner_result.append(cur) # 자른 나무 넣고
                    cur = 1 # 초기값 다시 지정
        inner_result.append(cur) # 마지막 나무 덩이 삽입
        inner_result.sort() # 값 정렬
        inner_result = tuple(inner_result) # 해싱을 위해 튜플로 변환
        # 리스트는 set 자료구조에 안들어간다

        result.add(inner_result) # 나무 자른 모음 저장
    
    return list(result) # 리스트로 바꿔서 반환

#2018112070 이희준
def brute_rod_cut(p: list[int], n: int):
    '''
    @param p 가격이 저장된 테이블
    @param n 원하는 길이
    
    brute force 방식으로 구현한 막대 자르기 알고리즘
    make_rod_cut으로 막대 조합 가져와서 각각의 값에 따라 계산한다.

    p의 대응되는 인덱스가 존재.
    '''
    rod_list = make_rod_cut(n) # 길이 n에 대한 잘린 막대 리스트

    result = -1 # 길이 i에 대한 최대 수익. 초기 -1

    for rods in rod_list:
        temp = 0
        for rod in rods: # 리스트 내의 변수들
            temp += p[rod - 1] # 대응되는 값 얻음.
            # rod의 길이가 3 이면, 대응되는 인덱스는 2.
        if temp > result : # 값이 더 크면 교체
            result = temp
    return result

#2018112070 이희준
if __name__ == '__main__':
    p = [1,5,8,9,10,17,17,20,24,30]
    cut_rods = make_rod_cut(9)
    for i in range(len(cut_rods)):
        print(cut_rods[i], end=' ')
        if i%5 == 0:
            print()
    print()
    print("result : ", brute_rod_cut(p, 9))
# print(make_rod_cut(5))