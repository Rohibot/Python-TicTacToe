#Rohith Karthikeyan
#copyright
# Tic-Tac-Toe
import random
#create game board
# game board is made up of 3 lists containing 3 elements each
# every element in the list starts out as a blank space, and may gain an "X" or "O" as the user plays the game.
row0 = [" "," "," "]
row1 = [" "," "," "]
row2 = [" "," "," "]
# Initialize a current player variable
currentPlayer = "X"
# Create a “counter or variable” that should become “True” when the game is over, but remains “False” until it is over
done = False
# Create a loop that runs until the game is over using a “while loop”.
while (done == False):
# print current player turn and game board
    print("Current Player: " + currentPlayer)
    print("   -0-1-2-")
    print("0: |" + row0[0] + "|" + row0[1] + "|" + row0[2] + "|")
    print("   -------")
    print("1: |" + row1[0] + "|" + row1[1] + "|" + row1[2] + "|")
    print("   -------")
    print("2: |" + row2[0] + "|" + row2[1] + "|" + row2[2] + "|")
    print("")
    # get row and column for current player
    if(currentPlayer == "X"):
        inputRow = int(input("Enter player " + currentPlayer + " row: "))
        inputCol = int(input("Enter player " + currentPlayer + " col: "))
        print("")
    elif(currentPlayer == "O"):
        #last item
        if ((row0[0] == "X") and (row0[1] == "X") and (row0[2] == " ")):
            inputRow = 0
            inputCol = 2
            
        elif ((row1[0] == "X") and (row1[1] == "X") and (row1[2] == " ")):
            inputRow = 1
            inputCol = 2
            
        elif ((row2[0] == "X") and (row2[1] == "X") and (row2[2] == " ")):
            inputRow = 2
            inputCol = 2
            
        elif ((row0[0] == "X") and (row1[0] == "X") and (row2[0] == " ")):
            inputRow = 2
            inputCol = 0
            
        elif ((row0[1] == "X") and (row1[1] == "X") and (row2[1] == " ")):
            inputRow = 2
            inputCol = 1
            
        elif ((row0[2] == "X") and (row1[2] == "X") and (row2[2] == " ")):
            inputRow = 2
            inputCol = 2
            
        elif ((row0[0] == "X") and (row1[1] == "X") and (row2[2] == " ")):
            inputRow = 2
            inputCol = 2
            
        elif ((row0[2] == "X") and (row1[1] == "X") and (row2[0] == " ")):
            inputRow = 2
            inputCol = 0
            
        #first item
        elif ((row0[0] == " ") and (row0[1] == "X") and (row0[2] == "X")):
            inputRow = 0
            inputCol = 0
            
        elif ((row1[0] == " ") and (row1[1] == "X") and (row1[2] == "X")):
            inputRow = 1
            inputCol = 0
            
        elif ((row2[0] == " ") and (row2[1] == "X") and (row2[2] == "X")):
            inputRow = 2
            inputCol = 0
            
        elif ((row0[0] == " ") and (row1[0] == "X") and (row2[0] == "X")):
            inputRow = 0
            inputCol = 0
            
        elif ((row0[1] == " ") and (row1[1] == "X") and (row2[1] == "X")):
            inputRow = 0
            inputCol = 1
            
        elif ((row0[2] == " ") and (row1[2] == "X") and (row2[2] == "X")):
            inputRow = 0
            inputCol = 2
            
        elif ((row0[0] == " ") and (row1[1] == "X") and (row2[2] == "X")):
            inputRow = 0
            inputCol = 0
            
        elif ((row0[2] == " ") and (row1[1] == "X") and (row2[0] == "X")):
            inputRow = 0
            inputCol = 2
            
            
        #middle Item
        elif ((row0[0] == "X") and (row0[1] == " ") and (row0[2] == "X")):
            inputRow = 0
            inputCol = 1
            
        elif ((row1[0] == "X") and (row1[1] == " ") and (row1[2] == "X")):
            inputRow = 1
            inputCol = 1
            
        elif ((row2[0] == "X") and (row2[1] == " ") and (row2[2] == "X")):
            inputRow = 2
            inputCol = 1
            
        elif ((row0[0] == "X") and (row1[0] == " ") and (row2[0] == "X")):
            inputRow = 1
            inputCol = 0
            
        elif ((row0[1] == "X") and (row1[1] == " ") and (row2[1] == "X")):
            inputRow = 1
            inputCol = 1
            
        elif ((row0[2] == "X") and (row1[2] == " ") and (row2[2] == "X")):
            inputRow = 1
            inputCol = 2
            
        elif ((row0[0] == "X") and (row1[1] == " ") and (row2[2] == "X")):
            inputRow = 1
            inputCol = 1
            
        elif ((row0[2] == "X") and (row1[1] == " ") and (row2[0] == "X")):
            inputRow = 1
            inputCol = 1
            
        else:
            inputRow = random.randint(0,2)
            inputCol = random.randint(0,2)
            print("")
        
    # place mark in appropriate cell
    if ((inputRow == 0) and (inputCol == (0 or 1 or 2))):
        if(row0[inputCol] == " "):
            row0[inputCol] = currentPlayer
        else:
            print("Stop taking other people's spot")
            continue
    elif ((inputRow == 1) and (inputCol == (0 or 1 or 2))):
        if(row1[inputCol] == " "):
            row1[inputCol] = currentPlayer
        else:
            print("Stop taking other people's spot")
            continue
    elif ((inputRow == 2) and (inputCol == (0 or 1 or 2))):
        if(row2[inputCol] == " "):
            row2[inputCol] = currentPlayer
        else:
            print("Stop taking other people's spot")
            continue
    else:
        print("You cannot make that move")
        continue
    # escape from loop on invalid row
    # Create an “if” block that will change the player.
    if(currentPlayer == "X"):
        currentPlayer = "O"
    elif(currentPlayer == "O"):
        currentPlayer = "X"
    # Check to see if there is 3-in-a-row in any direction.
    # There are 8 possibilities, so write code that will manually check each one for the same marks in a row.
    # If 3 in a row is found, print a winning message and set a variable to “True” to escape loop.
    #The first row and column has been done for you. Complete the remaining rows and columns.
    #Check the diagonals for 3 in a diagonal too. The first one has been done for you.

    # row 0
    if ((row0[0] == "X") and (row0[1] == "X") and (row0[2] == "X")):
        print("Player X wins in row 0!")
        done = True
    elif ((row0[0] == "O") and (row0[1] == "O") and (row0[2] == "O")):
        print("Player O wins in row 0!")
        done = True
        
    # row 1
    elif ((row1[0] == "X") and (row1[1] == "X") and (row1[2] == "X")):
        print("Player X wins in row 1!")
        done = True
    elif ((row1[0] == "O") and (row1[1] == "O") and (row1[2] == "O")):
        print("Player O wins in row 1!")
        done = True

    # row 2
    elif ((row2[0] == "X") and (row2[1] == "X") and (row2[2] == "X")):
        print("Player X wins in row 2!")
        done = True
    elif ((row2[0] == "O") and (row2[1] == "O") and (row2[2] == "O")):
        print("Player O wins in row 2!")
        done = True

    
    # column 0
    elif ((row0[0] == "X") and (row1[0] == "X") and (row2[0] == "X")):
        print("Player X wins in column 0!")
        done = True
    elif ((row0[0] == "O") and (row1[0] == "O") and (row2[0] == "O")):
        print("Player O wins in column 0!")
        done = True
        
    # column 1
    elif ((row0[1] == "X") and (row1[1] == "X") and (row2[1] == "X")):
        print("Player X wins in column 1!")
        done = True
    elif ((row0[1] == "O") and (row1[1] == "O") and (row2[1] == "O")):
        print("Player O wins in column 1!")
        done = True
        
    # column 2
    elif ((row0[2] == "X") and (row1[2] == "X") and (row2[2] == "X")):
        print("Player X wins in column 2!")
        done = True
    elif ((row0[2] == "O") and (row1[2] == "O") and (row2[2] == "O")):
        print("Player O wins in column 2!")
        done = True

        
    # first diagonal
    elif ((row0[0] == "X") and (row1[1] == "X") and (row2[2] == "X")):
        print("Player X wins in first diagonal!")
        done = True
    elif ((row0[0] == "O") and (row1[1] == "O") and (row2[2] == "O")):
        print("Player O wins in first diagonal!")
        done = True
        
    # second diagonal
    elif ((row0[2] == "X") and (row1[1] == "X") and (row2[0] == "X")):
        print("Player X wins in second diagonal!")
        done = True
    elif ((row0[2] == "O") and (row1[1] == "O") and (row2[0] == "O")):
        print("Player O wins in second diagonal!")
        done = True

    elif((row0[0] != " ") and (row0[1] != " ") and (row0[2] != " ") and (row1[0] != " ") and (row1[1] != " ") and (row1[2] != " ") and (row2[0] != " ") and (row2[1] != " ") and (row2[2] != " ")):
        print("Draw!!")
        done = True
        
# After the while loop finishes, print the final board and game-over message. The first one has been done for you. Complete the code for the board.
print("   -0-1-2-")

print("0: |" + row0[0] + "|" + row0[1] + "|" + row0[2] + "|")
print("   -------")
print("1: |" + row1[0] + "|" + row1[1] + "|" + row1[2] + "|")
print("   -------")
print("2: |" + row2[0] + "|" + row2[1] + "|" + row2[2] + "|")
print("")
print("GAME OVER")
