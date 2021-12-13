from collections import defaultdict

input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""".split("\n")

input = [s.strip() for s in open("05.txt").readlines()]
parsed = [[point.split(",") for point in line.split(" -> ")] for line in input]

point_counter = defaultdict(int)

# inclusive range either direction
def irange(start, end):
   if start > end:
       start, end = end, start # swap
   return range(start, end+1)

for line in parsed:
    start = (int(line[0][0]), int(line[0][1]))
    end = (int(line[1][0]), int(line[1][1]))
    if (start[0] == end[0]): # first coord equal, vertical
        for j in irange(start[1], end[1]):
            point_counter[(start[0], j)] += 1

    elif (start[1] == end[1]): # second coord equal, horizontal
        for i in irange(start[0], end[0]):
            point_counter[(i, start[1])] += 1
   
    else: # assume diagonal
        offset = abs(end[0] - start[0])
        x_direction = (end[0] - start[0])//offset
        y_direction = (end[1] - start[1])//offset
        for i in range(offset+1):
            point_counter[(start[0] + i*x_direction, start[1] + i*y_direction)] += 1
            

# print(point_counter)

print(sum(1 for point in point_counter if point_counter[point] >= 2))
