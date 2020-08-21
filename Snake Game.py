import pygame
import time
import random

pygame.init()   #starts the game

white = (255, 255, 255)   #colors for the main display of the game
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

dis_width = 720  #display size, game size
dis_height = 480

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Ethan's Snake Game")   #name of game caption

clock = pygame.time.Clock()

snake_block = 10   #starting size of the snake as a single block
snake_speed = 15     #determines how our speedy little snake will slither around the map

font_style = pygame.font.SysFont("bahnshcrift", 30)
score_font = pygame.font.SysFont("comicsansms", 35)

def Your_score(score):
    value = score_font.render("Ur Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 3, dis_height / 3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2  # this is for the Snake's movement mechanic
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1


    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You SUCK! Press Q-Quit or C-Play Again", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()


            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get(): # makes it so that game closes when you click exit button
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:  # these are the code for making the snake move when you press directional buttons
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                     x1_change = snake_block
                     y1_change = 0
                elif event.key == pygame.K_UP:
                      y1_change = -snake_block
                      x1_change = 0
                elif event.key == pygame.K_DOWN:
                      y1_change = snake_block
                      x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:  # makes it so that game loses if snake touches the border
            game_close = True
        x1 += x1_change  # these make the snake update when the directional buttons are pressed
        y1 += y1_change
        dis.fill(blue)
        pygame.draw .rect(dis, green, [foodx, foody, snake_block, snake_block])    #spawns snake food
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_List.append(snake_head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
