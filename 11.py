input = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526""".split("\n")

input = [s.strip() for s in open("11.txt").readlines()]

grid = [[int(x) for x in line] for line in input]

adj = [(-1,-1), (-1, 0), (-1, +1), (0, -1), (0, +1), (+1, -1), (+1, 0), (+1, +1)]

def flash(i, j):
    grid[i][j] = 0
    for di, dj in adj:
        if i+di >= 0 and i+di < 10 and j+dj >= 0 and j+dj < 10:
            if grid[i+di][j+dj] == 0: continue # already flashed
            grid[i+di][j+dj] += 1
            if grid[i+di][j+dj] > 9:
                flash(i+di, j+dj)

def process_step():
    for i in range(10):
        for j in range(10):
            grid[i][j] += 1
    for i in range(10):
        for j in range(10):
            if grid[i][j] > 9:
                flash(i, j)
    flash_counter = sum(1 for i in range(10) for j in range(10) if grid[i][j] == 0)
    return flash_counter
    

for i in range(1000):
    flashes = process_step()
    if flashes == 100:
        print(i+1)
        break
    

# print(sum(process_step() for i in range(100)))