import pygame

default_colors = [
    (0, 0, 0),
    (255, 255, 255),
    (128, 128, 128),
    (192, 192, 192),
    (128, 0, 0),
    (255, 0, 0),
    (128, 128, 0),
    (255, 255, 0),
    (0, 128, 0),
    (0, 255, 0),
    (0, 128, 128),
    (0, 255, 255),
    (0, 0, 128),
    (0, 0, 255),
    (128, 0, 128),
    (255, 0, 255),
    (128, 128, 64),
    (255, 255, 128),
    (0, 64, 64),
    (0, 255, 128),
    (0, 128, 255),
    (128, 255, 255),
    (0, 64, 128),
    (128, 128, 255),
    (64, 0, 255),
    (255, 0, 128),
    (128, 64, 0),
    (255, 128, 64),
]

size_block = 20

def draw_color_picker(screen):

    screen_height = screen.get_height()
    screen_width = screen.get_width()
    pygame.draw.rect(screen,(212,208,200),(0,screen_height-55,screen_width,55),0)
    pygame.draw.rect(screen,(255,255,255),(3,screen_height-52,350,49),0)

    for index, default_color in enumerate(default_colors):
        if index % 2 == 0:
            
            start_point = (5 + (index/2 * 5) + (index/2 * size_block) , screen_height - 5  - size_block - size_block - 5)

            pygame.draw.rect(
                screen,
                default_color,
                (start_point[0], start_point[1], size_block, size_block),
                0,
            )

        else:

            start_point = (5 + ((index-1)/2 * 5) + ((index-1)/2 * size_block) , screen_height - 5  - size_block)

            pygame.draw.rect(
                screen,
                default_color,
                (start_point[0], start_point[1], size_block, size_block),
                0,
            )

        
        pygame.draw.line(screen, (0,0,0), start_point, (start_point[0], start_point[1] + size_block))
        pygame.draw.line(screen, (0,0,0), start_point, (start_point[0]+ size_block, start_point[1] ))

        pygame.draw.line(screen, (212,208,200), (start_point[0] + size_block, start_point[1] + size_block), (start_point[0], start_point[1] + size_block))
        pygame.draw.line(screen, (212,208,200), (start_point[0] + size_block, start_point[1] + size_block), (start_point[0] + size_block, start_point[1] ))