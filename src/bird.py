import pygame

class Bird:
    def __init__(self, x, y, img_file):
        self.x = x
        self.y = y
        self.vel = 0
        self.gravity = 0.25
        self.jump_strength = -4
        self.image = pygame.image.load(img_file)

    def jump(self):
        self.vel = self.jump_strength

    def update(self):
        self.vel += self.gravity
        self.y += self.vel

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
