nr_points = input()

polygon_points = []

for i in range(int(nr_points)):
    line = input().split(' ')
    polygon_points.append((int(line[0]), int(line[1])))

def poly_monotonic_x(poly_points):
  nr_points = len(poly_points)
  nr_local_minimums = 0

  for i in range(0, nr_points):
    predecesor_point = poly_points[i - 1]
    current_point = poly_points[i]
    succesor_point = 0
    if i + 1 < nr_points:
        succesor_point = poly_points[i+1]
    else: succesor_point = poly_points[0]

    if current_point[0] < succesor_point[0] and current_point[0] < predecesor_point[0]:
        nr_local_minimums += 1
  
  return nr_local_minimums == 1

def poly_monotonic_y(poly_points):
  nr_points = len(poly_points)
  nr_local_minimums = 0

  for i in range(0, nr_points):
    predecesor_point = poly_points[i - 1]
    current_point = poly_points[i]
    succesor_point = 0
    if i + 1 < nr_points:
        succesor_point = poly_points[i+1]
    else: succesor_point = poly_points[0]

    if current_point[1] < succesor_point[1] and current_point[1] < predecesor_point[1]:
        nr_local_minimums += 1
  
  return nr_local_minimums == 1

print("YES" if poly_monotonic_x(polygon_points) else "NO")
print("YES" if poly_monotonic_y(polygon_points) else "NO")