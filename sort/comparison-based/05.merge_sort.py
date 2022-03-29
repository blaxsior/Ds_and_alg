"""
@input arr : 병합 대상이 되는 배열 
@input left : 병합할 범위 첫번째 인덱스
@input right : 병합할 범위 마지막 인덱스 
@input mid : 병합할 두 범위를 나누는 기준점.
"""
def merge(arr: list[int], left: int, right: int, mid: int):
    temp_list: list[int] = []  # 두 배열에 저장된 값을 합병 및 저장할 때 사용되는 배열
    a_idx = left  # 첫번째 배열
    b_idx = mid + 1  # 두번째 배열

    if left == right:  # 원소가 하나면 계산 안함
        return

    while a_idx <= mid and b_idx <= right:  # 둘다 배열 인덱스 안에 잘 있을때
        if arr[a_idx] < arr[b_idx]:  # 첫번째 배열의 요소가 더 작을 때
            temp_list.append(arr[a_idx])
            a_idx += 1
        else:  # 두번째 배열의 요소가 더 작을 때
            temp_list.append(arr[b_idx])
            b_idx += 1

    if a_idx > mid:  # 첫번째 배열이 남지 않은 경우
        temp_list.extend(arr[b_idx:right+1])  # 두번째 배열 통째로 붙여넣기
    elif b_idx > right:  # 두번째 배열이 남지 않은 경우
        temp_list.extend(arr[a_idx:mid+1])  # 첫번째 배열 통째로 붙여넣기

    assert(len(temp_list) == (right - left + 1))
    # 새로 생기는 배열의 길이는 반드시 기존 범위와 같아야 한다.

    temp_idx = 0  # 배열 복사를 위한 인덱스
    for i in range(left, right + 1):  # merge 끝나서 배열 복사
        arr[i] = temp_list[temp_idx]
        temp_idx += 1
    print(arr)


"""
@input arr : 병합 대상이 되는 배열 
@input left : 병합할 범위 첫번째 인덱스
@input right : 병합할 범위 마지막 인덱스 
"""
def merge_sort_rec(arr: list[int], left: int, right: int):
    if left < right:  # 좌측 인덱스가 우측 인덱스보다는 작아야 의미가 있음.
        mid = int((left + right)/2)  # mid는 배열 나누는 중간 인덱스

        # 인덱스를 기준으로 양쪽의 배열에 대해 recursive 하게 sort
        merge_sort_rec(arr, left, mid)
        merge_sort_rec(arr, mid+1, right)

        merge(arr, left, right, mid)  # 양쪽 배열을 merge


"""
주요 알고리즘?
for i = 1 ; i < n ; i *= 2  
    Left = 1
    while left <= n
        right = left + 2*1 - 1 
        if right > n
            right = n
        if mid <= n
            merge(arr, left, right, mid)
        left = right + 1

@input arr 정렬 대상이 되는 배열
"""
def merge_sort(arr: list[int]):
    i : int = 1 # 두 배열이 있을 때, 한쪽 인덱스에서 mid 까지의 거리를 의미한다.
    l_idx = len(arr) - 1 # 배열의 마지막 인덱스

    # 알고리즘 작동 방식
    # 크기가 1인 배열 단위부터 시작하여
    # 점차 크기가 2의 배수인 배열을 병합하기 시작.
    # 따라서, i는 매 순간마다 2배가 됨.
    
    while i < l_idx : # i가 배열의 크기보다 작을 때 
                    # 만약 i = l_idx이면 배열이 모두 정렬된 상태이므로, 상관 X
        left = 0 # 전체 배열의 첫번째 인덱스는 0이다.
        while left <= l_idx : # 좌측 인덱스가 마지막 인덱스 이하라면
            right = left + i * 2 - 1 
            # right - left = 2i - 1 이므로, right = left + 2i - 1 이 된다.
            # left <-- i -> mid <-- i --> right의 관계를 가진다.

            if right > l_idx : # 배열의 길이를 초과하는 right가 설정되었다면,
                right = l_idx # 배열을 정상화한다.
            mid = left + i - 1 # mid의 위치는 left에서 i 만큼 떨어진 곳에 있음.
            # 0 1 2 3 | 4 5 6 7 이면, mid 는 3 이 된다. 3은 0포함 4 거리에 있음.

            if mid <= l_idx : # mid가 마지막 인덱스를 넘으면 안됨
                merge(arr, left, right, mid)
            left = right + 1 # 새로운 범위에 대해 병합을 시작한다
            # right + 1 은 병합되지 않은 새로운 범위의 시작점을 의미한다.
        i = i * 2 # 병합 범위를 2배로 키운다.

        

print("Recursive Merge Sort", '*' * 10)
arr1 = [30, 20, 40, 35, 5, 50, 45, 10, 25, 15]
print(arr1)
merge_sort_rec(arr1, 0, len(arr1)-1)

print("Nonrecursive Merge Sort", '*' * 10)
arr2 = [30, 20, 40, 35, 5, 50, 45, 10, 25, 15]
merge_sort(arr2)

# 시간 복잡도 : O(nlogn)
# 제자리성 : 입력 크기에 비례하는 행렬이 필요
# 안정성 : 가까운 2~4 ... 개의 원소끼리 정렬되므로, 안정적이다.