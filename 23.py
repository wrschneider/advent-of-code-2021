state = {
    # "rooms": ["BDDA", "CCBD", "BBAC", "DACA"],
    "rooms": ["DDDB", "DCBA", "CBAB", "CACA"],
     "hall": [None] * 11,
    # "rooms": [[None, "A"], ["B", "B"], ["C", "C"], ["D", "D"]],
    # "hall": [None] * 10 + ["A"],
    "energy": 0
}
st = "ABCD"
erg = {"A": 1, "B": 10, "C":100, "D":1000}
hallpos = set([0,1,3,5,7,9,10])
CAPACITY = len(state["rooms"][0])
# rooms at indexes 2,4,6,8

def valid_moves(state):
    possible_new_states = []

    # for those in hallway can we put anyone in right place?
    for i in range(len(state["hall"])):
        if state["hall"][i] is None:
            continue
        
        ch = state["hall"][i]
        # check if slot open
        room = state["rooms"][st.index(ch)]
        if len(room) > 0 and any(chr != ch for chr in room):
            continue
        
        iroom = (st.index(ch) + 1) * 2 
        # check if path open
        if i > iroom and any(state["hall"][j] is not None for j in range(iroom, i)):
            continue
        if i < iroom and any(state["hall"][j] is not None for j in range(i+1, iroom)):
            continue
        # calculate energy
        steps = abs(iroom - i) + (CAPACITY - len(room))
        erg_used = erg[ch] * steps
        new_state = {"hall": list(state["hall"]), "rooms": list(state["rooms"])}
        new_state["energy"] = state["energy"] + erg_used
        new_state["rooms"][st.index(ch)] = ch + room
        new_state["hall"][i] = None
        possible_new_states.append(new_state)
    
    if possible_new_states:
        return possible_new_states

    for room in range(0,4):
        roomst = state["rooms"][room]
        if all(s == st[room] for s in roomst):
            continue # no available moves out of this room
        if len(roomst) > 0:
            ch = roomst[0]

            # look through all possible hallway moves
            for i in range((room+1)*2, -1, -1):
                if i not in hallpos:
                    continue
                if state["hall"][i] is not None:
                    break
                # possible move
                new_state = {"hall": list(state["hall"]), "rooms": list(state["rooms"])}
                new_state["hall"][i] = ch
                new_state["rooms"][room] = roomst[1:]
                erg_used = erg[ch] * abs((room+1)*2 - i + (CAPACITY - len(roomst) + 1))
                new_state["energy"] = state["energy"] + erg_used
                possible_new_states.append(new_state)

            for i in range((room+1)*2+1, 11):
                if i not in hallpos:
                    continue
                if state["hall"][i] is not None:
                    break
                # possible move
                new_state = {"hall": list(state["hall"]), "rooms": list(state["rooms"])}
                new_state["hall"][i] = ch
                new_state["rooms"][room] = roomst[1:]
                erg_used = erg[ch] * (i - (room+1)*2 + (CAPACITY - len(roomst) + 1))
                new_state["energy"] = state["energy"] + erg_used
                possible_new_states.append(new_state)


    return possible_new_states

states = [state]
states_seen = set()
winning = None

final_state = ["A" * CAPACITY, "B" * CAPACITY, "C" * CAPACITY, "D" * CAPACITY]
while states:
    testst = states.pop()
    for move in valid_moves(testst):
        # print(move)
        if move["rooms"] == final_state:
            if winning is None or move["energy"] < winning["energy"]:
                print("**** WIN *****", move["energy"])
                winning = move

        else:
            st_tuple = (tuple(move["rooms"]), tuple(move["hall"]), move["energy"])
            if st_tuple not in states_seen and (winning is None or move["energy"] < winning["energy"]):
                states.append(move)
                states_seen.add(st_tuple)
            else:
                # print("pruning")
                pass

print("****** FINAL *****")
print(winning)

