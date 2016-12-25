import pygame
import sys
import time
from snake import *
from food import *

#colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
snake_color = (random.randint(0, 255), random.randint(0,255), random.randint(0,255))

WIDTH = 640 #40 segments wide
HEIGHT = 480 #30 segments tall
TICK_RATE = 10

def main():
    #initializations
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake')
    screen.fill(white)
    pygame.display.update()
    clock = pygame.time.Clock()
    snake = Snake(WIDTH / 2, HEIGHT - 8) #initialize player
    food = Food()                        #initialize food
    food.setPosition(snake)

    #display instructions
    instructions(screen)

    while True:
        clock.tick(TICK_RATE)
        handleEvents(snake)                 # read inputs
        snake.move()                        # update snake position
        snake.eat(food)
        screen.fill(white)
        render(screen, snake, food)          # draw snake
        pygame.display.update()

        if snake.collide(WIDTH, HEIGHT):
            finalScore(screen, snake)
            if reset():
                snake = Snake(WIDTH/2, HEIGHT - 8)


def instructions(screen):
    '''Display insructions to user'''
    #header
    font = pygame.font.SysFont("freesansbold.ttf", 50, bold=True)
    header_width, header_height = font.size("SNAKE")
    header = font.render("SNAKE", False, black)
    screen.blit(header, (WIDTH/2 - header_width/2, HEIGHT/2 - 25))

    #instructions
    font = pygame.font.SysFont("freesansbold.ttf", 30)
    instr_text = "Use direction keys for movement"
    instr_width, instr_height = font.size(instr_text)
    instr = font.render(instr_text, False, black)
    screen.blit(instr, (WIDTH/2 - instr_width/2, HEIGHT/2 + 20))

    #continue
    cont_text = "Press any key to play"
    cont_width, cont_height = font.size(cont_text)
    cont = font.render(cont_text, False, black)
    screen.blit(cont, (WIDTH/2 - cont_width/2, HEIGHT/2 + 40))

    pygame.display.update()

    #wait for play
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return


def handleEvents(snake):
    '''Handle pygame events'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #exit game
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN: # control direction
            if event.key == pygame.K_LEFT:
                snake.changeDirection("left")
            elif event.key == pygame.K_RIGHT:
                snake.changeDirection("right")
            elif event.key == pygame.K_UP:
                snake.changeDirection("up")
            elif event.key == pygame.K_DOWN:
                snake.changeDirection("down")


def render(screen, snake, food):
    '''Display food and snake on screen'''
    #draw food
    pygame.draw.circle(screen, red, (food.x, food.y), food.radius, 0)

    s = snake.head
    while s is not None:
        pygame.draw.circle(screen, black, (s.x, s.y), snake.radius, 0)
        s = s.next


def finalScore(screen, snake):
    '''Display 'Game Over' screen'''
    # game over
    font = pygame.font.SysFont("freesansbold.ttf", 50, bold=True)
    text_width, text_height = font.size("Game Over")
    endgame = font.render("Game Over", False, black)
    screen.blit(endgame, (WIDTH/2 - text_width/2, HEIGHT/2 - text_height/2))

    # score
    font = pygame.font.SysFont("freesansbold.ttf", 40)
    score_text = "Score: " + str(snake.length)
    score_width, score_height = font.size(score_text)
    score = font.render(score_text, False, black)
    screen.blit(score, (WIDTH/2 - score_width/2, HEIGHT/2 + text_height/2))

    #play again
    play_text = "Press any key to play again"
    font = pygame.font.SysFont("freesansbold.ttf", 25)
    text_width, text_height = font.size(play_text)
    play = font.render(play_text, False, black)
    screen.blit(play, (WIDTH/2 - text_width/2, HEIGHT/2 + 3*text_height))

    pygame.display.update()
    time.sleep(1.5)


def reset():
    '''Pause game for user input'''
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return True



if __name__ == "__main__":
    main()
