    
def write_file(filename: str, name: str, arr: list[int], k: int, d = ','):
    n = len(arr)
    with open(filename, 'a+') as f:
        f.write(f'{name} : \n')
        for i in range(0,n,k): #k개 단위로 쪼개서 작성
            last = min(i + k, n) #마지막 인덱스와 100개 더한 값을 비교
            text = d.join([f'{x}' for x in arr[i:last]])
            text = text + d # comma 하나 추가
            f.write(text)
        f.write('\n')