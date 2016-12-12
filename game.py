import pygame
import sys
from snake import *

#colors
white = (255, 255, 255)
black = (0, 0, 0)

def main():
    #initializations
    pygame.init()
    WIDTH = 800
    HEIGHT = 600
    TICK_RATE = 9
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake')
    screen.fill(white)
    pygame.display.update()
    clock = pygame.time.Clock()
    snake = Snake(WIDTH/2, HEIGHT/2) #initialize player

    while True:
        clock.tick(TICK_RATE)
        handleEvents(snake)                 # read inputs
        snake.move()                        # update snake position
        screen.fill(white)
        render(screen, snake)          # draw snake
        pygame.display.update()

        print(snake.length)
        snake.getSegments()

def handleEvents(snake):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #exit game
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN: # control direction
            print(event.type)
            if event.key == pygame.K_LEFT:
                snake.changeDirection("left")
            elif event.key == pygame.K_RIGHT:
                snake.changeDirection("right")
            elif event.key == pygame.K_UP:
                snake.changeDirection("up")
            elif event.key == pygame.K_DOWN:
                snake.changeDirection("down")

def render(screen, snake):
    s = snake.head
    while s is not None:
        pygame.draw.circle(screen, black, (s.x, s.y), snake.radius, 0)
        s = s.next


if __name__ == "__main__":
    main()
