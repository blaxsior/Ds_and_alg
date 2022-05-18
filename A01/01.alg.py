from RabinKarp import dig
from brute import brute_force
from RabinKarp import RabinKarp
from KMP import KMP

# T = 'A STRING SEARCHING EXAMPLE CONSISTING OF A GIVEN PATTERN STRING'
# # # S 총 4개
# P = 'STRING'
    
T = list(input("Test String: "))
P = list(input("Pattern String: "))
# 파이썬은 문자열을 배열처럼 접근할 수 있다. -> 1차원 배열에 저장한 것과 유사한 효과.


print(len(T))
print(brute_force(T,P))
print(RabinKarp(T,P,dig,137))
print(KMP(T,P))
