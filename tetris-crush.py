import pygame;
import sys;
from grid import Grid

pygame.init();
backgroundcolor = (0, 14, 85)

screen = pygame.display.set_mode((300, 600))

pygame.display.set_caption("Tetris Crush")

clock = pygame.time.Clock()

game_grid = Grid()

game_grid.grid[0][0] = 1
game_grid.grid[9][5] = 4
game_grid.grid[1][8] = 7

game_grid.draw_grid()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            sys.exit();
    
    # Drawing

    screen.fill(backgroundcolor)
    game_grid.draw(screen)

    pygame.display.update();
    clock.tick(60);
