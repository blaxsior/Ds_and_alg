from __future__ import annotations
from collections import deque
from typing import TypeVar

T = TypeVar('T')

class RBNode:
    left : RBNode
    right : RBNode
    parent : RBNode
    
    color : bool # True를 적색으로 취급

    value : T

    def __init__(self, value: T, color : bool = True):
        self.value = value
        self.color = color
        # 기본적으로 적색

class RBTree:
    '''
    다음 조건을 만족하는 "이진 검색 트리"
    1. 모든 노드는 적색이거나 흑색이다.
    2. 루트는 흑색이다.
    3. 모든 리프(NIL)은 흑색이다.
    4. 노드가 적색이면 노드의 자식은 모두 흑색이다.
    5. 각 노드로부터 그 노드의 자손인 리프로 가는 경로는 모두 같은 흑색 노드 수를 가진다.
    - 최대 2log(n+1) 의 높이를 가지는 것으로 알려져 있다.
    '''
    root : RBNode
    NIL : RBNode

    def __init__(self):
        self.NIL = RBNode(None, False) # 아무 값도 없는 검정색 노드
        self.root = self.NIL # 맨 처음에는 헤드 노드도 없다.

    def left_rotate(self, x: RBNode):
        # 초기 설정
        y = x.right
        
        # x와 y의 좌측 자식을 연결
        x.right = y.left
        if y.left != self.NIL: # y의 좌측 자식이 null인 경우는 부모 설정 안해도 됨.
            y.left.parent = x
        y.parent = x.parent
        
        #x의 부모를 y에게 연결한다.
        if x.parent == self.NIL : # x가 부모가 없다면 = 루트노드라면
            self.root = y

        elif x.parent.left == x : # x가 부모의 왼쪽 자식이라면
            x.parent.left = y
        else: # x가 부모의 오른쪽 자식인 경우
            x.parent.right = y

        # x 와 y를 연결
        y.left = x
        x.parent = y

    def right_rotate(self, x: RBNode):
        # 초기 설정
        y = x.left

        x.left = y.right
        if y.right != self.NIL: # y.right가 존재한다면
            y.right.parent = x # x와 연결
        y.parent = x.parent

        #x의 부모를 y에게 연결한다.
        if x.parent == self.NIL : # x가 부모가 없다면 = 루트노드라면
            self.root = y

        elif x.parent.left == x : # x가 부모의 왼쪽 자식이라면
            x.parent.left = y
        else: # x가 부모의 오른쪽 자식인 경우
            x.parent.right = y

        # x 와 y를 연결
        y.right = x
        x.parent = y
    def insert_fixup(self, z: RBNode):
        '''
        삽입 과정에서 발생하는 문제를 해결
        - (0). 루트인 경우
            - 검정으로 칠한다.
        - (1). z의 부모와 삼촌이 적색
            - 부모 삼촌 색 검정으로 바꾸고 조부모 색 빨강 + 과정 반복
        - (2). z의 부모가 적색 삼촌이 흑색, z는 오른쪽 자식
            - z에 대해 left rotate 적용 후 (3)
        - (3). z의 부모 적색 삼촌 흑색, z는 왼쪽 자식
            - 부모에 대해 right rotate 적용 후 자식 삼촌 색 빨강, 자기는 검정
        '''
        while z.parent.color == True: # 부모가 적색이고, NIL이 아닐 때
            #(1) 번째 경우 :  
            if z.parent == z.parent.parent.left: # 부모가 왼쪽 자식이면
                uncle = z.parent.parent.right # 삼촌 노드는 오른쪽
                
                if uncle.color == True: # 삼촌의 색도 적색이면
                    z.parent.color = False # 부모의 색 검정으로
                    uncle.color = False # 삼촌 색 검정으로
                    z.parent.parent.color = True # 조부모의 색은 빨강으로
                    z = z.parent.parent # 조부모에 대해 다시 해당 과정 반복
                # (2) 삼촌은 검정이고, 자기는 오른쪽 자식인 경우
                else:
                    if z == z.parent.right : 
                        z = z.parent # 자신을 부모로 바꾸고,
                        self.left_rotate(z) # left rotate 수행
                        # (3)
                    z.parent.color = False # 부모의 색은 검정
                    z.parent.parent.color = True # 조부모의 색은 빨강 
                    self.right_rotate(z.parent.parent)# 조부모에 대해 right rotate
            # 위 상황과 대칭되는 모습을 보임.
            elif z.parent == z.parent.parent.right: # 부모가 왼쪽 자식이라면
                uncle = z.parent.parent.left

                if uncle.color == True: # 삼촌의 색도 적색이면
                    z.parent.color = False # 부모의 색 검정으로
                    uncle.color = False # 삼촌 색 검정으로
                    z.parent.parent.color = True # 조부모의 색은 빨강으로
                    z = z.parent.parent # 조부모에 대해 다시 해당 과정 반복
                # (2) 삼촌은 검정이고, 자기는 왼쪽 자식인 경우
                else:
                    if z == z.parent.left : 
                        z = z.parent # 자신을 부모로 바꾸고,
                        self.right_rotate(z) # right rotate 수행
                # (3)
                z.parent.color = False # 부모의 색은 검정
                z.parent.parent.color = True # 조부모의 색은 빨강 
                self.left_rotate(z.parent.parent)# 조부모에 대해 left rotate

        self.root.color = False # 루트 노드의 색을 검정으로 칠하고 마무리.

    def insert(self, z: RBNode):
        # 삽입 과정에서 2가지 문제점이 발생 가능
        '''
        @problem
        - (2). 루트는 흑색이다.
            - 집어넣는 위치가 루트면 적색 루트가 될 수 있음
        - (4). 노드가 적색이면 노드의 자식은 모두 흑색이다.
            - 적색 노드 자식으로 삽입하면 보장되지 않음 
        -위 문제점을 해결하기 위해 fix_up 작업이 필요하다!
        '''
        y = self.NIL
        x = self.root

        while x!= self.NIL: # 노드가 비지 않았을 때
            y = x
            if z.value < x.value: # 노드 탐색 과정. 현재 값과 비교하면서 목적지를 찾는다.
                x = x.left
            else:
                x = x.right
        z.parent = y # 목적지 찾으면 z가 y를 부모로 가지도록 만든다.

        if y == self.NIL: # 조건 상 y = NIL 인 경우는 루트조차 비어있는 경우.
            self.root = z # 루트 채우기
        elif z.value < y.value: # z가 더 작으면
            y.left = z # z는 y의 좌측 노드에 삽입
        else : 
            y.right = z # z가 크거나 같으면 우측 자식에 삽입
        
        z.left = self.NIL
        z.right = self.NIL # 값 초기화
        # 컬러 정보는 노드 만드는 순간 적색으로 초기화 되므로 무시한다.
        self.insert_fixup(z)

    def print_tree(self):
        root = self.root
        
        deq = deque() # 큐 자료구조
        deq.append(root)

        count = 1 # 노드 번호
        p = 1 # 2의 배수 감지

        while len(deq) > 0: # 큐가 비지 않았다면
            node : RBNode = deq.popleft() # 큐에서 뺀다
            #자식들 큐에 넣기
            if node != self.NIL:
                deq.append(node.left)
                deq.append(node.right)
            if count == 2**p:
                print()
                p += 1
            print(f'({node.value},{"R" if node.color == True else "B"})', end=' ')
            count += 1 # count 에 1 더함
        print('\n\n') # 마지막에 엔터