import pygame
import random

pygame.init()

SPRITE = pygame.USEREVENT + 1
BG = pygame.USEREVENT + 2

sprite_colors = ['yellow', 'magenta', 'orange', 'white']
bg_colors = ['blue', 'lightblue', 'darkblue']

class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 20))
        self.image.fill('white')
        self.rect = self.image.get_rect(
            x=random.randint(0, 470), y=random.randint(0, 380))
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

    def update(self):
        self.rect.move_ip(self.velocity)

        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] *= -1
            pygame.event.post(pygame.event.Event(SPRITE))
            pygame.event.post(pygame.event.Event(BG))

        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] *= -1
            pygame.event.post(pygame.event.Event(SPRITE))
            pygame.event.post(pygame.event.Event(BG))

    def color(self):
        self.image.fill(random.choice(sprite_colors))

sprite = Sprite()
sprites = pygame.sprite.Group(sprite)
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Boundary Sprite")
bg_color = 'blue'
clock = pygame.time.Clock()
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == SPRITE:
            sprite.color()
        elif event.type == BG:
            bg_color = random.choice(bg_colors)

    sprites.update()
    screen.fill(bg_color)
    sprites.draw(screen)
    pygame.display.flip()
    clock.tick(240)

pygame.quit()