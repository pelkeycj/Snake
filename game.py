import pygame
from snake import *

#colors
white = (255, 255, 255)
black = (0, 0, 0)

def main():
    #initializations
    pygame.init()
    WIDTH = 800
    HEIGHT = 600
    gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake')
    gameDisplay.fill(white)
    pygame.display.update()
    clock = pygame.time.Clock()
    snake = Snake(WIDTH/2, HEIGHT/2) #initialize player

    while True:
        clock.tick(60) #clock runs at 5 FPS

        handleEvents(snake)                      # read inputs
        snake.move()                        # update snake position
        gameDisplay.fill(white)             # clear screen
        render(gameDisplay, snake)          # draw snake
        pygame.display.update()

def handleEvents(snake):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #exit game
            pygame.quit()
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

def render(gameDisplay, snake):
    for segment in snake.segments:
        pygame.draw.circle(gameDisplay, black, (segment.x, segment.y), snake.radius, 0)


if __name__ == "__main__":
    main()
