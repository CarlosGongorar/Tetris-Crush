import pygame;
import sys;
from game import Game

pygame.init();
backgroundcolor = (0, 14, 85);

screen = pygame.display.set_mode((300, 600));

pygame.display.set_caption("Tetris Crush");

clock = pygame.time.Clock();

game = Game();

GAME_UPDATE = pygame.USEREVENT

pygame.time.set_timer(GAME_UPDATE, 300);

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            sys.exit();

        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                if event.key == pygame.K_r and game.game_over == True:
                    game.game_over = False
                    game.reset();
            if event.key == pygame.K_UP:
                pass
            elif event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down();
            elif event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left();
            elif event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right();
            elif event.key == pygame.K_SPACE and game.game_over == False:
                game.rotate();

        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down();
    # Drawing

    screen.fill(backgroundcolor);
    game.draw(screen);

    pygame.display.update();
    clock.tick(60);
