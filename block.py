from colors import Colors
import pygame
from position import Position

class Block:

    def __init__(self, id):
        self.column_offset = 0
        self.row_offset = 0
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.rotation_state = 0
        self.colors = Colors.get_cell_colors()

    def draw(self, screen):
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(tile.column * self.cell_size + 1, tile.row * self.cell_size + 1, self.cell_size -1, self.cell_size -1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)

    def move(self, rows, columns):
        self.row_offset += rows 
        self.column_offset += columns

    def get_cell_positions(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for tile in tiles:
            position = Position(tile.row + self.row_offset, tile.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles
    
    def rotate(self):
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0    

    def undo_rotation(self):
        self.rotation_state -= 1
        if self.rotation_state == -1:
            self.rotation_state = (len(self.cells) - 1)