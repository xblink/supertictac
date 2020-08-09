#!/urs/bin/env python3

import game

"""supertictac.py - super-tictactoe console implementation"""
def main():
    g = game.Game()
    
    while not g.won:
        print_game(g)  
        nextMove = 0

        while nextMove not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            nextMove = input("Move? ")
            if nextMove not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                print ("Invalid selection. (0-9)")
                nextMove = 0
            
        g.play(nextMove)
    print_game(g)
    print(f"Congradulations! {g._whosMove} wins!")

        
    

def print_game(g):
    board = g.get_board()
    headerString = build_header_ascii(g)
    boardString = build_board_ascii(board)
    print(headerString)
    print(boardString)

def build_header_ascii(g):
    finalOut = f"\nsupertictactoe | move: {g.currentMove} | active grid: {g.activeGrid}\n"
    finalOut += "-" * 43

    return finalOut
    
def build_board_ascii(board):
    finalOut = ""
    for j in range(3):
        for i in range(3):
            line = "  "
            line += " | ".join(board[3*j][3*i:3*i+3]) + "      "
            line += " | ".join(board[3*j+1][3*i:3*i+3]) + "      "
            line += " | ".join(board[3*j+2][3*i:3*i+3]) + "\n"
            if i < 2:
                line += " ---+---+---    ---+---+---    ---+---+---\n"
            finalOut += line
        
        line = ""
        if j < 2:
            line += "\n"
        finalOut += line

    return finalOut

if __name__ == "__main__":
    main()