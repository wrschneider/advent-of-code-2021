input = [s.strip("\n") for s in open("08.txt").readlines()]

# input = ["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]

parsed = [[s.strip().split(" ") for s in line.split("|")] for line in input]

def infer(line):
  unique_digits = {
    2: 1,
    3: 7,
    4: 4,
    7: 8
  }

  mapping = {}
  digits = {} # reverse mapping

  for s in line[0]:
    s_s = "".join(sorted(s))
    if len(s) in unique_digits:
      mapping[s_s] = unique_digits[len(s)]
      digits[unique_digits[len(s)]] = s

  # now we know 1, 4, 7 and 8
  # second pass to figure out 6, 9 and 0
  for s in line[0]:
    s_s = "".join(sorted(s))
    if len(s) == 6:
      if len(set(digits[1]).intersection(set(s))) == 1:
        digits[6] = s
        mapping[s_s] = 6
      elif len(set(digits[4]).intersection(set(s))) == 3:
        digits[0] = s
        mapping[s_s] = 0
      else:
        digits[9] = s
        mapping[s_s] = 9
  
  # last ones 2 3 and 5
  for s in line[0]:
    s_s = "".join(sorted(s))
    if len(s) == 5:
      if len(set(digits[1]).intersection(set(s))) == 2:
        digits[3] = s
        mapping[s_s] = 3
      elif len(set(digits[6]).intersection(set(s))) == 5:
        digits[5] = s
        mapping[s_s] = 5
      else:
        digits[2] = s
        mapping[s_s] = 2
      
  num = "".join(str(mapping[s_s]) for s_s in ["".join(sorted(s)) for s in line[1]])
  return(int(num))

print(sum(infer(line) for line in parsed))


