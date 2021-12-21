def add(s1, s2):
    return "[" + s1 + "," + s2 + "]"

def split(s):
    for i in range(len(s)):
        if s[i].isdigit():
            for j in range(i+1, len(s)):
                if not s[j].isdigit(): break
            num = int(s[i:j])
            if num >= 10:
                left = num // 2
                right = num // 2
                if num % 2 == 1:
                    right += 1
                return s[0:i] + "[" + str(left) + "," + str(right) + "]" + s[j:]
def explode(s):
    depth = 0
    for i in range(len(s)):
        ch = s[i]
        if ch == "[":
            depth += 1
        if ch == "]":
            depth -= 1
        if depth == 5:
            lbrace = i
            comma = s.index(",", i+1)
            rbrace = s.index("]", i+1)
            # replace lbrace..rbrace with "0"
            left = int(s[i+1:comma])
            right = int(s[comma+1:rbrace])
            print(left, right)

            leftnum = None
            rightnum = None
            for j in range(i, 0, -1):
                if s[j].isdigit():
                    leftnum_end = j+1
                    leftnum_start = j
                    for k in range(j-1, 0, -1):
                        if (s[k:leftnum_end].isdigit()):
                            leftnum_start = k
                        else: 
                            break
                    leftnum = int(s[leftnum_start:leftnum_end])
                    print(leftnum)
                    break

            for j in range(rbrace, len(s)):
                if s[j].isdigit():
                    rightnum_start = j
                    rightnum_end = j+1
                    for k in range(j+1, len(s)):
                        if s[rightnum_start:k].isdigit():
                            rightnum_end = k
                        else:
                            break
                    rightnum = int(s[rightnum_start:rightnum_end])
                    print(rightnum)
                    break
            
            new_result = ""
            # finish explode process
            if leftnum is not None:
                leftnum = left + leftnum
                new_result += s[0:leftnum_start] + str(leftnum) + s[leftnum_end:lbrace]
            else:
                new_result += s[0:lbrace]
            new_result += "0"
            if rightnum is not None:
                rightnum = right + rightnum
                new_result += s[rbrace+1:rightnum_start] + str(rightnum) + s[rightnum_end:]
            else:
                new_result += s[rbrace+1:]

            return new_result

def reduce(s):
    while True:
        s1 = explode(s)
        if s1 is not None:
            s = s1
            continue
        
        s2 = split(s)
        if s2 is not None:
            s = s2
            continue

        return s

def add_up(lst):
    curr = lst[0]
    for s in lst[1:]:
        curr = add(curr, s)
        curr = reduce(curr)
    return curr

def mag(lst):
    left = lst[0]
    if type(left) == type(list()):
        left = mag(left)
    else:
        left = int(left)
    right = lst[1]
    if type(right) == type(list()):
        right = mag(right)
    else:
        right = int(right)

    return 3*left + 2*right

input = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]""".split("\n")

input = [s.strip() for s in open("18.txt").readlines()]

# part 1
print(add_up(input))
print(mag(eval(add_up(input))))

# part 2
maxmag = 0
for i in range(0, len(input)):
    for j in range(i+1, len(input)):
        m = mag(eval(add_up([input[i], input[j]])))
        if m > maxmag: maxmag = m
print (maxmag)


