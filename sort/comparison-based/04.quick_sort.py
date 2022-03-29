from collections import namedtuple
from queue import SimpleQueue
from random import sample


def get_rand():
    # 1 ~ 1000000 사이의 값 중 10개를 뽑는다.
    return sample(range(1, 1000001), 10)


"""
@input arr : 대상 리스트
@input s_idx : 분할된 시작 인덱스
@input l_idx : 분할된 끝 인덱스

@return 피벗과 교환될 값.
"""
def partition(arr: list[int], s_idx: int, l_idx: int):
    pivot_value = arr[s_idx]
    pivot = s_idx  # 정렬 기준이 되는 값의 인덱스.

    left = s_idx + 1  # 피벗 자체는 정렬 대상이 아니므로, 1 더함
    right = l_idx # 제일 우측 배열 요소

    while True:
        while left < l_idx and arr[left] < pivot_value: 
            # left가 배열 범위 안에 있음 + pivot_value보다 큰 값 탐색
            # print("[Left]: ", arr[left])
            left += 1
        while right > s_idx and arr[right] > pivot_value:
             # right가 배열 범위 안에 있음 + pivot_value보다 작은 값 탐색 
            # print("[Right]: ", arr[right])
            right -= 1
        if (left < right): # left < right라 배열 순서상 교환할 수 있다면,
            arr[left], arr[right] = arr[right], arr[left] # 큰 값과 작은 값의 위치를 교환한다.
            print("\t[Swapped] : ", arr, arr[left], arr[right])  # 주석
            left += 1
            right -= 1  # swap 거쳤으므로 고려하지 않음
        else:
            break 
            # left >= right이면, 서로 교환할 대상이 없고, 모든 원소를 이미 탐색함 -> while문 탈출
    
    arr[pivot] = arr[right] # 피벗값과 right에 저장된 값을 서로 교환함
    arr[right] = pivot_value

    print("\t[Result] : ", arr)  # 주석

    return right # 현재 배열을 두 배열로 구분할 인덱스 반환


"""
비순환적 퀵 정렬 알고리즘.
큐에 인덱스를 저장한다.
quick_sort 자체는 한번만 실행된다!

@input arr 정렬의 대상이 되는 배열

"""
def quick_sort(arr: list[int]):
    # 이름을 가진 튜플. 값을 left, right로 접근 가능해진다.
    Idx = namedtuple('Idx', ['left', 'right']) # left,right 요소를 가지는 튜플을 만든다.

    idx_queue: SimpleQueue[Idx] = SimpleQueue()  # 인덱스를 관리하는 큐.
    idx_queue.put(Idx(0, len(arr) - 1)) # 맨 처음 시점에 전체 배열을 sort 대상으로 넣는다

    while not idx_queue.empty(): # 큐가 텅 빈게 아니면 (아직 정렬 대상이 남았다면)
        left, right = idx_queue.get() # 큐에서 튜플 뽑아온다. 
        if left < right : # 배열의 길이가 1 이상이라면 -> 정렬할 게 있다면
            print(f"[partition for {left} {right}]")
            idx = partition(arr, left, right) # partition 함수를 이용하여 전체 배열을 분할 & sort

            idx_queue.put(Idx(left, idx - 1)) # 큐에 좌측 배열 인덱스 넣음.
            idx_queue.put(Idx(idx+1, right)) # 큐에 우측 배열 인덱스 넣음.


"""
순환적 퀵 정렬 알고리즘.
첫번째 값이 인덱스가 된다.

@input arr : 정렬 대상이 되는 배열
@input s_idx : 정렬의 시작 인덱스
@input l_idx : 정렬의 끝 인덱스
"""
def quick_sort_rec(arr: list[int], s_idx, l_idx):
    if s_idx < l_idx:
        print(f"[partition for {s_idx} {l_idx}]")
        idx = partition(arr, s_idx, l_idx)  # 피벗 인덱스는 교환 대상이 아니다!
        quick_sort_rec(arr, s_idx, idx - 1)  # 정렬된 원소 기준 왼쪽 정렬
        quick_sort_rec(arr, idx + 1, l_idx)  # 정렬된 원소 기준 오른쪽 정렬


arr1 = get_rand()
print(arr1)
quick_sort_rec(arr1, 0, len(arr1) - 1)
print(arr1)

arr2 = get_rand()
print(arr2)
quick_sort(arr2)
print(arr2)
