input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7""".split("\n")

input = [s.strip("\n") for s in open("04.txt").readlines()]
numbers_to_call = [int(x) for x in input[0].split(",")]

board_lines = input[1:]
num_boards = len(board_lines)//6

def board(i):
    return [[(int(line[k*3:k*3+2]), False) for k in range(5)] for line in board_lines[i*6+1:i*6+6]]

boards = [board(i) for i in range(num_boards)]
winning_boards = {}

def calculate_score(board, num):
    return sum(board[j][i][0] for j in range(5) for i in range(5) if not board[j][i][1]) * num
    
def check_winning_board(board):
   win = any(all(board[j][i][1] for j in range(5)) for i in range(5)) or any(all(board[j][i][1] for i in range(5)) for j in range(5))
   if win:
      return True
   
def cell(c):
   star = "*" if c[1] else " "
   return f"{str(c[0])}{star}"

def play_number(num):
    # go through all boards and mark as selected
    print("CALLED " + str(num))
    for b, board in enumerate(boards):
        if b in winning_boards: 
            continue
        for i in range(5):
            for j in range(5):
                if board[j][i][0] == num:
                    board[j][i] = (board[j][i][0], True)
                    if check_winning_board(board): 
                        score = calculate_score(board, num)
                        winning_boards[b] = score
                        print(score)
                   
        #print("")
        #:print("\n".join((" ".join(cell(board[j][i]) for i in range(5)) for j in range(5))))

for n in numbers_to_call:
    play_number(n)
