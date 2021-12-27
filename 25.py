input = """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>""".split("\n")

def move(inp):
    moved = False
    # process east facing first
    for i in range(len(inp)):
        ln = inp[i]
        lenln = len(ln)
        newline = list(ln)
        moves = []
        for j in range(lenln):
            if ln[j] == ">" and ln[(j+1) % lenln] == ".":
                moves.append(j)
        for m in moves:
            moved = True
            newline[(m+1) % lenln] = ">"
            newline[m] = "."
        inp[i] = newline

    # now south
    lenln = len(inp[0])
    for i in range(lenln):
        moves = []
        for j in range(len(inp)):
            if inp[j][i] == "v" and inp[(j+1) % len(inp)][i] == ".":
                moves.append(j)
        for m in moves:
            moved = True
            inp[(m+1)%len(inp)][i] = "v"
            inp[m][i] = "."

    return moved
    
input = [s.strip() for s in open("25.txt").readlines()]

m = 0
moved = True
while moved:
    m += 1
    moved = move(input)

print(m)

for ln in input:
    print("".join(ln))



