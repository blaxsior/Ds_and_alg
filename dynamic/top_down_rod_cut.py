#2018112070 이희준
def top_down_rod_cut(p: list[int], n: int, r: list[int]):
    '''
    하향식으로 구현된 막대자르기 알고리즘

    @param length 특정 길이의 막대에 대한 가격표
    @param n 현재 주어진 막대 길이
    @param 특정 길이의 막대에 대한 최대 수익 테이블
    '''
    if n == 0:  # n이 0이면
        return 0  # 0 반환

    idx = n - 1  # 배열에서 n에 대한 값이 실제 저장되는 인덱스

    if r[idx] > 0:  # 값이 저장된 적이 있다면
        return r[idx]  # 해당 값을 반환

    result = p[idx]  # 초기값

    # n = 4
    # 4
    # (1, 3) (2, 2)

    for i in range(1, int(n / 2) + 1):
        j = n - i
        temp = top_down_rod_cut(p, i, r) + top_down_rod_cut(p, j, r)
        if temp > result:
            result = temp

    r[idx] = result
    return result


if __name__ == '__main__':
    p = [1,5,8,9,10,17,17,20,24,30]
    r_list: list[int] = [-1 for _ in range(10)]  # 계산 값 저장하기 위한 리스트
    print(top_down_rod_cut(p, 10, r_list))
    print("r 리스트 내용 : ", r_list)