input = [s.strip() for s in open("20.txt").readlines()]

code = input[0]

image = input[2:]
sz = len(image)

lit_pixels = set()
for i in range(sz):
    for j in range(sz):
        if image[i][j] == "#": lit_pixels.add((i,j))

print(len(lit_pixels))

def enhance(lit_pixels, mn, mx, inf):
    def pixel_lit(i,j):
        if (i,j) in lit_pixels: return True

        return inf and (i <= mn or i >= mx-1 or j <= mn or j >= mx-1)

    new_pixels = set()
    for i in range(mn, mx):
        for j in range(mn, mx):
            # calculate new pixel at [i][j] from 8 surrounding
            lst = (["1" if pixel_lit(i-1, j2) else "0" for j2 in range(j-1, j+2)]
             + ["1" if pixel_lit(i, j2) else "0" for j2 in range(j-1, j+2)]
             + ["1" if pixel_lit(i+1, j2) else "0" for j2 in range(j-1, j+2)])
            num = int("".join(lst), 2)
            if (i <= 0 and j <= 0):
                # print(i,j,lst,num,code[num])
                pass
            # print(i, j, num)
            if code[num] == "#": new_pixels.add((i,j))

    # special case for infinity
    inf = code[0] == "#" if not inf else code[-1] == "#"
    return new_pixels, inf

inf = False
for i in range(1, 51):
    lit_pixels, inf = enhance(lit_pixels, -i, sz+i, inf)
    
# print(sorted(list(round1)), inf1)
# print(sorted(list(round2)), inf2)

print(len(lit_pixels))

