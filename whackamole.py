import random

import pygame


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        x,y = 0,0
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    click_location = event.pos
                    square_x = click_location[0]//32
                    square_y = click_location[1]//32
                    if square_x == x and square_y ==y:
                        x = random.randrange(1,20)
                        y = random.randrange(1,16)
            screen.fill("light green")
            for i in range(0,20):
                pygame.draw.line(screen, pygame.Color(0, 0, 0), (32*i, 0), (32*i, 512))
            for j in range(0,16):
                pygame.draw.line(screen, pygame.Color(0, 0, 0), (0, 32*j), (640, 32*j))
            screen.blit(mole_image, mole_image.get_rect(topleft=(x*32+4, y*32+5)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
