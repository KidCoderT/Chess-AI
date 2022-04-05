import sys
import pygame
import random

pygame.init()

width, height = 720, 720
tile_size = 90

DISPLAY = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chess")

clock = pygame.time.Clock()
index_font = pygame.font.SysFont(None, 20)


def draw_board():
    def draw_square(color: tuple, pos: dict): return pygame.draw.rect(
        DISPLAY, color, (pos["x"], pos["y"], tile_size, tile_size))

    for file in range(8):
        for rank in range(8):
            is_white = (file + rank) % 2 != 0
            square_color = (232, 237, 249) if is_white else (183, 192, 216)

            position = {"x": tile_size * file, "y": tile_size * rank}
            draw_square(square_color, position)

            position = {"x": tile_size * file + tile_size / 2,
                        "y": tile_size * rank + tile_size / 2}
            text = index_font.render(
                str(8 * rank + file), False, (0, 0, 0))
            rect = text.get_rect(center=(position["x"], position["y"]))
            DISPLAY.blit(text, rect.topleft)


while True:
    DISPLAY.fill((0, 0, 0))
    draw_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)
