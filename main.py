board = [' ' for x in range(10)]


def insertLetter(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos] == ' '


def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (
            bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (
                   bo[2] == le and bo[5] == le and bo[8] == le) or (
                   bo[3] == le and bo[6] == le and bo[9] == le) or (
                   bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)


def playerMove():
    run = True
    while run:
        move = input("Enter a number between 0-9\n")
        try:
            move = int(move)
            if 0 < move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('x', move)
                else:
                    print('Space is occupied !')
            else:
                print("Enter an integer between 0 - 9")
        except:
            print('Enter an integer')


def cmpMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['o', 'x']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                return i

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move

    return move


def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


if __name__ == '__main__':
    '''
    Computer is 'o' and player is 'x'
    '''

    while True:
        print("Play Tic tac toe ? Y or N ?")
        if input() == 'Y':
            print("Game starts now")
            printBoard(board)

            while not (isBoardFull(board)):
                if not isWinner(board, 'o'):
                    playerMove()
                    printBoard(board)
                else:
                    print("Computer won")

                if not isWinner(board, 'x'):
                    move = cmpMove()
                    if move == 0:
                        print("Tie game")
                    else:
                        insertLetter('o', move)
                        print("Computer placed o in ", move)
                        printBoard(board)
                else:
                    print("You've won! Good job")

            if isBoardFull(board):
                print("Tie game")
        else:
            exit()
