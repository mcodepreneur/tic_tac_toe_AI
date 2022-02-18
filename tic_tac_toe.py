import random

def print_board(inp) :
    print()
    for first in inp :
        for item in first :
            print(item, end = '  ')
        print()
    print()

def is_run(inp, exc, run) :
    check = None
    done_check = 0
    first = True
    for line in inp :
        for item in line:
            if check is None or check is item and check is not exc :
                check = item
                done_check = done_check + 1
            if done_check == run : 
                return check
        done_check = 0
        check = None
    for x in range(3) :
        for y in range(3) :
            item  = inp[y][x]
            if check is None or check is item and check is not exc :
                check = item
                done_check = done_check + 1
            if done_check == run : 
                return check
        done_check = 0
        check = None
    for x in range(2) :
        for y in range(3) :
            if first : 
                item = inp[y][y]
            else : 
                item = inp[y][abs(y - 2)]
            if check is None or check is item and check is not exc :
                check = item
                done_check = done_check + 1
            if done_check == run : 
                return check
        done_check = 0
        check = None
        first = False
    return False

def make_move(move, exc) :
    if exc is None :    
        inp = input("Enter "+ move +"'s move (column+row): ")
    else :
        inp = exc
    try :
        if board[int(inp[1]) - 1][int(inp[0:1]) - 1] is fill :
            board[int(inp[1]) - 1][int(inp[0:1]) - 1] = move
        else :
            print('\nThis space is taken!\n')
            make_move(move, exc)
    except : 
        print("\nInvalid move, try again\n")
        make_move(move, exc)

def is_center_hole(set) :
    i = 0
    x = 0
    y = 0
    is_center = False
    for set in set :
        for place in set :            
            if place != '-' :
                if y == 1 and x == 1 :
                    is_center = True
                else :
                    return False   
            else : 
                i = i + 1             
            x = x + 1
        y = y + 1
        x = 0
    
    if is_center :
        return True
    return None

def sides(set) :
    i = 0
    x = 0
    y = 0
    for line in set :
        for item in line :
            if item != '-' :
                if x == 0 and y == 1 :
                    i = i + 1
                elif x == 1 and (y == 0 or y == 2) : 
                    i = i + 1
                elif x == 2 and y == 1 :
                    i = i + 1
            y = y + 1
        x = x + 1
        y = 0
    return i

def moves(set) :
    i = 0
    for line in set :
        for space in line :
            if space != '-' :
                i = i + 1
    return i

