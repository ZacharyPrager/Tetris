import pygame
import sys
from game import Game
pygame.init()

DARK_BLUE = (44, 44, 127)

screen = pygame.Surface((300,600))
container_screen = pygame.display.set_mode((700, 600))

pygame.display.set_caption("Tetrus")
clock = pygame.time.Clock()
game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, game.game_speed)

font = pygame.font.SysFont('Arial', 30)

def draw_score(screen, score):
    pygame.draw.rect(screen, (0, 0, 0), (300, 0, 400, 40))
    text_surface = font.render(f"Score: {score}", True, (255, 255, 255))  
    screen.blit(text_surface, (350, 10))

def draw_level(screen, level):
    pygame.draw.rect(screen, (0, 0, 0), (300, 40, 400, 40))
    text_surface = font.render(f"Level: {level}", True, (255, 255, 255))  
    screen.blit(text_surface, (550, 10))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        keys = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if keys[pygame.K_LEFT] and game.game_over == False:
                game.move_left()
            if keys[pygame.K_DOWN] and game.game_over == False:
                game.move_down()
            if keys[pygame.K_RIGHT] and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
            if event.key == pygame.K_SPACE and game.game_over == False:
                game.fast_fall()
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()
    screen.fill(DARK_BLUE)
    game.draw(screen)
    container_screen.blit(screen, (0, 0))
    draw_score(container_screen, game.score)
    draw_level(container_screen, game.level)

    pygame.display.update()
    clock.tick(60)