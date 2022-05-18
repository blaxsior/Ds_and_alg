class Point:
    '''
    점을 의미하는 클래스
    '''
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class Line:
    '''
    선을 의미하는 클래스
    '''
    def __init__(self, l: Point, r: Point):
        '''
          l, r 선의 양쪽 점
        '''
        self.l = l
        self.r = r


def direction(a: Point, b: Point, c: Point):
    '''
    a, b, c 점이 어떤 관계를 가지고 있는지 검사.
    '''
    # ab의 변위
    dxAB = b.x - a.x
    dyAB = b.y - a.y

    # ac의 변위
    dxAC = c.x - a.x
    dyAC = c.y - a.y

    direction = 0
    '''
    1 : 시계방향
    -1 : 반시계
    0 : 일직선
    '''

    if dxAB * dyAC < dyAB * dxAC:  # 시계 방향에 있는 경우
        print('dAB > dAC, 시계방향')
        direction = 1  # 시계방향에 위치
    if dxAB * dyAC > dyAB * dxAC:  # 반시계 방향에 있는 경우
        print('dAB < dAC, 반시계방향')
        direction = -1  # 반시계방향에 위치
    if dxAB * dyAC == dyAB * dxAC:  # 동일선상에 있는 경우
        if dxAB == 0 and dyAB == 0:  # A = B로 점인 경우
            print('A = B')
            direction = 0  # AC는 그냥 직선
        if dxAB * dxAC < 0 or dyAB * dyAC < 0:  # A가 가운데인 경우
            print('A가 중간')
            direction = -1
        elif dxAB**2 + dyAB**2 >= dxAC**2 + dyAC**2:  # 피타고라스 정리를 이용
            # C가 가운데에 있는 경우
            print('C가 중간')
            direction = 0
        else:  # B가 가운데에 있는 경우
            print('B가 중간')
            direction = 1
    return direction


def intersection(ab: Line, cd: Line):
    '''
    현재 두 선이 교차했는지 여부를 알려주는 알고리즘.
    '''
    cross: bool  # 현재 두 선이 교차했는지 여부.

    # AB 입장에서 CD가 양쪽에 있는지
    cross_AB_CD = direction(ab.l, ab.r, cd.l) * direction(ab.l, ab.r, cd.r) 

    # CD 입장에서 AB가 양쪽에 있는지
    cross_CD_AB = direction(cd.l, cd.r, ab.l) * direction(cd.l, cd.r, ab.r)
    if cross_AB_CD<= 0 and cross_CD_AB <= 0:
        # ab 입장에서 cd 점이 양쪽에 존재하고,
        # cd 입장에서 ab 점이 양쪽에 존재할 때 선은 교차한다고 볼 수 있다.
        cross = True
    else:
        cross = False

    return cross

if __name__ == '__main__':
    line_data : list[list[tuple[int,int]]] = [
        [(2, 1), (-1, 3), (-1, 1), (2, 3)],
        [(-3, 0), (1, 1), (-4, 1), (-6, 3)],
        [(-2.2, 0), (0, 3.3), (-1, 4), (-0.5, -2.3)]
    ]

    for data in line_data: # 데이터들에 대해 연산

        points : list[Point] = [] # 점들
        for (x,y) in data: # 현재 데이터에 대해 점 생성
            p = Point(x,y) # 점 클래스
            points.append(p) # 점 넣기
        lineAB = Line(points[0], points[1]) # AB 생성
        lineCD = Line(points[2], points[3]) # CD 생성

        print("교차 여부 : ", end='')
        for p in points:
            print(f'({p.x}, {p.y}) ', end='')
        print()
        print(intersection(lineAB, lineCD))

        x = 10 + 10
        y = 20 + 20
        
        z = 10 / 0