def run_catch(player, set) : 
    i = 0
    x = 0
    y = 0
    spots = []
    mapx = [set[0].copy(), set[1].copy(), set[2].copy()]
    for line in set :
        for item in line :
            
            if item == '-' :
                mapx[x][y] = i
            else :
                mapx[x][y] = item           
            i = i + 1
            y = y + 1
        x = x + 1
        y = 0
        # to get around character exemption, make all the -'s different
    # detects if a win is about to occur, done for each point on board, alternate method than is_run()
    
    if ((mapx[1][0] == player and mapx[2][0] == player) or (mapx[0][1] == player and mapx[0][2] == player) or (mapx[1][1] == player and mapx[2][2] == player)) and isinstance(mapx[0][0], int) :
        # covers all partial runs that converge at 1,1 typed input
        return ['11']
    if ((mapx[0][0] == player and mapx[2][0] == player) or (mapx[1][1] == player and mapx[1][2] == player)) and isinstance(mapx[1][0], int) :
        return ['12']
    if ((mapx[0][0] == player and mapx[1][0] == player) or (mapx[0][2] == player and mapx[1][1] == player) or (mapx[2][1] == player and mapx[2][2] == player)) and isinstance(mapx[2][0], int) :
        return ['13']
    if ((mapx[0][0] == player and mapx[0][2] == player) or (mapx[1][1] == player and mapx[2][1] == player)) and isinstance(mapx[0][1], int) :
        return ['21']
    if ((mapx[0][0] == player and mapx[2][2] == player) or (mapx[2][1] == player and mapx[0][1] == player) or (mapx[1][0] == player and mapx[1][2] == player) or (mapx[2][0] == player and mapx[0][2] == player)) and isinstance(mapx[1][1], int) :
        return ['22']
    if ((mapx[0][1] == player and mapx[1][1] == player) or (mapx[2][0] == player and mapx[2][2] == player)) and isinstance(mapx[2][1], int) :
        return ['23']
    if ((mapx[0][0] == player and mapx[0][1] == player) or (mapx[2][0] == player and mapx[1][1] == player) or (mapx[1][2] == player and mapx[2][2] == player)) and isinstance(mapx[0][2], int) :
        return ['31']
    if ((mapx[1][0] == player and mapx[1][1] == player) or (mapx[0][2] == player and mapx[2][2] == player)) and isinstance(mapx[1][2], int) :
        return ['32']
    if ((mapx[0][0] == player and mapx[1][1] == player) or (mapx[2][0] == player and mapx[2][1] == player) or (mapx[0][2] == player and mapx[1][2] == player)) and isinstance(mapx[2][2], int) :
        return ['33']
    
    if (mapx[1][0] == mapx[2][0] or mapx[0][1] == mapx[0][2] or mapx[1][1]  == mapx[2][2]) and isinstance(mapx[0][0], int) :
        # covers all partial runs that converge at 1,1 typed input
        spots.append('11')
    if (mapx[0][0] == mapx[2][0] or mapx[1][1] == mapx[1][2]) and isinstance(mapx[1][0], int) :
        spots.append('12')
    if (mapx[0][0] == mapx[1][0] or mapx[0][2] == mapx[1][1] or mapx[2][1] == mapx[2][2]) and isinstance(mapx[2][0], int) :
        spots.append('13')
    if (mapx[0][0] == mapx[0][2] or mapx[1][1] == mapx[2][1]) and isinstance(mapx[0][1], int) :
        spots.append('21')
    if (mapx[0][0] == mapx[2][2] or mapx[2][1] == mapx[0][1] or mapx[1][0] == mapx[1][2] or mapx[2][0] == mapx[0][2]) and isinstance(mapx[1][1], int) :
        spots.append('22')
    if (mapx[0][1] == mapx[1][1] or mapx[2][0] == mapx[2][2]) and isinstance(mapx[2][1], int) :
        spots.append('23')
    if (mapx[0][0] == mapx[0][1] or mapx[2][0] == mapx[1][1] or mapx[1][2] == mapx[2][2]) and isinstance(mapx[0][2], int) :
        spots.append('31')
    if (mapx[1][0] == mapx[1][1] or mapx[0][2] == mapx[2][2]) and isinstance(mapx[1][2], int) :
        spots.append('32')
    if (mapx[0][0] == mapx[1][1] or mapx[2][0] == mapx[2][1] or mapx[0][2] == mapx[1][2]) and isinstance(mapx[2][2], int) :
        spots.append('33')
    
    return spots

def across(player, map) : # returns moves across from an existing player's move, like next_to()
    moves = []
    if map[0][0] == '-' and ((map[1][0] == '-' and map[2][0] == player) or (map[0][1] == '-' and map[0][2] == player)) :
        moves.append('11')
    if map[1][0] == '-' and (map[1][1] == '-' and map[1][2] == player) :
        moves.append('12')
    if map[2][0] == '-' and ((map[1][0] == '-' and map[0][0] == player) or (map[2][1] == '-' and map[2][2] == player)) :
        moves.append('13')
    if map[0][1] == '-' and (map[1][1] == '-' and map[2][1] == player) :
        moves.append('21')
    if map[2][1] == '-' and (map[1][1] == '-' and map[0][1] == player) :
        moves.append('23')
    if map[0][2] == '-' and ((map[0][1] == '-' and map[0][0] == player) or (map[1][2] == '-' and map[2][2] == player)) :
        moves.append('31')
    if map[1][2] == '-' and (map[1][1] == '-' and map[1][0] == player) :
        moves.append('32')
    if map[2][2] == '-' and ((map[2][1] == '-' and map[2][0] == player) or (map[1][2] == '-' and map[0][2] == player)) :
        moves.append('33')
    return moves

