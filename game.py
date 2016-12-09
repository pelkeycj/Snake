import pygame

def main():
    #colors
    white(255, 255, 255)
    #initializations
    pygame.init()
    gameDisplay = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Snake')
    gameDisplay.fill(white)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        gameDisplay.update()

if __name__ == "__main__":
    main()
