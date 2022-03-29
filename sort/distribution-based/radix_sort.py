"""
전체 키를 여러 자리로 나누어 각 자리마다 안정적 정렬을 적용한다.
왜 안정적 ? : 안정성이 없는 알고리즘 이용시, 이전 단계에 분류했던 것들이 섞일 수 있음!
따라서 안정성이 있는 알고리즘 (ex 삽입 정렬) 등을 각 단계에서 적용.
여기서는 정수에 대한 정렬을 수행해본다.
"""


def getDig(number: int, digit: int):
    return int(number/(10**digit)) % 10


def radix_sort_for_integer(arr: list[int]):
    result = arr.copy()
    can_exit = False

    digit = 0
    while not can_exit:
        radix = [[] for _ in range(10)]

        for val in result:
            dig_number = getDig(val, digit)
            radix[dig_number].append(val)

        result = []
        for values in radix:
            result.extend(values)
            if len(values) == len(arr):
                can_exit = True
                break
        digit += 1
    return result


arr = [567, 654, 124, 457, 830, 911, 1324, 555, 41, 32, 13, 1]
result = radix_sort_for_integer(arr)
print(result)
#시간복잡도 : O(dn) = O(n)
#제자리성 : 제자리 정렬 아님. 진법 만큼의 메모리 필요. + 추가 메모리 필요할 수도 있음.
#안정성 : 안정적. 순서대로 뒤쪽 레코드부터 뒤에 배치