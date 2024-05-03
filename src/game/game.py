import pygame
import random
pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
CELL_SIZE = 20
FPS = 10

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

class SnakeGame:
    def __init__(self):
        self.snake = [(200, 200)]
        self.snake_direction = 'RIGHT'
        self.food = self.random_food_position()
        self.extra_food = None
        self.yellow_block = None
        self.score = 0
        self.high_score = self.load_high_score()
        self.running = True

    def random_food_position(self):
        return (random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.snake_direction != 'RIGHT':
            self.snake_direction = 'LEFT'
        elif keys[pygame.K_RIGHT] and self.snake_direction != 'LEFT':
            self.snake_direction = 'RIGHT'
        elif keys[pygame.K_UP] and self.snake_direction != 'DOWN':
            self.snake_direction = 'UP'
        elif keys[pygame.K_DOWN] and self.snake_direction != 'UP':
            self.snake_direction = 'DOWN'

    def update_snake_position(self):
        x, y = self.snake[0]
        if self.snake_direction == 'LEFT':
            x -= CELL_SIZE
        elif self.snake_direction == 'RIGHT':
            x += CELL_SIZE
        elif self.snake_direction == 'UP':
            y -= CELL_SIZE
        elif self.snake_direction == 'DOWN':
            y += CELL_SIZE

        if x < 0 or x >= SCREEN_WIDTH or y < 0 or y >= SCREEN_HEIGHT or (x, y) in self.snake:
            self.game_over()

        self.snake.insert(0, (x, y))

        if (x, y) == self.food:
            self.score += 1
            self.food = self.random_food_position()

            if random.random() < 0.2:
                self.extra_food = self.random_food_position()

            if random.random() < min(0.1 + self.score * 0.005, 0.5):
                self.spawn_yellow_block()

            self.check_high_score()

        else:
            self.snake.pop()

    def spawn_yellow_block(self):
        x = random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 2) * CELL_SIZE
        y = random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 2) * CELL_SIZE
        self.yellow_block = (x, y)

    def check_collisions(self):
        head_x, head_y = self.snake[0]

        if self.extra_food and (head_x, head_y) == self.extra_food:
            self.score += 2
            self.extra_food = None

        if self.yellow_block:
            block_x, block_y = self.yellow_block
            if head_x >= block_x and head_x < block_x + CELL_SIZE * 2:
                if head_y >= block_y and head_y < block_y + CELL_SIZE * 2:
                    self.game_over()

    def check_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score

    def save_high_score(self):
        with open('high_score.txt', 'w') as file:
            file.write(str(self.high_score))

    def load_high_score(self):
        try:
            with open('high_score.txt', 'r') as file:
                return int(file.read())
        except FileNotFoundError:
            return 0

    def game_over(self):
        self.save_high_score()
        self.running = False

    def restart_game(self):
        self.snake = [(200, 200)]
        self.snake_direction = 'RIGHT'
        self.food = self.random_food_position()
        self.extra_food = None
        self.yellow_block = None
        self.score = 0
        self.running = True

    def draw(self):
        screen = pygame.display.get_surface()
        screen.fill((0, 0, 0))
        self.draw_grid()
        pygame.draw.rect(screen, WHITE, (self.food[0], self.food[1], CELL_SIZE, CELL_SIZE))

        if self.extra_food:
            pygame.draw.rect(screen, BLUE, (self.extra_food[0], self.extra_food[1], CELL_SIZE, CELL_SIZE))

        if self.yellow_block:
            pygame.draw.rect(screen, YELLOW, (self.yellow_block[0], self.yellow_block[1], CELL_SIZE * 2, CELL_SIZE * 2))

        for segment in self.snake:
            pygame.draw.rect(screen, (0, 255, 0), (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

        self.draw_score()
        self.draw_high_score()
        pygame.display.flip()

    def draw_grid(self):
        screen = pygame.display.get_surface()
        for x in range(0, SCREEN_WIDTH, CELL_SIZE):
            pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
            pygame.draw.line(screen, (40, 40, 40), (0, y), (SCREEN_WIDTH, y))

    def draw_score(self):
        screen = pygame.display.get_surface()
        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {self.score}', True, WHITE)
        screen.blit(score_text, (10, 10))

    def draw_high_score(self):
        screen = pygame.display.get_surface()
        font = pygame.font.Font(None, 36)
        high_score_text = font.render(f'High Score: {self.high_score}', True, WHITE)
        screen.blit(high_score_text, (SCREEN_WIDTH - 200, 10))