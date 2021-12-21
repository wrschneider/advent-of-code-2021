pos = (8,3)
score = (0,0)
rolls = 0
curr = 0
player = 0

# 3  -> 1
# 4  -> 3 
# 5  -> 6 
# 6  -> 7
# 7  -> 6
# 8  -> 3 
# 9  -> 1

weights = {3:1, 4:3, 5:6, 6:7, 7:6, 8:3, 9:1}

d = {}  # state (positions,scores,whose turn) -> count of wins for each player from that state
def count_winners(pos, score, player):
    if (pos,score,player) in d:
        return d[pos,score,player]

    # wins from this state
    wins = [0,0]
    for roll in range(3,9+1):
        new_pos = (pos[player]+roll-1)%10 + 1
        new_score = score[player] + new_pos
        if new_score >= 21:
            wins[player] += weights[roll]
        else:
            if player == 0:
                new_pos_t = (new_pos, pos[1])
                new_scores_t = (new_score, score[1])
            else:
                new_pos_t = (pos[0], new_pos)
                new_scores_t = (score[0], new_score)
            
            wins_from_next_turn = count_winners(new_pos_t, new_scores_t, (player+1)%2)
            wins[0] += weights[roll] * wins_from_next_turn[0]
            wins[1] += weights[roll] * wins_from_next_turn[1]
    d[pos,score,player] = wins
    return wins

print(count_winners(pos, score, 0))
print(max(count_winners(pos, score, 0)))