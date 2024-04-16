import pygame
import random

class Pipe:
    def __init__(self, x, y, img_file):
        self.x = x
        self.y = y
        self.img_file = img_file
        self.image = pygame.image.load(img_file)

    def move(self, speed):
        self.x -= speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
