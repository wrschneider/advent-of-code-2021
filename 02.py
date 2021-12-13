f = open("02.txt")
input = f.readlines()

def new_pos(pos, move):
   cmd, delta_s = move.split(" ")
   delta = int(delta_s)
   if cmd == "forward": return (pos[0] + delta, pos[1] + pos[2] * delta , pos[2])
   if cmd == "down": return (pos[0], pos[1], pos[2] + delta)
   if cmd == "up": return (pos[0], pos[1], pos[2] - delta)
   raise Exception(move) 

pos = (0, 0, 0)
for move in input:
    if not move: break
    pos = new_pos(pos, move)

print(pos)
print(pos[0] * pos[1])
