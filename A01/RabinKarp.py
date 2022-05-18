#      
from typing import Callable


def dig(ch: str):
    # 알파벳 대문자를 받아 26진법 숫자로 취급... 0~25 사이의 값이 나온다.
    if ch.isalpha():
        return ord(ch) - ord('A')
    if ch == ' ':  # 공백문자면
        return 26  # 26으로 취급


def get27(input: str, n, start=0):
    # 값을 26진수 값을 10진수로 바꿈.
    # start : 계산할 위치.
    result = 0
    for i in range(0, n):
        result += dig(input[i+start]) * 27 ** (n - i - 1)
        # 각 값 더하기.
    return result
    # 결과값 반환.

#      


def RabinKarp(T: str, P: str, dig: Callable[[str], int], q=29, d=10):
    # q : 해시 값
    n = len(T)  # 문자열 길이
    m = len(P)  # 패턴 길이

    count = 0  # 비교 횟수

    result = []  # 결과 위치를 저장하는 배열

    D = (d ** (m - 1)) % q  # 미리 계산해둔 최대차항의 값.

    h = 0 # P를 d진수로 변환한 값
    t = 0 # T 내의 부분 문자열을 d진수로 변환한 값

    for i in range(m):
        h = (d * h + dig(P[i])) % q
        t = (d * t + dig(T[i])) % q
    # 초기 값을 설정한다.
# 2...

    for i in range(n - m + 1):
        count += 1  # 해시 값 검사
        if h == t:  # 해시 값이 같을 때 문자열 직접 비교
            cond = True
            for j in range(0, m):  # 패턴 검사
                count += 1
                if P[j] != T[j+i]:
                    cond = False  # 패턴이 아님
                    break
            if cond:  # 패턴에 맞으면
                result.append(i)  # 배열에 삽입
        if i < n - m:  # i 가 범위 내에 있다면
            t = (d*(t-dig(T[i])*D) + dig(T[i+m])) % q  # 다음 값 계산 위해 점화식 ...
            # 맨 앞값 빼고 맨 뒤값 구함.
    return (count, result)
