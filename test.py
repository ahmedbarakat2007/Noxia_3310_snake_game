import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (45, 64, 33)
blue = (106, 138, 87)
foord = (77, 89, 72)

programIcon = pygame.image.load('icon.png')

pygame.display.set_icon(programIcon)
 
dis_width = 600
dis_height = 400
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Nokia 3310 Snake By Ahmed Barakat')
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 15
 
font_style = pygame.font.Font("slkscr.ttf", 25)
score_font = pygame.font.Font("slkscr.ttf", 35)
 
 
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, black)
    dis.blit(value, [0, 0])
 
 
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 9, dis_height / 6])
def message1(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 7, dis_height / 4])
def message2(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
def message3(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 12, dis_height / 2])
def message4(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg,[20, 300])

 
def gameLoop():
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
        
 
        while game_close == True:
            dis.fill(blue)
            message("Game Over", black)
            message1("(C) for Play again", black)
            message2("(Q) for Quit", black)
            message3("THX for Playing", black)
            message4("Made by Ahmed Barakat", black)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
 
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
                elif event.key == pygame.K_d:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_w:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_s:
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_a:
                    x1_change = -snake_block
                    y1_change = 0
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, foord, [foodx, foody, snake_block, snake_block])
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
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()