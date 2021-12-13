from collections import defaultdict

input = """start-A
start-b
A-c
A-b
b-d
A-end
b-end""".split("\n")

input = [s.strip() for s in open("12.txt").readlines()]

graph = defaultdict(list)

for line in input:
    n1, n2 = line.split("-")
    graph[n1].append(n2)
    graph[n2].append(n1)

def paths(n1, current_path, counts):
    # print(current_path)
    if n1 == "end": return [current_path]

    next_paths = []

    for n2 in graph[n1]:
        if n2 == "start": continue
        if n2.islower() and n2 in current_path and any(ct >= 2 for ct in counts.values()):
            continue
        new_counts = counts.copy()
        if n2.islower(): new_counts[n2] += 1
        next_paths += paths(n2, current_path + [n2], new_counts)
    return next_paths

counts = defaultdict(int)
p = paths("start", ["start"], counts)
print(len(p))
print("\n".join(",".join(n for n in path) for path in p))


    