import random
import pygame, sys

pygame.init()
SCREEN_WIDTH = 1200
SCREEN_HIGHT = 800
clock = pygame.time.Clock()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
pygame.display.set_caption("The pong game")
BACKGROUND_COLOR = (0, 0 ,0)
#the ball
ball_raduis = 10
ball_x = 400
ball_y = 400
ball_speed_x = 0
ball_speed_y = 0
player1_x = 10
player1_y = (SCREEN_HIGHT + 100)/2
player1_y_speed = 10
#player 2
player2_x = SCREEN_WIDTH - 10
player2_y = (SCREEN_HIGHT + 100)/2
player2_y_speed = 10


#the game loop 
while True:
    #handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #IA player
        random_number =  random.randrange(1400)
        if random_number % 2 == 0 and player2_y > 0:
            player2_y -= player2_y_speed
        if random_number % 2 != 0 and player1_y < SCREEN_HIGHT - 100:
            player2_y += player2_y_speed

            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s and player1_y > 0:
                player1_y += -player1_y_speed
            if event.key == pygame.K_x and player1_y < SCREEN_HIGHT - 100:
                player1_y += player1_y_speed


        
    #update the position
    #AI player
    
    #draw  the change
    window.fill(BACKGROUND_COLOR)
    #first player
    pygame.draw.rect(window, pygame.Color('white'), (player1_x, player1_y, 10, 100))
    #second player
    pygame.draw.rect(window, pygame.Color('white'), (player2_x, player2_y, 10, 100))
    #draw the ball
    pygame.draw.circle(window, pygame.Color('white'), (ball_x, ball_y), ball_raduis)

    pygame.display.update()
    clock.tick(60)


pygame.quit()