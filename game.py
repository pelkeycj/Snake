import pygame
import snake

def main():
    #colors
    white = (255, 255, 255)
    black = (0, 0, 0)
    #initializations
    pygame.init()
    WIDTH = 800
    HEIGHT = 600
    gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake')
    gameDisplay.fill(white)
    pygame.display.update()
    snake = Snake() #initialize player

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #exit game
                pygame.quit()
            if event.type == pygame.KEYDOWN: # control direction
                if event.key == pygame.K_LEFT or \
                        event.key == pygame.K_RIGHT or \
                        event.key == pygame.K_UP or \
                        event.key == pygame.K_DOWN:
                    snake.changeDirection(event.key)

        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, black, [WIDTH/2, HEIGHT/2, 10, 50])
        pygame.display.update()

if __name__ == "__main__":
    main()
