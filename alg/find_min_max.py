from random import sample

def getRandom1000():
    """
    sample : 주어진 sequence 에서 set 형식으로 k개만큼 뽑는다
    random : 1~ 100000 범위에서 1000 개 뽑는다!
    """
    return sample(range(1, 100001), 1000)

def Minimum(arr: list[int]):
    """
    @function Minimum
    @description 값들을 앞에서부터 차례대로 비교하면서 최소값보다 작은지 본다.
    @params arr : list
    @return minimum
    """
    minimum = arr[0] # 기본값 설정
    for val in arr: # 배열 내의 원소들에 대해
        if val < minimum : # 배열 값이 더 작으면
            minimum = val # 값을 바꾼다
    return minimum # 최소값 반환

def Maximum(arr: list[int]):
    """
    @function Maximum
    @description 값들을 앞에서부터 차례대로 비교하면서 최대값보다 큰지 본다.
    @params arr : list
    @return maximum
    """
    maximum = arr[0] # 기본값 설정
    for val in arr: # 배열 내의 원소들에 대해
        if val > maximum : # 배열 값이 더 크면
            maximum = val # 값을 바꾼다
    return maximum # 최대값 반환
    
def FindMinMax(arr: list[int]):
    """
    @function find_min_max
    @description 최대값 및 최소값을 동시에 찾기.  
    각 단계에서 2개씩 값을 비교하면서 small 및 large을 갱신한다.
    2개씩 인덱스 값이 증가한다는 점이 특징적이다!

    @return (min, max)

    @pseudo_code
    minimum = arr[0]
    maximum = arr[0]
    for i in [1, n) : step = 2  # (n-1) / 2 
        small, large = small(arr[i],arr[i+1]) , large(arr[i],arr[i+1]) # 1
        if small < minimum : # 1
            minimum = small
        if large > maximum :  # 1
            maximum = large

        return (minimum, maximum)
    """
    minimum = arr[0]
    maximum = arr[0]
    # 기본 값을 설정해둬야 오류가 안난다.

    small = 0
    large = 0

    length = len(arr)
    # 계속 변수 만들기 싫어서 선언해두었다
    for i in range(1, length, 2):
        if i + 1 < length:  # 두번째 인덱스가 배열 내에 존재하는 위치라면
            if arr[i] < arr[i + 1]:
                # min < small < large < max 관계를 비교하기 위해
                # small, large을 구한다!
                small, large = arr[i], arr[i + 1]
            else:
                small, large = arr[i + 1], arr[i]
        else:  # 첫번째 인덱스만 존재하는 상황 => 하나로 퉁치자
            small = arr[i]
            large = arr[i]

        if small < minimum:  # 현재 작은 값이 minimum보다도 작다면
            minimum = small  # 최소값을 바꾼다
        if large > maximum:  # 현재 큰 값이 maximum보다도 크다면
            maximum = large  # 최대값을 바꾼다

    return (minimum, maximum)


if __name__ == "__main__":

    test_arr1 = [1, 3, 5, 4, 7, 9, 11, 5, 8, -2]  # 최소 -2 최대 11 | 원소 10개
    test_arr2 = [1, 3, 5, 4, 7, 9, 27, 5, -2, 15, 11]  # 최소 -2 최대 27 | 원소 11개
    assert(FindMinMax(test_arr1) == (-2, 11)) # 코드에 문제가 없는지 검사
    assert(FindMinMax(test_arr2) == (-2, 27))

    rand_arr = getRandom1000()
    print(rand_arr)

    minimum, maximum = FindMinMax(rand_arr)
    print(f"Min: {minimum}")
    print(f"Max: {maximum}")
    print(f"Min : {minimum}, Max : {maximum}")
