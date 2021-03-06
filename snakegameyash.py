import pygame
from pygame import mixer
import time
import random

pygame.init()

white = (255, 255, 255)  # constants defined to be used in the code ahead
# These parameters are color code for red,green and blue respectively
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 1100  # width of display screen
dis_height = 600  # height of display screen


pygame.display.set_mode()
bgimg = pygame.image.load("tree.jpg")
bgimg = pygame.transform.scale(bgimg, (dis_width, dis_height)).convert_alpha()



# creating window with width and height as parameters
dis = pygame.display.set_mode((dis_width, dis_height))

# providing caption at the top of the window
pygame.display.set_caption('Snake Game by Yash vardhan')

# to keep tack of time we built an object 'clock' for predefined function clock()
clock = pygame.time.Clock()

snake_block = 10  # size of block
snake_speed = 20  # speed of snake

font_style = pygame.font.SysFont(
    "bahnschrift", 25)  # for font play again or quit
score_font = pygame.font.SysFont("calibri", 25)  # for font of score


def Your_score(score):  # method for score
    value = score_font.render("Your Score: " + str(score), True, black)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 3, dis_height / 2])


def gameLoop():
    mixer.music.load("background.wav")
    mixer.music.play(-1)

    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    

    while not game_over:
        dis.blit(bgimg, (0, 0))
        while game_close == True:
            dis.fill(black)
            message("You Lost! Press P-Play Again or Q-Quit", yellow)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
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

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(
                0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(
                0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
