f = open("01.txt")

input_s = f.readlines()

input = [int(s) for s in input_s if s]

output = sum(1 for i in range(3, len(input)) if input[i] > input[i-3])

print(output)
