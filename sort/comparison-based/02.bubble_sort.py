def bubble_sort(array: list[any]):
    for i in range(len(array) - 1, -1, -1):
        # 배열 길이 -> len(arr) 일때
        # 인덱스 범위는 0 ~ len(arr) - 1
        # 값은 idx ~ idx + 1 씩 비교하므로, 마지막 인덱스는 값을 비교하는 대상이 없음.
        # 따라서, 마지막 인덱스 이전까지 항상 비교.
        # 범위는 len(arr) - 2 ~ 0 까지
        # 이때, 파이썬 range 는 stop index 바로 이전 인덱스까지 iterate 수행
        # 그러므로 0 인덱스까지 보려면 -1 에서 값이 멈춰야 함.
        changed = False
        for j in range(0, i):
            # i의 범위는 0~n-2 로, 각 단계의 마지막 원소는 포함하지 않는다.
            if(array[j] > array[j+1]):  # 버블정렬 : 다음원소가 더 크면 앞과 자리 교체
                array[j], array[j+1] = array[j+1], array[j]
                changed = True
        print(array, changed, sep=', ')  # 알고리즘 내용을 볼 필요 없다면 주석 처리.
        if changed == False:
            break
    return array


arr1 = [20, 30, 10, 5, 10, 30, 15, 40]

print(bubble_sort(arr1))