from random import choices
acgt = ['A', 'C', 'G', 'T']

def create_union_str(n: int, ch_list: list[str]):
    '''
    길이 n, m개의 원소를 가진 리스트를 기반으로 m^n 개의 변수를 만든다.
    '''
    temp = ['']

    for _ in range(n): # n번 길이
        inner_temp =[] # 다음 길이

        for val in temp:
            for ch in ch_list:
                inner_temp.append(val+ch)
        
        temp = inner_temp # 배열 바꾸기
    return temp
            
def create_rand_ACGT(n: int):
    '''
    n * 1000 개의 ACGT 문자를 output 파일에 적는다.
    '''
    # 1000개 단위로 1000번 쓸 예정
    with open('input.txt', 'w+') as f:
        for _ in range(n):
            print("current :", _)
            acgt_str = ''.join(choices(acgt, k = 1000))
            f.write(acgt_str)
