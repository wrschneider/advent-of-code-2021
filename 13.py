input = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5""".split("\n")

input = [s.strip() for s in open("13.txt").readlines()]

points = set()

def fold(points, instr):
    new_points = set()
    axis, value_str = instr.split("=")
    value = int(value_str)

    for point in points:
        if axis == "x" and point[0] < value:
            new_points.add(point)
        elif axis == "y" and point[1] < value:
            new_points.add(point)
        elif axis == "x":
            new_points.add((value - (point[0] - value), point[1]))
        elif axis == "y":
            new_points.add((point[0], value - (point[1] - value)))
    return new_points
    
for line in input:
    if line and not line.startswith("fold"):
        points.add(tuple(int(x) for x in line.split(",")))
    elif line.startswith("fold"):
        instr = line.split(" ")[-1]
        points = fold(points, instr)

print(points)

grid = []
for y in range(40):
    grid.append(list(" " * 40))

for point in points:
    print(point)
    grid[point[1]][point[0]] = "*"

for s in grid:
    print("".join(s))




