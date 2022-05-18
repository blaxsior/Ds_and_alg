from ACGT import create_union_str
from ACGT import acgt
from brute import brute_force
from write_file import write_file
#      


def brute_ACGT(T: str, P: list[str]):
    all_count = 0

    for p in P:
        count, loc = brute_force(T, p)  # brute force로 코드를 실행하고,
        write_file('output(A).txt', p, loc, 1000)  # 내용을 쓴다.
        all_count += count

    return all_count  # 결과 반환 + 인덱스 개수 반환


if __name__ == '__main__':
    # T = ''
    # P = ["ACCGTAT"]
    # with open('input.txt', 'r') as f:
    #     T = f.read(100000) # 10만개의 글자 읽기
    #     count = brute_ACGT(T,P) # count는 읽은 횟수
    #     print(count)

    for m in range(5, 20, 5):
        for n in [10000, 100000]:
            with open('input.txt', 'r') as f:
                T = f.read(n)  
                count = brute_ACGT(T, create_union_str(m, acgt))  # count는 읽은 횟수
                print(count)
