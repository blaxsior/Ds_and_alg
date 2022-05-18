from functools import reduce

"""
키 값이 0~1 사이에 균일하게 분포한다고 가정, 하나의 버킷에 하나의 키만 들어있을 확률이 높다.

"""

"""
@input insertion_sort을 통해 
"""
def by_insertion_sort(arr: list[float], value: float):
    insert_idx = len(arr) - 1

    while insert_idx >= 0 : 
        if arr[insert_idx] <= value:
            break
        insert_idx -= 1
    insert_idx += 1
    if insert_idx == len(arr) : 
        # 가장 큰 원소라면 값을 추가
        arr.append(value)
    else: # 아니면 값을 특정 인덱스 자리에 삽입
        arr.insert(insert_idx, value)

    #리스트의 insert 함수는 지정된 인덱스 "앞에" 값을 넣는다.

def bucket_sort(arr: list[float]):
    bucket = [[] for _ in range(10)] #데이터가 담길 버킷

    for val in arr :  # arr에 담긴 값들에 대해
        idx = int(val * 10) # 값에 대한 "내림" 인덱스를 적용한다.
        by_insertion_sort(bucket[idx], val)
    print(bucket)
    result = []

    for temp in bucket:
        result.extend(temp)
    return result

arr = [0.86, 0.32, 0.27, 0.12, 0.49, 0.21, 0.62, 0.89, 0.71, 0.87]

arr = bucket_sort(arr)
print(arr)


