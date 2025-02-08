from grid import Grid
from blocks import *
import random
import pygame

class Game:
    def __init__(self):
        self.grid = Grid();
        self.blocks = [LBlock(), JBlock(), IBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block();
        self.next_block = self.get_random_block();
        self.game_over = False;
        self.score = 0;
        self.get_score = pygame.mixer.Sound("songs/tetrisclear.mp3");
        self.game_over_song = pygame.mixer.Sound("songs/gameoversong.mp3");

        pygame.mixer.music.load("songs/theme.mp3");
        pygame.mixer.music.play(-1);
    
    def upadte_score(self, lines_cleared, move_down_points):
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500
        self.score += move_down_points
    
    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [LBlock(), JBlock(), IBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]

        block = random.choice(self.blocks);
        self.blocks.remove(block);
        return block
    
    def move_left(self):
        self.current_block.move(0, -1);
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, 1);
    
    def move_right(self):
        self.current_block.move(0, 1);
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, -1);
    
    def move_down(self):
        self.current_block.move(1, 0);
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(-1, 0);
            self.lock_block();
    
    def rotate(self):
        self.current_block.rotate();
        if not (self.block_inside() and self.block_fits()):
            self.current_block.undo_rotation();
    
    def lock_block(self):
        tiles = self.current_block.get_cell_positions();
        for pos in tiles:
            self.grid.grid[pos.row][pos.column] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block();
        rows_cleared = self.grid.clear_full_rows();
        if rows_cleared > 0:
            self.get_score.play()
            self.upadte_score(rows_cleared, 0);

        match_score = 0
        while True:
            blocks_cleared = self.grid.clear_matches();
            if blocks_cleared == 0:
                break
            if blocks_cleared == 3:
                self.get_score.play();
                match_score += 50
            elif blocks_cleared == 4:
                self.get_score.play();
                match_score += 150
            elif blocks_cleared == 5:
                self.get_score.play();
                match_score += 300
            elif blocks_cleared >= 6:
                self.get_score.play();
                match_score += 600

            self.grid.apply_gravity();

        self.score += match_score

        if self.block_fits() == False:
            self.game_over = True
            self.game_over_song.play();
            pygame.mixer.music.pause();
    
    def block_fits(self):
        tiles = self.current_block.get_cell_positions();
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False
        return True
        
    def block_inside(self):
        tiles = self.current_block.get_cell_positions();
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True

    def reset(self):
        self.grid.reset();
        self.blocks = [LBlock(), JBlock(), IBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block();
        self.next_block = self.get_random_block();
        self.score = 0;
        pygame.mixer.music.play(-1);

    def draw(self, screen):
        self.grid.draw(screen);
        self.current_block.draw(screen, 11, 11);
        if self.next_block.id == 3:
            self.next_block.draw(screen, 307, 290);
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 307, 275);
        else:
            self.next_block.draw(screen, 320, 270);