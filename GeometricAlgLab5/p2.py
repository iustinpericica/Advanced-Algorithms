def determinant3Per3(a):
    return (a[0][0] * (a[1][1] * a[2][2] - a[2][1] * a[1][2])
           -a[1][0] * (a[0][1] * a[2][2] - a[2][1] * a[0][2])
           +a[2][0] * (a[0][1] * a[1][2] - a[1][1] * a[0][2]))

n = int(input())
p1 = list(map(int, input().split(' ')))
p1prim = [i for i in p1]
p2 = list(map(int, input().split(' ')))

left = right = equal = 0

for i in range(n-2):
    p3 = list(map(int, input().split(' ')))
    det = determinant3Per3( [ [1, 1, 1] , [p1[0], p2[0], p3[0]] , [p1[1], p2[1], p3[1]] ] )
    if det > 0:
        left+=1
    elif det < 0:
        right+=1
    else:
        equal+=1
    p1 = p2
    p2 = p3

det = determinant3Per3( [ [1, 1, 1] , [p1[0], p2[0], p1prim[0]] , [p1[1], p2[1], p1prim[1]] ] )
if det > 0:
   left+=1
elif det < 0:
    right+=1
else:
    equal+=1

print(str(left) + " " + str(right) + " " + str(equal))