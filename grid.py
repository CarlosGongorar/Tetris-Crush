import pygame

class Grid:
    def __init__(self):
        self.num_rows = 18
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = self.get_cell_colors();

    def draw_grid(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                print(self.grid[row][col], end=" ");
            print();

    def get_cell_colors(self):
        dark_grey = (26, 31, 40);
        green = (47, 230, 23);
        red = (232, 18, 18);
        orange = (226, 18, 18);
        yellow = (237, 234, 4);
        purple = (166, 0, 247);
        cyan = (21, 204, 209);
        blue = (13, 26, 216);
        
        return [dark_grey, green, red, orange, yellow, purple, cyan, blue]
    
    def draw(self, screen):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                cell_value = self.grid[row][col]
                cell_rect = pygame.Rect(col*self.cell_size + 1, row*self.cell_size + 1, self.cell_size - 1, self.cell_size - 1);
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect);