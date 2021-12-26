orientations = [
    (0,1,2, 1,1,1),
    (1,0,2, 1,-1,1),
    (0,1,2, -1,-1,1),
    (1,0,2, -1,1,1),

    (2,1,0, -1,1,1),
    (1,2,0, 1,1,1),
    (2,1,0, 1,-1,1),
    (1,2,0, -1,-1,1),

    (0,2,1, 1,-1,1),
    (2,0,1, -1,-1,1),
    (0,2,1, -1,1,1),
    (2,0,1, 1,1,1),

    (0,1,2, -1,1,-1),
    (1,0,2, 1,1,-1),
    (0,1,2, 1,-1,-1),
    (1,0,2, 1,1,-1),

    (2,1,0, -1,-1,-1),
    (1,2,0, -1,1,-1),
    (2,1,0, 1,1,-1),
    (1,2,0, 1,-1,-1),

    (0,2,1, 1,1,-1),
    (2,0,1, 1,-1,-1),
    (0,2,1, -1,-1,-1),
    (2,0,1, -1,1,-1),
]

input = [s.strip() for s in open("19_sample.txt").readlines()]
input = [s.strip() for s in open("19.txt").readlines()]

scanners = []
beacons = []
scanners.append(beacons)
for s in input:
    if not s:
        beacons = []
        scanners.append(beacons)
        continue

    if s.startswith("---"):
        continue
    
    beacons.append(tuple(int(i) for i in s.split(",")))


def invert(o):
    a = o.index(0)
    b = o.index(1)
    c = o.index(2)
    return (a, b, c, o[3+a], o[3+b], o[3+c])

def find_overlapping(s1, s2):
    set1 = set(s1)
    set2 = set(s2)
    for i in range(len(s1)-10):
        for o in orientations:
            for j in range(len(s2)):
                # assume these are the same, how many others are there?
                matching = []
                for i2 in range(i, len(s1)):
                    ofs = (s1[i2][0] - s1[i][0], s1[i2][1] - s1[i][1], s1[i2][2] - s1[i][2])
                    ofs_rot = (ofs[o[0]] * o[3], ofs[o[1]] * o[4], ofs[o[2]] * o[5])
                    pt = (s2[j][0] + ofs_rot[0], s2[j][1] + ofs_rot[1], s2[j][2] + ofs_rot[2])
                    if pt in set2:
                        # print("s2", pt, "s1", s1[i2])
                        matching.append(s1[i2])

                if len(matching) >= 12:
                    # assemble new map of s1 + others in s2 not in s1
                    # print(s1[i], s2[j], o)
                    new_map = list(s1)
                    for b in s2:
                        ofs = (b[0] - s2[j][0], b[1] - s2[j][1], b[2] - s2[j][2])
                        o2 = invert(o)
                        ofs_rot = (ofs[o2[0]] * o2[3], ofs[o2[1]] * o2[4], ofs[o2[2]] * o2[5])
                        pt = (s1[i][0] + ofs_rot[0], s1[i][1] + ofs_rot[1], s1[i][2] + ofs_rot[2])
                        # print("original", b, "ofs", ofs, "ofs_rot", ofs_rot, "new", pt)
                        if pt not in set1:
                            # print("new, appending")
                            new_map.append(pt)
                    return new_map
                    

for i in range(len(scanners)):
    for j in range(i+1, len(scanners)):
        ovl = find_overlapping(scanners[i], scanners[j])
        if ovl is not None:
            print("found match", i, j)
            