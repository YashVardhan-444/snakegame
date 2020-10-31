import pygame
import time
import random
 
pygame.init()
                           
white = (255, 255, 255)    #constants defined to be used in the code ahead
yellow = (255, 255, 102)   #These parameters are color code for red,green and blue respectively
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
dis_width = 1100  #width of display screen
dis_height = 600  #height of display screen
 
dis = pygame.display.set_mode((dis_width, dis_height))  #creating window with width and height as parameters
pygame.display.set_caption('Snake Game by Yash vardhan') #providing caption at the top of the window
 
clock = pygame.time.Clock()#to keep tack of time we built an object 'clock' for predefined function clock()
 
snake_block = 10 #size of block
snake_speed = 20 #speed of snake
 
font_style = pygame.font.SysFont("bahnschrift", 25) #for font play again or quit
score_font = pygame.font.SysFont("calibri", 25) #for font of score 
 
 
def Your_score(score): #method for score
    value = score_font.render("Your Score: " + str(score), True, black)
    dis.blit(value, [0, 0]) #used for displaying the score at top left corner that's why 0,0
 
 
 
def our_snake(snake_block, snake_list): #creating snake
    for x in snake_list:
        pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block]) #providing size and color of the rectangular snake
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 3, dis_height / 2]) #displaying msg at width/3,height/2
 
 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 #random generation of x coordinate
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0 #random generation of y coordinate
 
    while not game_over:
 
        while game_close == True:
            dis.fill(black) #background with black color
            message("You Lost! Press P-Play Again or Q-Quit", yellow) #msg in yellow color
            Your_score(Length_of_snake - 1) 
            pygame.display.update() #to make the display surface actually appear on screen
 
            for event in pygame.event.get(): #creates a queue of events(mouse click or keyboard input)
                if event.type == pygame.KEYDOWN: #if key pressed on keyboard
                    if event.key == pygame.K_q: #if pressed key is q
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p: #if pressed key is p
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: #if pressed key is left arrow key
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT: #if pressed key is right arrow key
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP: #if pressed key is up arrow key
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN: #if pressed key is down arrow key
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0: #game over conditions(boundaries and snake merging in itself)
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block]) # creating food item of red color with foodx and foody as coordinates
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head) #adding one rectangle on eating one food item
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody: #if by chance snake coordinate and food cordinate become same
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed) #for frames per second
 
    pygame.quit() #if event.type.quit is true then this will execute 
    quit() #for exiting the program
 
 
gameLoop() #caling of gameloop
