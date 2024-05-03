import pygame
import random
from src.game.game import SnakeGame, SCREEN_WIDTH, SCREEN_HEIGHT, FPS

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
CELL_SIZE = 20
FPS = 10

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

class SnakeGameController:
    def __init__(self):
        self.game = SnakeGame()
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and not self.game.running:
                    self.game.restart_game()

    def run(self):
        while self.running:
            self.handle_events()
            if self.game.running:
                self.game.handle_events()
                self.game.update_snake_position()
                self.game.check_collisions()
                self.game.draw()
                clock.tick(FPS)
            else:
                self.show_game_over_screen()

        pygame.quit()

    def show_game_over_screen(self):
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 72)
        game_over_text = font.render('Game Over', True, (255, 0, 0))
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50))

        font = pygame.font.Font(None, 36)
        restart_text = font.render('Press R to restart', True, (255, 255, 255))
        screen.blit(restart_text, (SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2 + 30))

        pygame.display.flip()

if __name__ == '__main__':
    controller = SnakeGameController()
    controller.run()