input = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""".split("\n")

input = [s.strip() for s in open("03.txt").readlines() if s]

num_bits = len(input[0])

def dig_sum(input, i):
    x = sum(int(s[i]) for s in input if s)
    return(x)

o2 = input
co2 = input

for i in range(num_bits):
    input_length = len(o2)
    print(dig_sum(o2, i), input_length//2)
    o2 = [s for s in o2 if len(o2) == 1 or s[i] == "1" and dig_sum(o2, i)*2 >= input_length or s[i] == "0" and dig_sum(o2, i)*2 < input_length]
    print(o2)
    input_length = len(co2)
    print(dig_sum(co2, i), input_length//2)
    co2 = [s for s in co2 if len(co2) == 1 or s[i] == "0" and dig_sum(co2, i)*2 >= input_length or s[i] == "1" and dig_sum(co2, i)*2 < input_length]
    print(co2)

print(o2)
print(co2)
print(int(o2[0], 2) * int(co2[0], 2))

