from Solver import Solver
import tkinter as tk



HEIGHT = 500
WIDTH = 700

root = tk.Tk()
root.title("Sudoku Solver")

frame = tk.Frame(root, bg="#80c1ff")
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

# e = tk.Entry(root, width=35, borderwidth=5)
# e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
# e.insert(0, "0")

grid = list()
for y in range(9):
    row = list()
    for x in range(9):
        e = tk.Entry(frame, width=5, borderwidth=5)
        e.insert(0, "0")
        row.append(e)
    grid.append(row)


i = 0
for row in grid:
    j = 0
    for e in row:
        e.grid(row=i, column=j, columnspan=1, padx=10, pady=10)
        j += 1
    i +=1


def solve():
    sudo_grid = list()
    for y in range(9):
        sudo_grid.append([])
        for x in range(9):
            sudo_grid[y].append(int(grid[y][x].get()))
    
    print(sudo_grid)

    s = Solver(sudo_grid)
    s.solve()
    for y_idx, y in enumerate(s.board):
        for x_idx, x in enumerate(y):
            replace_entry(y_idx, x_idx, x)
    
def replace_entry(y, x, n):
    grid[y][x].delete(0)
    grid[y][x].insert(0, n)

button = tk.Button(root, text="Solve", command=solve)
button.pack(fill="both")




root.mainloop()

def main():
    pass

if __name__ == "__main__":
    main()