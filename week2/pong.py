import pygame, sys, random

# imports pygmae allows to access more functionality

#######General set-up######

pygame.init()
#initiates all pygame modules
#REQUIRED in all pgame projects

clock = pygame.time.Clock()

screen_width = 880
screen_height = 660

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("PONG")

###FUNCTIONSS##
def ball_restart():
    global ball_speed_x, ball_speed_y, player_speed, opponent_speed
    
    
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_y *= random.choice((1, -1)) 
    ###define the speed of the objets using variables##
    ###Ball collision with borders
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()

        ###Ball collision with players##
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def ball_animation():
    global ball_speed_x, ball_speed_y, player_speed, opponent_speed
    ###ANIMATIONS###
    ball_speed_x = 7
    ball_speed_y = 7
    player_speed = 0
    opponent_speed = 7
    
    ball.x += ball_speed_x
    ball.y += ball_speed_y



####playeranimations###
def player_animation():
    player.y += player_speed

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
                player_speed += 7
        if event.key == pygame.K_UP:
                player_speed += 7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7
    
        if player.top <= 0:
            player.top = 0
        if player.bottom >= screen_height:
            player.bottom = screen_height

def opponent_animation():
    ##if the opponent object is above the top, then return to top###
    ###if the opponent object is below the bottom, then return to the bottom ##
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed

    if opponent.top <= 0:
            player.top = 0
    if opponent.bottom >= screen_height:
            player.bottom = screen_height

####GAME RECTANGLES####
ball = pygame.Rect(screen_width/2 - 15, screen_height/2, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 -70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 -70, 10, 140)

###COLOURSSS###
bg_color = pygame.Color("grey12")
light_grey = (200, 200, 200)



#------------------------

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    ball_animation()
    player_animation()
    opponent_animation()


    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))
    
    pygame.display.flip()
    clock.tick(30)
