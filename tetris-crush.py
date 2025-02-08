import pygame;
import sys;
from game import Game
from colors import Colors

pygame.init();

title_font = pygame.Font(None, 40);
score_surface = title_font.render("Score", True, Colors.white);
next_surface = title_font.render("Next", True, Colors.white);
game_over_surface = title_font.render("GAME OVER!", True, Colors.red);

score_rect = pygame.Rect(370, 55, 170, 60);
next_rect = pygame.Rect(370, 215, 170, 180);

screen = pygame.display.set_mode((600, 600));
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

    screen.fill(Colors.background_color);
    screen.blit(score_surface, (415, 20, 70, 50));
    screen.blit(next_surface, (420, 180, 70, 50));

    if game.game_over == True:
        screen.blit(game_over_surface, (365, 450, 50, 50));

    pygame.draw.rect(screen, Colors.details, score_rect, 0, 10);
    pygame.draw.rect(screen, Colors.details, next_rect, 0, 10);
    game.draw(screen);

    pygame.display.update();
    clock.tick(60);
