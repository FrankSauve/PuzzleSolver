from Puzzle import Puzzle
from DFS import DFS
from BFS import BFS
from A_Star import AStar


# Asks the user for the initial puzzle
input_puzzle = input("Enter the board separated by commas: ").replace(" ", "").split(",")

option = input("Which algorithm do you want to use? (1,2,3)\n1. DFS \n2. BFS \n3. A*\n")

# Converts to int
input_puzzle = list(map(int, input_puzzle))

puzzle = Puzzle(input_puzzle)

# Check if puzzle is solvable
if len(puzzle.puzzle) < 2:
    raise Exception("Invalid puzzle size: Puzzles must be at least two tiles large.\nExiting Program...")
if not puzzle.is_tiled_correctly():
    raise Exception("Incorrect tile values were provided. \nExiting Program...")
puzzle.goal_gen()
if not puzzle.is_puzzle_solvable():
    option_continue = input("This puzzle may not be solvable, do you want to continue? (Y/N)\n")
    if option_continue == 'N' or option_continue == 'n':
        print("Exiting Program...")
        exit()
puzzle.set_rows_and_columns()

if option == "1":
    dfs = DFS(puzzle)
    dfs.search()
elif option == "2":
    bfs = BFS(puzzle)
    bfs.search()
elif option == "3":
    a_star = AStar(puzzle)
    a_star.search()
else:
    raise Exception("Invalid option. Option must be (1,2,3)")



