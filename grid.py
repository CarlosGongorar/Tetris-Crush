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

    def is_row_full(self, row):
        for col in range(self.num_cols):
            if self.grid[row][col] == 0:
                return False
        return True

    def clear_row(self, row):
        for col in range(self.num_cols):
            self.grid[row][col] = 0
    
    def move_row_down(self, row, num_rows):
        for col in range(self.num_cols):
            self.grid[row + num_rows][col] = self.grid[row][col]
            self.grid[row][col] = 0
    
    def clear_full_rows(self):
        completed = 0
        for row in range(self.num_rows -1, -1, -1):
            if self.is_row_full(row):
                self.clear_row(row);
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed);
        return completed

    def reset(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.grid[row][col] = 0

    def clear_matches(self):
        to_clear = set()         # Posiciones específicas a limpiar (para secuencias de 3 o 4)
        colors_to_clear = set()  # Colores que se deben limpiar en todo el tablero (por match de 5)
        clear_all_flag = False   # Bandera para indicar que se formó un match de 6 (o más)

        # Verificar coincidencias horizontales
        for row in range(self.num_rows):
            count = 1
            start_col = 0
            for col in range(1, self.num_cols):
                if self.grid[row][col] != 0 and self.grid[row][col] == self.grid[row][col - 1]:
                    count += 1
                else:
                    if self.grid[row][col - 1] != 0:
                        color = self.grid[row][col - 1]
                        if count >= 6:
                            clear_all_flag = True
                        elif count == 5:
                            colors_to_clear.add(color);
                        elif count == 4:
                            # Regla para 4 en línea horizontal: eliminar la fila completa
                            for c in range(self.num_cols):
                                to_clear.add((row, c));
                        elif count == 3:
                            # Regla para 3 en línea: eliminar solo la secuencia
                            for c in range(start_col, col):
                                to_clear.add((row, c));
                    count = 1
                    start_col = col
            # Procesar la última secuencia de la fila
            if self.grid[row][self.num_cols - 1] != 0:
                color = self.grid[row][self.num_cols - 1]
                if count >= 6:
                    clear_all_flag = True
                elif count == 5:
                    colors_to_clear.add(color);
                elif count == 4:
                    for c in range(self.num_cols):
                        to_clear.add((row, c));
                elif count == 3:
                    for c in range(start_col, self.num_cols):
                        to_clear.add((row, c));

        # Verificar coincidencias verticales
        for col in range(self.num_cols):
            count = 1
            start_row = 0
            for row in range(1, self.num_rows):
                if self.grid[row][col] != 0 and self.grid[row][col] == self.grid[row - 1][col]:
                    count += 1
                else:
                    if self.grid[row - 1][col] != 0:
                        color = self.grid[row - 1][col]
                        if count >= 6:
                            clear_all_flag = True
                        elif count == 5:
                            colors_to_clear.add(color);
                        elif count == 4:
                            # Regla para 4 en línea vertical: eliminar la columna completa
                            for r in range(self.num_rows):
                                to_clear.add((r, col));
                        elif count == 3:
                            for r in range(start_row, row):
                                to_clear.add((r, col));
                    count = 1
                    start_row = row
            # Procesar la última secuencia de la columna
            if self.grid[self.num_rows - 1][col] != 0:
                color = self.grid[self.num_rows - 1][col]
                if count >= 6:
                    clear_all_flag = True
                elif count == 5:
                    colors_to_clear.add(color);
                elif count == 4:
                    for r in range(self.num_rows):
                        to_clear.add((r, col));
                elif count == 3:
                    for r in range(start_row, self.num_rows):
                        to_clear.add((r, col));

        # Regla 6: Si se formó un match de 6 o más, se limpia todo el tablero.
        if clear_all_flag:
            cleared = sum(1 for row in range(self.num_rows) for col in range(self.num_cols) if self.grid[row][col] != 0)
            for row in range(self.num_rows):
                for col in range(self.num_cols):
                    self.grid[row][col] = 0
            return cleared

        # Regla 5: Para cada color que tenga un match de 5, se eliminan todas las cajas de ese color.
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if self.grid[row][col] in colors_to_clear:
                    to_clear.add((row, col));

        # Eliminar (poner a 0) todas las celdas marcadas
        cleared = len(to_clear);
        for (row, col) in to_clear:
            self.grid[row][col] = 0

        return cleared

    def apply_gravity(self):
        moved = True
        while moved:
            moved = False
            # Recorremos desde la penúltima fila hasta la primera
            for row in range(self.num_rows - 2, -1, -1):
                for col in range(self.num_cols):
                    if self.grid[row][col] != 0 and self.grid[row + 1][col] == 0:
                        # Mover el bloque hacia abajo
                        self.grid[row + 1][col] = self.grid[row][col]
                        self.grid[row][col] = 0
                        moved = True
    
    def draw(self, screen):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                cell_value = self.grid[row][col]
                cell_rect = pygame.Rect(col*self.cell_size + 11, row*self.cell_size + 11, self.cell_size - 1, self.cell_size - 1);
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect);