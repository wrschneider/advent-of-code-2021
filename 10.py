input = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]""".split("\n")

input = [s.strip("\n") for s in open("10.txt").readlines()]

matching_chars = {"[": "]", "(": ")", "{": "}", "<": ">"}

scores = {")": 3, "]": 57, "}": 1197, ">": 25137}

def first_invalid_char(line):
    stack = []
    for ch in line:
        if ch in "[({<": stack.append(ch)
        if ch in "])}>":
            open_char = stack.pop()
            if ch != matching_chars[open_char]:
                return ch

def missing_chars(line):
    stack = []
    for ch in line:
        if ch in "[({<": stack.append(ch)
        if ch in "])}>":
            open_char = stack.pop()
    return [matching_chars[c] for c in stack][::-1]

def missing_char_score(chars):
    print ("".join(chars))
    c_scores = {')': 1, ']': 2, '}': 3, '>': 4}
    score = 0
    for c in chars:
        score *= 5
        score += c_scores[c]
    return score
    
score = 0
missing_scores = []
for line in input:
    c = first_invalid_char(line)
    if c:
        score += scores[c]
    else: 
        missing_scores.append(missing_char_score(missing_chars(line)))

print(score)
missing_scores = sorted(missing_scores)
print(missing_scores)
final = missing_scores[len(missing_scores)//2]
print(final)