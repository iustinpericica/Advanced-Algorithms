def determinant3Per3(a):
    return (a[0][0] * (a[1][1] * a[2][2] - a[2][1] * a[1][2])
           -a[1][0] * (a[0][1] * a[2][2] - a[2][1] * a[0][2])
           +a[2][0] * (a[0][1] * a[1][2] - a[1][1] * a[0][2]))

m = int(input())
poly = []
for i in range(m):
    p = list(map(int, input().split(' ')))
    poly.append(p)

n = int(input())
points = []
for i in range(n):
    p = list(map(int, input().split(' ')))
    points.append(p)

for point in points:
    ok = 1
    iPoly = 0
    broken = 0
    while iPoly < m - 1:
        pointA = poly[iPoly]
        pointB = poly[iPoly + 1]
        det = determinant3Per3( [ [1, 1, 1] , [pointA[0], point[0], pointB[0]] , [pointA[1], point[1], pointB[1]]] )
        if det == 0:
            print("BOUNDARY")
            broken = 1
            break
        if det > 0:
            ok = 0
        iPoly+=1

    if broken:
        continue
    
    pointA = poly[iPoly]
    pointB = poly[0]
    det = determinant3Per3( [ [1, 1, 1] , [pointA[0], point[0], pointB[0]] , [pointA[1], point[1], pointB[1]]] )
    if det == 0:
        print("BOUNDARY")
        continue
    if det > 0:
        ok = 0

    if ok:
        print("INSIDE")
    else:
        print("OUTSIDE")