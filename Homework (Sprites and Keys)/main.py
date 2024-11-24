
import pygame

pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Sprites And Keys HW - CAT")

WIDTH = 800
HEIGHT = 800

class Cat(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("cat.png")
        self.rect = self.image.get_rect()
    def update(self, keysPressed):
        if keysPressed[pygame.K_UP]:
            self.rect.move_ip((0,-2))
        if keysPressed[pygame.K_DOWN]:
            self.rect.move_ip((0,2))
        if keysPressed[pygame.K_LEFT]:
            self.rect.move_ip((-2,0))
        if keysPressed[pygame.K_RIGHT]:
            self.rect.move_ip((2,0))
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

catGroup = pygame.sprite.Group

def controlCatGame():
    cat = Cat()
    catGroup.add(cat)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        keysPressed = pygame.key.get_pressed()
        screen.blit(pygame.image.load("bg.jpg"), (0,0))
        screen.fill("lavender")
        catGroup.draw(screen)
        cat.update(keysPressed)
        pygame.display.update()

controlCatGame()