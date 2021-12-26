input = [s.strip() for s in open("22.txt").readlines()]

instr = []
for ln in input:
    onstr , dims = ln.split(" ")
    on = onstr == "on"
    instr.append(([[int(x) for x in d.split("=")[1].split("..")] for d in dims.split(",")], on))
    
ct = 0
for i in range(-50, 51):
    for j in range(-50, 51):
        for k in range(-50, 51):
            on = False
            for ins in instr:
                if i >= ins[0][0][0] and i <= ins[0][0][1] and j >= ins[0][1][0] and j <= ins[0][1][1] and k >= ins[0][2][0] and k <= ins[0][2][1]:
                    on = ins[1]
            if on: ct += 1

print(ct)