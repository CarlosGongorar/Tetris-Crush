import pygame;
import sys;
from game import Game

pygame.init();
backgroundcolor = (0, 14, 85);

screen = pygame.display.set_mode((300, 600));

pygame.display.set_caption("Tetris Crush");

clock = pygame.time.Clock();

game = Game();

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            sys.exit();

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pass
            elif event.key == pygame.K_DOWN:
                game.move_down();
            elif event.key == pygame.K_LEFT:
                game.move_left();
            elif event.key == pygame.K_RIGHT:
                game.move_right();
            elif event.key == pygame.K_SPACE:
                game.rotate();
    # Drawing

    screen.fill(backgroundcolor);
    game.draw(screen);

    pygame.display.update();
    clock.tick(60);
