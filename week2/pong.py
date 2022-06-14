import pygame, sys

# imports pygmae allows to access more functionality

#######General set-up######

pygame.init()
#initiates all pygame modules
#REQUIRED in all pgame projects

clock = pygame.time.Clock()

screen_width = 980
screen_height = 560

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("PONG")

ball = pygame.Rect(screen_width/2 - 15, screen_height/2, 30, 30)

player = pygame.Rect(screen_width - 20, screen_height/2 -70, 10, 140)

opponent = pygame.Rect(10, screen_height/2 -70, 10, 140)

bg_color = pygame.Color("grey12")
light_grey = (200, 200, 200)
#------------------------

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    
    pygame.display.flip()
    clock.tick(60)