from collections import Counter 

input = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C""".split("\n")

input = [s.strip() for s in open("14.txt").readlines()]
polymer = input[0]
rules = {}
for rule in input[2:]:
    s = rule.split(" -> ")
    rules[s[0]] = s[1]

c = Counter(polymer)

UPPER = 40
d = {}
def apply_rules(s, i):
    if i >= UPPER: return Counter()
    if s not in rules: return Counter()
    if (s, i) in d:
        return d[(s,i)]
    ch = rules[s]
    val = Counter(ch) + apply_rules(s[0] + ch, i + 1) + apply_rules(ch + s[1], i + 1)
    d[(s,i)] = val
    return val
    
for i in range(len(polymer)-1):
    s = polymer[i:(i+2)]
    c += apply_rules(s, 0)
    
print(c.most_common()[0][-1] - c.most_common()[-1][-1])



