import pygame
import sys
from snake import *
from food import *

#colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

def main():
    #initializations
    pygame.init()
    WIDTH = 840 #60 segments wide
    HEIGHT = 700 #50 segments tall
    TICK_RATE = 7
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake')
    screen.fill(white)
    pygame.display.update()
    clock = pygame.time.Clock()
    snake = Snake(WIDTH / 2, HEIGHT - 7) #initialize player
    food = Food() # initialize food
    food.setPosition(snake)

    while True:
        clock.tick(TICK_RATE)
        handleEvents(snake)                 # read inputs
        snake.move()                        # update snake position
        snake.eat(food)
        screen.fill(white)
        render(screen, snake, food)          # draw snake
        pygame.display.update()


def handleEvents(snake):
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
    #draw food
    pygame.draw.circle(screen, red, (food.x, food.y), food.radius, 0)

    s = snake.head
    while s is not None:
        pygame.draw.circle(screen, black, (s.x, s.y), snake.radius, 0)
        s = s.next




if __name__ == "__main__":
    main()
