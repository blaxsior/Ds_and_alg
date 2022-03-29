# 0~n-1 까지
# 부모는 int((n-1)/2)
# 자식은 왼 + 1 오 + 2

# 배열에 원소를 하나씩 삽입하면서 만드는 방식
def make_heap1(arr: list[int]):
    for i in range(1, len(arr)):
        child = i
        while child > 0:
            parent = int((child - 1) / 2)
            if(arr[parent] < arr[child]):
                arr[parent], arr[child] = arr[child], arr[parent]
                child = parent
            else:
                break
        print(arr)

# 스왑하는 함수.


def swap_if(arr: list[int], x: int, y: int):
    if arr[x] < arr[y]:
        arr[x], arr[y] = arr[y], arr[x]
        return y
    else:
        return x


"""
@input arr 대상 리스트
@input idx 현재 정렬 대상인 부모 노드

자식의 위치 :
    left  : 2n + 1 (0 - 1)
    right : 2n + 2 (0 - 2)

    자식이 더 크면 자식 노드 반환
    부모가 더 크면 부모 노드 반환.
"""


def small_term_sort(arr: list[int], parent: int, last: int):
    lc = 2 * parent + 1
    rc = 2 * parent + 2

    if rc <= last:  # lc 및 rc가 모두 존재할 때
        target = lc + int(arr[lc] < arr[rc])
        # 더 큰 자식 노드를 선택하는 과정.
        # lc가 더 크거나 같으면 0이 되고,
        # rc가 더 크면 1이 됨.
        # lc 와 rc 사이의 인덱스 차이는 1이다.
        return swap_if(arr, parent, target)
    elif lc <= last:  # rc 는 last 보다 크고, lc는 last 이하. 즉 lc = last인 상황을 의미
        return swap_if(arr, parent, lc)
    else:  # 자식 노드 없음
        return parent
# 존재하는 배열을 마지막 원소부터 차례대로 정렬하는 방식.

# idx 위치부터 거슬러가며 배열 정렬 시도
# target을 찾는 마지막 위치는 last
def successive_pc_sort(arr:list[int], idx: int, last: int):
    parent = idx
    target = small_term_sort(arr, idx, last)
    while parent != target: # 정렬이 발생했다면
        parent = target # 자식 노드로 가서
        target = small_term_sort(arr, parent, last) #자식노드 선에서 정렬한다.


def make_heap2(arr: list[int]):
    last = len(arr) - 1
    for i in range(len(arr) - 1, -1, -1):
        successive_pc_sort(arr, i, last)
        print(arr)

# 실제로 힙을 정렬하는 코드.
def heap_sort(arr: list[int]):
    # i는 정렬 안된 배열의 마지막 인덱스
    for i in range(len(arr) - 1, 0, -1): 
        arr[0], arr[i] = arr[i], arr[0]
        print(arr)
        successive_pc_sort(arr, 0, i - 1) 
        # 마지막 값은 이미 정렬된 상태임!

arr1 = [30, 10, 50, 60, 20, 70, 80]

print("Make Heap 1")
make_heap1(arr1)
print(arr1)

print("heap_sort")
heap_sort(arr1)
print(arr1)

arr2 = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]

print("Make Heap 2")
make_heap2(arr2)
print("heap_sort")
print(arr2)
heap_sort(arr2)
print(arr2)

# 시간 복잡도 : 최악 O(nlogn)
# 제자리성 : 상수 크기의 메모리만 사용. 따로 배열에 비례하는 공간 필요 없음.
# 안정성 : 정렬의 띄어띄어 발생하므로, 불안정하다.