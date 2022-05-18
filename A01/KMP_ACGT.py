from ACGT import create_union_str
from ACGT import acgt
from write_file import write_file
from KMP import create_table

#      


def iter_KMP(filename: str, P: list[str], n: int, size: int):
    """
    KMP를 일정한 크기 단위로 쪼개서 여러번 반복하는 방식.
    입력 받은 size씩 파일에서 읽어들인다.
    최대 n만큼 읽어들일 수 있다.
    n : 남은 문자 수
    """
    t_all_count = 0
    all_count = 0

    for p in P:
        in_n = n
        t_count, table = create_table(p)  # 최대 접두부 테이블
        t_all_count += t_count
        i = 0

        count = 0
        result = []

        with open(filename, 'r') as f:
            cond = True
            n_iter = 0
            while cond:
                n_read = size  # 이번에 쓰는 갯수
                if in_n - size <= 0:  # 남은 갯수가 더 적거나 같으면
                    n_read = n
                    cond = False

                in_n -= size  # 마지막 개수.

                T = f.read(n_read)
                if len(T) == 0:  # 더 이상 읽을 것이 없다면
                    break

                i, c, r = inner_KMP(T, p, table, i)
                count += c
                result.extend([n_iter * size + val for val in r])
                n_iter += 1
        all_count += count
        write_file('output(B).txt', p, result, 1000)

    return (t_all_count, all_count)

#      


def inner_KMP(T: str, P: str, table: list[int], init_i: int):
    '''
    KMP 알고리즘을 일정 단위로 끊어서 여러번 반복한다.
    i를 함께 반환한다는 특징 존재.
    '''
    len_P = len(P)  # 우리 패턴의 길이
    len_T = len(T)  # 전체 문자열의 길이

    result = []  # 결과 배열

    i = init_i  # 일치하는 길이를 의미하는 변수

    count = 0

    for j in range(0, len_T):  # j 인덱스는 T의 현재 인덱스를 의미.
        count += 1
        while i > 0 and P[i] != T[j]:
            i = table[i - 1]  # i 인덱스 바로 전까지 일치. 테이블 상 해당 위치에 저장된 위치로 이동!
            # 탈출 조건은 1 == 0 혹은 P[i] == T[j]
        if P[i] == T[j]:  # 패턴이 일치해서 탈출한 경우
            if i == len_P - 1:  # 패턴이 일치 + 거리 만족
                # j 인덱스는 패턴의 마지막 위치. 원하는 값은 패턴이 시작되는 위치.
                result.append(j - len_P + 1)
                # STRING : G의 위치는 5, 시작 위치는 0. 5 - 6 + 1 = 0으로, 시작 위치를 얻을 수 있다.
                i = table[i]
            else:
                i += 1

    return (i, count, result)  # i, count, result 반환


if __name__ == '__main__':
    # P = ["ACCGTAT"]
    # t_count, count = iter_KMP('input.txt',P, 100000, 10000)
    # print(t_count, count)

    for m in range(5, 20, 5):
        for n in [10000, 100000]:
            t_count, count = iter_KMP(
                'input.txt', create_union_str(m, acgt), n, 100000)
            print(t_count, count)
