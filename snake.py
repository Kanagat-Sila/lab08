
import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
CELL_SIZE = 20
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Font for score display
font = pygame.font.Font(None, 30)

# Snake initial settings
snake = [(100, 100), (90, 100), (80, 100)]
direction = "RIGHT"
speed = 5
score = 0
level = 1

# Generate food at a random position avoiding the snake
def generate_food():
    while True:
        food_x = random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE
        food_y = random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
        if (food_x, food_y) not in snake:
            return (food_x, food_y)

food = generate_food()

clock = pygame.time.Clock()

running = True
while running:
    SCREEN.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"
    
    # Move the snake
    head_x, head_y = snake[0]
    if direction == "UP":
        head_y -= CELL_SIZE
    elif direction == "DOWN":
        head_y += CELL_SIZE
    elif direction == "LEFT":
        head_x -= CELL_SIZE
    elif direction == "RIGHT":
        head_x += CELL_SIZE
    
    new_head = (head_x, head_y)
    
    # Check for border collision
    if head_x < 0 or head_x >= SCREEN_WIDTH or head_y < 0 or head_y >= SCREEN_HEIGHT:
        print("Game Over! Collision with wall.")
        running = False
    
    # Check for self collision
    if new_head in snake:
        print("Game Over! Collision with self.")
        running = False
    
    # Add new head to the snake
    snake.insert(0, new_head)
    
    # Check if food is eaten
    if new_head == food:
        score += 1
        food = generate_food()
        # Increase level every 3 points
        if score % 3 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()
    
    # Draw snake
    for segment in snake:
        pygame.draw.rect(SCREEN, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
    
    # Draw food
    pygame.draw.rect(SCREEN, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))
    
    # Draw score and level
    score_text = font.render(f"Score: {score}  Level: {level}", True, BLACK)
    SCREEN.blit(score_text, (10, 10))
    
    pygame.display.update()
    clock.tick(speed)

pygame.quit()
sys.exit()
