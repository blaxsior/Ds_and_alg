def insertion_sort(array: list[any]):
    for i in range(1, len(array)):
        target = array[i]  # 현재 array[i]에 있는, 비교 대상이 되는 값.
        # idx = i - 1
        # while idx >= 0 and target < array[idx]:
        #     array[idx + 1] = array[idx]
        #     idx -= 1
        # array[idx + 1] = target
        for idx in range(i - 1, -1, -1):
            if (target < array[idx]):
                array[idx + 1] = array[idx]
            else:
                array[idx + 1] = target
                break

            if idx == 0:
                array[0] = target
        print(array)
    return array


arr2 = [20, 30, 10, 5, 10, 30, 15, 40]
print(insertion_sort(arr2))
print(arr2)
