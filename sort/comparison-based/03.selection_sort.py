def selection_sort(array: list[any]):
    for i in range(len(array) - 1):
        changed = False
        min_idx: int = i
        for j in range(i+1, len(array)):
            if (array[min_idx] > array[j]):
                min_idx = j
                changed = True
        array[i], array[min_idx] = array[min_idx], array[i]
        print(array, changed, sep=',')  # 주석 출력 단계. 필요 없으면 삭제.
        if changed == False:
            break
    return array


arr0 = [20, 30, 10, 5, 10, 30, 15, 40]

print(selection_sort(arr0))