def next_to(player, map) : # returns list of moves next to existing player, formatted like run_catch()
    moves = []
    if map[0][0] == '-' and ((map[1][1] == player and map[2][2] == '-') or (map[1][0] == player and map[2][0] == '-') or (map[0][1] == player and map[0][2] == '-')) :
        moves.append('11')
    if map[1][0] == '-' and ((map[1][1] == player and map[1][2] == '-') or ((map[0][0] == player and map[2][0] == '-') or (map[2][0] == player and map[0][0] == '-'))) :
        moves.append('12')
    if map[2][0] == '-' and ((map[1][0] == player and map[0][0] == '-') or (map[2][1] == player and map[2][2] == '-') or (map[1][1] == player and map[0][2] == '-')) :
        moves.append('13')
    if map[0][1] == '-' and ((map[1][1] == player and map[2][1] == '-') or ((map[0][0] == player and map[0][2] == '-') or (map[0][2] == player and map[0][0] == '-'))) :
        moves.append('21')
    if map[1][1] == '-' and (((map[0][1] == player and map[2][1] == '-') or (map[2][1] == player and map[0][1] == '-')) or ((map[1][0] == player and map[1][2] == '-') or (map[1][2] == player and map[1][0] == '-')) or ((map[2][0] == player and map[0][2] == '-') or (map[0][2] == player and map[2][0] == '-')) or ((map[0][0] == player and map[2][2] == '-') or (map[2][2] == player and map[0][0] == '-'))) :
        moves.append('22')
    if map[2][1] == '-' and ((map[1][1] == player and map[0][1] == '-') or ((map[2][0] == player and map[2][2] == '-') or (map[2][2] == player and map[2][0] == '-'))) :
        moves.append('23')
    if map[0][2] == '-' and ((map[0][1] == player and map[0][0] == '-') or (map[1][1] == player and map[2][0] == '-') or (map[1][2] == player and map[2][2] == '-')) :
        moves.append('31')
    if map[1][2] == '-' and ((map[1][1] == player and map[1][0] == '-') or ((map[0][2] == player and map[2][2] == '-') or (map[2][2] == player and map[0][2] == '-'))) :
        moves.append('32')
    if map[2][2] == '-' and ((map[1][1] == player and map[0][0] == '-') or (map[2][1] == player and map[2][0] == '-') or (map[1][2] == player and map[0][2] == '-')) :
        moves.append('33')
    return moves

def empty(set) : # return list of all empty spots
    spots = []
    x = 1
    y = 1
    for line in set :
        for item in line :
            if item == '-' :
                spots.append(str(x) + str(y))
            x = x + 1
        y = y + 1
        x = 1
    return spots

def best_move(player, set) :
    end = empty(set)
    if len(end) == 1 :
        return end[0]
        # if there's only one empty spot left take that spot
    intercept = run_catch(player, set)
    if len(intercept) > 0 :
        return intercept[random.randrange(len(intercept))]
    count = moves(set)
    corners = ['11', '13', '31', '33']
    if count == 0 :
        return corners[random.randrange(len(corners))]
        # automated moves returned in typed format to be passed in as string input
    if count == 1 and set[1][1] != '-' :
        return corners[random.randrange(len(corners))]
    if (count == 1 or count == 2 or count == 3) and set[1][1] == '-' :
        return '22'
    
    acros = across(player, set)
    if len(acros) > 0 :    
        return acros[random.randrange(len(acros))]
    
    next = next_to(player, set)
    if len(next) > 0 :    
        return next[random.randrange(len(next))]
    return end[random.randrange(len(end))]        

board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
#print_board(board)
fill = '-'
x_ai = None
count = 0

choo = input('Against computer? ("y"/other) ')
if choo == 'y' or choo == 'Y' :
    while x_ai == None :
        is_ai = input('\nX or O computer? ("x"/"o") ')
        if is_ai == 'x' or is_ai == 'X' :
            x_ai = True
        elif is_ai == 'o' or is_ai == 'O' :
            x_ai = False
        else :
            print('\nInvalid input, try again')

while True :
    #print('Across   : ' + str(across('X', board)))
    #print('Next_to  : ' + str(next_to('X', board)))
    #print('Run_catch: ' + str(run_catch('X', board)))
    
    if x_ai is True :
        make_move('X', best_move('X', board))
    else :
        if count == 0 :
            print_board(board)
        make_move('X', None)
    print_board(board)
    if is_run(board, fill, 3) is not False : break
    count = count + 1

    if count == 9 : 
        count = True 
        break

    #print('Across   : ' + str(across('O', board)))
    #print('Next_to  : ' + str(next_to('O', board)))
    #print('Run_catch: ' + str(run_catch('O', board)))
    
    if x_ai is False :
        make_move('O', best_move('O', board))
    else :
        make_move('O', None) 
    print_board(board)
    if is_run(board, fill, 3) is not False : break
    count = count + 1

if count is not True : 
    print(is_run(board, '-', 3), 'Wins!')
else :
    print("Cat's Game!")