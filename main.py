import time
import togboard

def humanPlay():
    tBoard = togboard.TogBoard()
    gameFinished = False

    while not tBoard.finished:
        while True:
            moveStr = input("\nEnter your move (1-9, 0 - exit): ")
            if not moveStr.isdigit():
                continue

            move = int(moveStr)
            if move == 0:
                gameFinished = True
                break
            elif move in range(1, 10):
                break

        if gameFinished:
           break            

        tBoard.makeMove(move)
        tBoard.printPosition(True)

    print("\nGame over: {} - {}. Result: {}\n".format(tBoard.fields[20], tBoard.fields[21], tBoard.gameResult))
    tBoard.printPosition(True)
    tBoard.printNotation(True)

def machinePlay():
    while True:
        numStr = input("\nEnter number of iterations (1-1000): ")
        if not numStr.isdigit():
            continue

        num = int(numStr)
        if num in range(1, 1001):
            break

    win = draw = loss = 0
    start = time.time()

    for i in range(1, num + 1):
        tBoard = togboard.TogBoard()
        while not tBoard.finished:
            ai = tBoard.makeRandomMove()

        if num <= 5:
            tBoard.printPosition(True)
            print("\nGame over: {} - {}. Result: {}\n".format(tBoard.fields[20], tBoard.fields[21], tBoard.gameResult))

        if tBoard.gameResult == 1:
            win += 1
        elif tBoard.gameResult == -1:
            loss += 1
        elif tBoard.gameResult == 0:
            draw += 1
        else:
            print("What??")

    print("W: {}, D: {}, L: {}\n".format(win, draw, loss))
    elapsed = time.time() - start
    print("Elapsed: " + str(elapsed))

def randomPlay():
    tBoard = togboard.TogBoard()
    gameFinished = False
    currentColor = 0

    while True:
        colorStr = input("\nEnter your color (0 - white, 1 - black): ")
        if not colorStr.isdigit():
            continue

        color = int(colorStr)
        if color in range(0, 2):
            break

    while not tBoard.finished:
        if currentColor == color:
            while True:
                moveStr = input("\nEnter your move (1-9, 0 - exit): ")
                if not moveStr.isdigit():
                    continue

                move = int(moveStr)
                if move == 0:
                    gameFinished = True
                    break
                elif move in range(1, 10):
                    break

            if gameFinished:
               break            

            tBoard.makeMove(move)
            tBoard.printPosition(True)
            color = 0 if color == 1 else 1
        else:
            ai = tBoard.makeRandomMove()
            print("AI move: " + ai)
            tBoard.printPosition(True)
            color = 0 if color == 1 else 1

    print("\nGame over: {} - {}. Result: {}\n".format(tBoard.fields[20], tBoard.fields[21], tBoard.gameResult))
    tBoard.printPosition(True)
    tBoard.printNotation(True)


print("Welcome to Togyz Kumalak world!")

modeStr = input("\nEnter the mode (h - human play, m - random machine, r - against random AI): ")
if modeStr == 'h':
    humanPlay()
elif modeStr == 'm':
    machinePlay()
elif modeStr == 'r':
    randomPlay()