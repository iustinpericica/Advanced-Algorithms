import math

def determinant3Per3(a):
    return (a[0][0] * (a[1][1] * a[2][2] - a[2][1] * a[1][2])
           -a[1][0] * (a[0][1] * a[2][2] - a[2][1] * a[0][2])
           +a[2][0] * (a[0][1] * a[1][2] - a[1][1] * a[0][2]))


def left_most_index_point(points):
    min = 0
    for i in range(1,len(points)):
        if points[i][0] < points[min][0]:
            min = i
        elif points[i][0] == points[min][0]:
            if points[i][1] > points[min][1]:
                min = i
    return min

def convexHull(points, n):
     
    if n < 3:
        return points
 
    l = left_most_index_point(points)
 
    hull = []
    q = 0
    p = l

    while(True):
         
        hull.append(p)
        q = (p + 1) % n
 
        for i in range(n):
             
            o = determinant3Per3( [ [1, 1, 1] , [points[p][0], points[i][0], points[q][0]] , [points[p][1], points[i][1], points[q][1]]])
            if o > 0 or (o == 0 and math.dist(points[i], points[p]) > math.dist(points[q], points[p])):
                q = i

        p = q
        if(p == l):
            break
 
    return hull

n = int(input())
points = []
for i in range(n):
    p = list(map(int, input().split(' ')))
    points.append(p)

convexPoints = convexHull(points, n)

print(len(convexPoints))
for each in convexPoints:
    print(points[each][0], points[each][1])