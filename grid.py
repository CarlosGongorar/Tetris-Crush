import pygame
from colors import Colors

class Grid:
    def __init__(self):
        self.num_rows = 18
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = Colors.get_cell_colors();

    def draw_grid(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                print(self.grid[row][col], end=" ");
            print();
    
    def is_inside(self, row, col):
        if row >= 0 and row < self.num_rows and col >= 0 and col < self.num_cols:
            return True
        return False
    
    def is_empty(self, row, col):
        if self.grid[row][col] == 0:
            return True
        return False

    def draw(self, screen):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                cell_value = self.grid[row][col]
                cell_rect = pygame.Rect(col*self.cell_size + 1, row*self.cell_size + 1, self.cell_size - 1, self.cell_size - 1);
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect);