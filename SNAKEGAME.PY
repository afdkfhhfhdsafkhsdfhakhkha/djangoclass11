import pygame
import random

# Initialize pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the width and height of each snake segment
segment_width = 15
segment_height = 15
segment_margin = 3

# Set the dimensions of the game window
display_width = 800
display_height = 600

# Set the speed of the snake
snake_speed = 15

# Create the game window
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

# Function to display the snake on the game window
def draw_snake(snake_segments):
    for segment in snake_segments:
        pygame.draw.rect(game_display, GREEN, (segment[0], segment[1], segment_width, segment_height))

# Function to generate a random position for the food
def generate_food():
    food_x = round(random.randrange(0, display_width - segment_width) / 15.0) * 15.0
    food_y = round(random.randrange(0, display_height - segment_height) / 15.0) * 15.0
    return food_x, food_y

# Main game loop
def game_loop():
    game_over = False
    game_quit = False

    # Initial position of the snake
    lead_x = display_width / 2
    lead_y = display_height / 2

    # Initial velocity of the snake
    lead_x_change = 0
    lead_y_change = 0

    # Initialize the snake segments
    snake_segments = []
    snake_length = 1

    # Generate the first food
    food_x, food_y = generate_food()

    # Game loop
    while not game_quit:
        while game_over:
            # Game over screen
            game_display.fill(BLACK)
            font = pygame.font.Font(None, 50)
            text = font.render("Game Over, Press Q to Quit or C to Continue", True, RED)
            game_display.blit(text, (display_width / 2 - text.get_width() / 2, display_height / 2 - text.get_height() / 2))
            pygame.display.update()

            # Event handling for the game over screen
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_quit = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_quit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -segment_width - segment_margin
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = segment_width + segment_margin
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -segment_height - segment_margin
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = segment_height + segment_margin
                    lead_x_change = 0

       

