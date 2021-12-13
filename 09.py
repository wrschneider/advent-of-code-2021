input = """2199943210
3987894921
9856789892
8767896789
9899965678""".split("\n")

input = [s.strip() for s in open('09.txt').readlines()]

def find_lows():
    for i in range(len(input)):
        for j in range(len(input[i])):
            # 4 different directions - only up/down/left/right
            curr = input[i][j]
            is_low = (i < 0 or curr < input[i-1][j]) and (i == (len(input) - 1) or curr < input[i+1][j]) and (j < 0 or curr<input[i][j-1]) and (j == len(input[i])-1 or curr < input[i][j+1])
            if is_low: yield (i,j)


def find_basin(low):
    basin = set([low])
    q = [low]
    while q:
        i, j = q.pop()
        val = input[i][j]
        # points around current
        point = (i-1, j)
        if i > 0 and input[i-1][j] < '9' and point not in basin:
            basin.add(point)
            q.append(point)
        point = (i+1, j)
        if i < len(input) - 1 and input[i+1][j] < '9' and point not in basin:
            basin.add(point)
            q.append(point)
        point = (i, j-1)
        if j > 0 and input[i][j-1] < '9' and point not in basin:
            basin.add(point)
            q.append(point)
        point = (i, j+1)
        if j < len(input[i]) - 1 and input[i][j+1] < '9' and point not in basin:
            basin.add(point)
            q.append(point)
    return basin

basin_lengths = [len(find_basin(low)) for low in find_lows()]
basin_lengths = (sorted(basin_lengths)[::-1])
print(basin_lengths[0] * basin_lengths[1] * basin_lengths[2])