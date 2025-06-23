from grid import Grid
from blocks import *
import random
class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0
        self.level = 1
        self.total_completed_lines = 0
        self.speeds = {
            1: 717, 2: 633, 3: 550, 4: 467,
            5: 383, 6: 300, 7: 217, 8: 133, 9: 100,
            10: 83, 11: 83, 12: 83,
            13: 67, 14: 67, 15: 67,
            16: 50, 17: 50, 18: 50,
            19: 33, 20: 33, 21: 33, 22: 33, 23: 33,
            24: 33, 25: 33, 26: 33, 27: 33, 28: 33,
            29: 17
        }
        self.game_speed = self.add_speed()

    def get_random_block(self):
        if len(self.blocks) == 0:
                self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)
        
    def move_left(self):
        self.current_block.move(0, -1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, 1)

    def move_right(self):
        self.current_block.move(0, 1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, -1)

    def move_down(self):
        self.current_block.move(1, 0)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(-1, 0)
            self.lock_block()

    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        for pos in tiles:
            self.grid.grid[pos.row][pos.column] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        num_of_completed = self.grid.clear_full_rows()
        self.total_completed_lines += num_of_completed
        self.add_level()
        self.add_score(num_of_completed)
        if self.block_fits() == False:
            self.game_over = True

    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.undo_rotation()

    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True
    
    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False
        return True
    
    def fast_fall(self):
        while True:
            self.current_block.move(1, 0)
            if not self.block_inside() or not self.block_fits():
                self.current_block.move(-1, 0)
                break
        self.lock_block()
        self.move_down()
    
    def add_score(self, completed):
        rows_cleared = completed
        if  rows_cleared == 1: 
            base_score = 100
        elif rows_cleared == 2:
            base_score = 300
        elif rows_cleared == 3:
            base_score = 500
        elif rows_cleared == 4:
            base_score = 700
        else:
            base_score = 0
        base_score = self.level * base_score
        self.score += base_score

    def add_level(self):
        expected_level = (self.total_completed_lines // 10) + 1
        if expected_level > self.level:
            self.level = expected_level
            self.game_speed = self.add_speed()
    
    def add_speed(self):
        return self.speeds[self.level if self.level <= 29 else 29]
    