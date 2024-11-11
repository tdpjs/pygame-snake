import pygame
import random
import sys  

pygame.init()

screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)

snake_block = 10
snake_speed = 15

font = pygame.font.SysFont(None, 35)

def display_message(msg, color, pos):
    msg_surface = font.render(msg, True, color)
    screen.blit(msg_surface, pos)

def game_loop():
    game_over = False
    game_close = False

    x1, y1 = screen_width / 2, screen_height / 2
    x1_change, y1_change = 0, 0

    snake = []
    snake_length = 1
    score = 0  

    
    food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

    clock = pygame.time.Clock()
    current_direction = "STOP"  

    while not game_over:
        while game_close:
            screen.fill(black)
            display_message("You Lost! Press Q-Quit or C-Play Again", red, [screen_width / 6, screen_height / 3])
            display_message(f"Score: {score}", white, [screen_width / 2 - 40, screen_height / 2])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and current_direction != "RIGHT":
                    x1_change, y1_change = -snake_block, 0
                    current_direction = "LEFT"
                elif event.key == pygame.K_RIGHT and current_direction != "LEFT":
                    x1_change, y1_change = snake_block, 0
                    current_direction = "RIGHT"
                elif event.key == pygame.K_UP and current_direction != "DOWN":
                    x1_change, y1_change = 0, -snake_block
                    current_direction = "UP"
                elif event.key == pygame.K_DOWN and current_direction != "UP":
                    x1_change, y1_change = 0, snake_block
                    current_direction = "DOWN"

        x1 += x1_change
        y1 += y1_change

        if x1 >= screen_width:
            x1 = 0
        elif x1 < 0:
            x1 = screen_width - snake_block
        if y1 >= screen_height:
            y1 = 0
        elif y1 < 0:
            y1 = screen_height - snake_block

        screen.fill(black)
        
        pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])
        
        snake_head = [x1, y1]
        snake.append(snake_head)
        
        if len(snake) > snake_length:
            del snake[0]

        for block in snake[:-1]:
            if block == snake_head:
                game_close = True

        for block in snake:
            pygame.draw.rect(screen, green, [block[0], block[1], snake_block, snake_block])

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
            snake_length += 1
            score += 1  

        clock.tick(snake_speed)

    pygame.quit()
    sys.exit()  

game_loop()
