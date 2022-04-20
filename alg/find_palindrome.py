"""
@input str 검사 대상이 되는 문장

비순환적 회문 알고리즘.
회문 알고리즘 조건

- 한글자만 적혀있는 파일은 회문이 안되게 작성

- 문장 안에 한글자가 적혀있는 경우는 회문이 될 수 있음

- 회문 판별 조건에 공백도 포함

- 대소문자 구별은 안해도 됨(하고 싶은 분은 하셔도 됩니다.)

- 특수문자는 회문에 포함 하지 말 것(eye?이면 회문이라고 나오도록 구현해주세요)

- 특수문자가 들어간다면 단어나 문장 끝에만 넣기

유사 코드:
@function   is_palindrome
@input  in_str : string
@return whether in_str is palindrome

if length(in_str) <= 1:
    return false

to_lower_case(in_str)

left = 0
right = last_idx(in_str)

while left <= right :
    while (in_str[left] is not alnum | in_str[left] is not ' ') & left < last_idx(in_str) :
        left += 1
    while (in_str[right] is not alnum | in_str[right] is not ' ') & right > -1 :
        right -= 1

    if in_str[left] != in_str[right]:
        return false

    left += 1
    right -= 1
return true
"""



def is_palindrome(in_str: str):
    if(len(in_str) <= 1):
        # 한글자라면
        return False
    in_str = in_str.lower()  # 대소문자를 구분하지 않기 위해 소문자로 일괄 변경한다.

    left = 0  # 좌측에서 검사 대상 인덱스
    right = len(in_str) - 1  # 우측에서 검사 대상 인덱스
    last = len(in_str)  # 인덱스 끝을 가리키기 위한 값

    while left <= right:  # 좌측과 우측이 교차하지 않을 때 -> 다 본게 아닐 때
        while not (in_str[left].isalnum() or in_str[left] == ' ' ) and left < last:
            # left가 가리키는 문자가 영문자 혹은 숫자 혹은 공백이 아니라면
            # 배열을 넘어선게 아니라면
            left += 1
        while not (in_str[right].isalnum() or in_str[right] == ' ' ) and right > -1:
            right -= 1
            # right가 가리키는 문자가 영문자 혹은 숫자 혹은 공백이 아니라면
            # 배열을 넘어선게 아니라면

        if in_str[left] != in_str[right]:  # 찾은 문자가 다르면 회문이 아님.
            return False
        # 다음 문자부터 다시 검사한다.
        left += 1
        right -= 1
    return True  # 끝까지 검사해서 살아남았다면 회문이다.


"""
@input str 검사 대상이 되는 문장
@input left 검사를 시작하는 좌측 인덱스
@input right 검사를 시작하는 우측 인덱스

순환적 회문 알고리즘.
회문 알고리즘 조건

- 한글자만 적혀있는 파일은 회문이 안되게 작성

- 문장 안에 한글자가 적혀있는 경우는 회문이 될 수 있음

- 회문 판별 조건에 공백도 포함

- 대소문자 구별은 안해도 됨(하고 싶은 분은 하셔도 됩니다.)

- 특수문자는 회문에 포함 하지 말 것(eye?이면 회문이라고 나오도록 구현해주세요)

- 특수문자가 들어간다면 단어나 문장 끝에만 넣기

유사 코드:

@function   is_palindrome_rec
@input  in_str : string
@input left
@input right
@return whether is_str[left] and is_str[right] are same

if length(in_str) <= 1:
    return false

if left <= right :
    while (in_str[left] is not alnum | in_str[left] is not ' ') & left < last_idx(in_str) :
        left += 1
    while (in_str[right] is not alnum | in_str[right] is not ' ') & right > -1 :
        right -= 1

    change in_str[left] and in_str[right] to lower case

    if in_str[left] != in_str[right]:
        return false
    else:
        return is_palindrome_rec(in_str, left + 1, right + 1)
else :
    return true
"""


def is_palindrome_rec(in_str: str, left: int, right: int):
    if(len(in_str) <= 1):
        # 한글자라면
        return False

    while left <= right: # 좌측과 우측이 교차하지 않을 때 -> 다 본게 아닐 때
        while not (in_str[left].isalnum() or in_str[left] == ' ' ) and left < len(in_str): 
            # left가 가리키는 문자가 영문자 혹은 숫자 혹은 공백이 아니라면
            # 배열을 넘어선게 아니라면
            left += 1
        while not (in_str[right].isalnum() or in_str[right] == ' ' ) and right > -1:
            right -= 1
            # right가 가리키는 문자가 영문자 혹은 숫자 혹은 공백이 아니라면
            # 배열을 넘어선게 아니라면

        if in_str[left].lower() != in_str[right].lower(): #찾은 문자가 다르면 회문이 아님.
            return False
        else :
            return is_palindrome_rec(in_str, left + 1, right - 1)

    return True # 끝까지 검사해서 살아남았다면 회문이다.



"""
회문이 담긴 파일.

"""
file_name = 'palindrome.txt'

# 파일에서 문자열 읽어들이는 과정
with open(file_name, 'r', encoding='utf-8') as f:
    print("This is Recursive")
    idx = 0 # 현재 라인 번호
    line = None # 현재 읽고 있는 문장
    while True:
        line = f.readline()
        
        if not line : # 파일이 끝에 도달? 그만 읽기
            break
        my_line = line.rstrip('\n') #문장에서 엔터는 제거 : 엔터는 문장에 포함 안된다.
        idx += 1
        # palindrome = is_palindrome(my_line)
        palindrome = is_palindrome_rec(my_line, 0, len(my_line) - 1)
        print(f"[{idx}]string : {my_line}")
        print(f"[{idx}]is palindrome? : {palindrome}")
        print()