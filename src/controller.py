import pygame
from bird import Bird
from pipe import Pipe

class Controller:
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Flappy Bird")
        self.clock = pygame.time.Clock()
        self.bird = Bird(50, 200, "bird.png")
        self.pipes = []

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bird.jump()

    def update_models(self):
        self.bird.update()
        for pipe in self.pipes:
            pipe.move()
            if self.bird.collides_with(pipe):
                pass

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.bird.draw(self.screen)
        for pipe in self.pipes:
            pipe.draw(self.screen)
        pygame.display.flip()

    def main_loop(self):
        while True:
            self.handle_events()
            self.update_models()
            self.draw()
            self.clock.tick(60)

if __name__ == "__main__":
    controller = Controller()
    controller.main_loop()