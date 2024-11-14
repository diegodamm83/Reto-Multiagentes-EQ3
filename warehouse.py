def generate_warehouse_layout(rows=75, cols=75):
    # Initialize empty maze with floors
    maze = [['F' for _ in range(cols)] for _ in range(rows)]
    
    # Add border walls
    for row in range(rows):
        for col in range(cols):
            if row == 0 or col == 0 or row == rows - 1 or col == cols - 1:
                maze[row][col] = 'B'

    # Rack dimensions and spacing
    rack_width = 2
    standard_spacing = 2
    
    # Top section: 17 long racks
    start_col = 5
    for i in range(12):
        col = start_col + (i * (rack_width + standard_spacing))
        if col + rack_width < cols - 1:
            for row in range(4, 20):
                for w in range(rack_width):
                    maze[row][col + w] = 'B'
                    if row % 2 == 0:  # Add internal divisions
                        maze[row][col + w] = 'B'

    # Middle section: 20 racks
    for i in range(15):
        col = start_col + (i * (rack_width + standard_spacing))
        if col + rack_width < cols - 1:
            for row in range(24, 38):
                for w in range(rack_width):
                    maze[row][col + w] = 'B'
                    if row % 2 == 0:  # Add internal divisions
                        maze[row][col + w] = 'B'

    # Bottom section: 17 racks
    bottom_start = start_col + (3 * (rack_width + standard_spacing))
    for i in range(12):
        col = bottom_start + (i * (rack_width + standard_spacing))
        if col + rack_width < cols - 1:
            for row in range(42, 54):
                for w in range(rack_width):
                    maze[row][col + w] = 'B'
                    if row % 2 == 0:
                        maze[row][col + w] = 'B'

    # Top right corner - 3 vertical racks (now half height and moved left)
    top_right_start_col = cols - 22  # Changed from cols - 15 to cols - 20
    for i in range(3):
        col = top_right_start_col + (i * (rack_width + standard_spacing))
        if col + rack_width < cols - 1:
            for row in range(12, 20):
                for w in range(rack_width):
                    maze[row][col + w] = 'B'
                    if row % 2 == 0:
                        maze[row][col + w] = 'B'

    # Add small terminal in bottom left
    for row in range(48, 50):
        for col in range(6, 12):
            maze[row][col] = 'B'

    return maze

def save_maze(maze, filename):
    with open(filename, 'w') as file:
        for row in maze:
            file.write("".join(row) + "\n")

def display_maze(maze):
    symbols = {
        'B': '█',  # Wall/Rack
        'F': ' ',  # Floor
        'G': '◎'   # Goal (if present)
    }
    
    for row in maze:
        print(''.join(symbols[cell] for cell in row))

if __name__ == '__main__':
    maze = generate_warehouse_layout()
    save_maze(maze, 'warehouse.txt')
    print("Precise Warehouse Layout Preview:")
    display_maze(maze)
    print("\nMaze has been saved to 'warehouse.txt'")