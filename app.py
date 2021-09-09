from flask import Flask, render_template, request



#Valid() function,which checks if num can be place in the cell indicated by row and col

 
def Valid(board, row, col, num):
 
    #checking row
    for x in range(9):
        if board[row][x] == num:
            return False
 
    #checking column
    for x in range(9):
        if board[x][col] == num:
            return False
 
    #get top-left corner
    c_row = row - row%3
    c_col = col - col%3
 
    #check 3x3 square
    for x in range(c_row, c_row+3):
        for y in range(c_col, c_col+3):
            if board[x][y] == num:
                return False
 
    #return True if none of the cases above returns False
    return True


# Boardsolver() function, which solves the Sudoku board using recursion
 
def Boardsolver(board):
    for x in range(9):
        for y in range(9):
            if board[x][y] == 0:
                for num in range(1,10):
                    if Valid(board, x, y, num):
                        board[x][y] = num
                        result = Boardsolver(board)
                        if result == True:
                            return True
                        else:
                            board[x][y] = 0
                return False
    return True

app = Flask(__name__)

@app.route("/")
def index():
    puzzle = [['' for x in range(9)] for x in range(9)]
    return render_template("sudoku.html", puzzle=puzzle, message="Solve Puzzle")


@app.route("/results", methods=["POST"])
def process():
    
    cells = request.form.getlist("cells[]", type=int)

    if 0 in cells:
        puzzle = []
        for x in range(9):
            puzzle.append(cells[x*9: (x+1)*9])
        Boardsolver(puzzle)
        return render_template("sudoku.html", puzzle=puzzle, message="Reset Board")
    else:
        puzzle = [['' for x in range(9)] for x in range(9)]
        return render_template("sudoku.html", puzzle=puzzle, message="Solve Puzzle")

if __name__ == "__main__":
    app.run(debug=True)



