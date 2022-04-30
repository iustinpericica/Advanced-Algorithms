# 1. (0,5p) Implementati / utilizati testul de orientare.

# Input. Trei puncte P = (xP , yP ), Q = (xQ, yQ), R = (xR, yR) (ˆın aceasta ordine) din R
# 2.
# Output. Programul afiseaza natura virajului P QR (viraj la stanga, viraj la
# dreapta, puncte coliniare).

# https://stackoverflow.com/a/9455334/9574340
def determinant3Per3(a):
    return (a[0][0] * (a[1][1] * a[2][2] - a[2][1] * a[1][2])
           -a[1][0] * (a[0][1] * a[2][2] - a[2][1] * a[0][2])
           +a[2][0] * (a[0][1] * a[1][2] - a[1][1] * a[0][2]))

n = int(input())
for i in range(n):
    line = list(map(int, input().split(' ')))
    det = determinant3Per3( [ [1, 1, 1] , [line[0], line[2], line[4]] , [line[1], line[3], line[5]] ] )
    if det > 0:
        print("LEFT")
    elif det < 0:
        print("RIGHT")
    else:
        print("TOUCH")