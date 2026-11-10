import pygame
import random
import sys
import urllib.request
import io
from urllib.request import urlopen

# Initialize Pygame
pygame.init()

# Game Constants
SCREEN_WIDTH = 288
SCREEN_HEIGHT = 512
GRAVITY = 0.25
BIRD_JUMP = -5
PIPE_GAP = 100
PIPE_FREQUENCY = 1500  # milliseconds
GROUND_HEIGHT = 100

# Colors
WHITE = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()

# Load images from URLs
def load_image_from_url(url):
    image_str = urlopen(url).read()
    image_file = io.BytesIO(image_str)
    return pygame.image.load(image_file)

# Load images
background_img = load_image_from_url('https://raw.githubusercontent.com/sourabhv/FlapPyBird/master/assets/sprites/background-day.png')
bird_img = load_image_from_url('https://raw.githubusercontent.com/sourabhv/FlapPyBird/master/assets/sprites/yellowbird-midflap.png')
pipe_img = load_image_from_url('https://raw.githubusercontent.com/sourabhv/FlapPyBird/master/assets/sprites/pipe-green.png')
ground_img = load_image_from_url('https://raw.githubusercontent.com/sourabhv/FlapPyBird/master/assets/sprites/base.png')

# Scale images if needed
background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
pipe_img_flipped = pygame.transform.flip(pipe_img, False, True)

class Bird:
    def __init__(self):
        self.x = 50
        self.y = SCREEN_HEIGHT // 2
        self.velocity = 0
        self.rect = bird_img.get_rect(center=(self.x, self.y))

    def jump(self):
        self.velocity = BIRD_JUMP

    def move(self):
        self.velocity += GRAVITY
        self.y += self.velocity
        self.rect.centery = self.y

    def draw(self):
        screen.blit(bird_img, self.rect)

class Pipe:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.height = random.randint(150, 350)
        self.top_rect = pipe_img_flipped.get_rect(bottomleft=(self.x, self.height - PIPE_GAP // 2))
        self.bottom_rect = pipe_img.get_rect(topleft=(self.x, self.height + PIPE_GAP // 2))

    def move(self):
        self.x -= 3
        self.top_rect.x = self.x
        self.bottom_rect.x = self.x

    def draw(self):
        screen.blit(pipe_img_flipped, self.top_rect)
        screen.blit(pipe_img, self.bottom_rect)

def main():
    bird = Bird()
    pipes = []
    score = 0
    last_pipe = pygame.time.get_ticks()
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_over:
                    bird.jump()
                if event.key == pygame.K_SPACE and game_over:
                    # Reset game
                    bird = Bird()
                    pipes = []
                    score = 0
                    game_over = False

        if not game_over:
            # Draw background
            screen.blit(background_img, (0, 0))

            # Create new pipes
            time_now = pygame.time.get_ticks()
            if time_now - last_pipe > PIPE_FREQUENCY:
                pipes.append(Pipe())
                last_pipe = time_now

            # Update and draw pipes
            for pipe in pipes[:]:
                pipe.move()
                pipe.draw()
                
                # Check collision
                if bird.rect.colliderect(pipe.top_rect) or bird.rect.colliderect(pipe.bottom_rect):
                    game_over = True
                
                # Remove off-screen pipes
                if pipe.x < -pipe_img.get_width():
                    pipes.remove(pipe)
                    score += 1

            # Update and draw bird
            bird.move()
            bird.draw()

            # Draw ground
            screen.blit(ground_img, (0, SCREEN_HEIGHT - ground_img.get_height()))

            # Check ground collision
            if bird.y > SCREEN_HEIGHT - ground_img.get_height() or bird.y < 0:
                game_over = True

            # Draw score
            font = pygame.font.Font(None, 36)
            score_text = font.render(f'Score: {score}', True, WHITE)
            screen.blit(score_text, (10, 10))

        else:
            # Game over screen
            font = pygame.font.Font(None, 48)
            game_over_text = font.render('Game Over!', True, WHITE)
            restart_text = font.render('Press SPACE to restart', True, WHITE)
            screen.blit(game_over_text, (SCREEN_WIDTH//2 - game_over_text.get_width()//2, SCREEN_HEIGHT//2 - 50))
            screen.blit(restart_text, (SCREEN_WIDTH//2 - restart_text.get_width()//2, SCREEN_HEIGHT//2 + 50))

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()