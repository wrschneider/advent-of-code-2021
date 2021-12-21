import re

input = "target area: x=20..30, y=-10..-5"
input = "target area: x=137..171, y=-98..-73"

pattern = re.compile(r"target area: x=(.*)\.\.(.*), y=(.*)\.\.(.*)")
# target range 
x1, x2, y1, y2 = tuple(int(x) for x in pattern.match(input).groups())

def step(x, y, vx, vy):
    newx = x + vx
    newy = y + vy
    if vx > 0:
        vx -= 1
    vy -= 1
    return newx, newy, vx, vy

def in_target(x, y):
    if x >= x1 and x <= x2 and y >= y1 and y <= y2: return True
    return False

# overshoot = x > x2
# undershoot = x < x1 and y < y1

def try_it(vx, vy):
    x = 0
    y = 0
    max_y = 0
    while True:
        x,y,vx,vy = step(x, y, vx, vy)
        if y > max_y: max_y = y
        if in_target(x, y):
            return max_y # target
        elif x > x2 or y < y1:
            return None # missed

# find minimum possible range
max_vx = x2+1
min_vx = 0
test_x = 0
while test_x < x1:
    min_vx += 1
    test_x += min_vx

max_y = 0
results = []
for vx in range(min_vx, max_vx+1):
    # found_y = False
    for vy in range(-200, 200):
        # print("trying: " , vx,vy)
        result = try_it(vx,vy)
        print(vx, vy, result)
        if result is not None:
            found_y = True
            results.append((vx,vy))
            if result > max_y: max_y = result


print(max_y)
print(len(results))













