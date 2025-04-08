import pygame
import random
import sys

pygame.init()

# Dimensions
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

# Couleurs
WHITE = (255, 255, 255)
FONT = pygame.font.SysFont("Arial", 40)

# Images
bg_img = pygame.image.load("images/background.png")
bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))

bird_img = pygame.image.load("images/bird.png")
bird_img = pygame.transform.scale(bird_img, (40, 40))

pipe_img = pygame.image.load("images/pipe.png")
pipe_img = pygame.transform.scale(pipe_img, (60, 400))

# Joueur
bird = pygame.Rect(100, 250, 40, 40)
gravity = 0
jump_strength = -10

# Tuyaux
pipes = []
PIPE_WIDTH = 60
PIPE_GAP = 150
pipe_timer = 0

# Score
score = 0
game_over = False

def reset():
    global bird, gravity, pipes, score, game_over
    bird.y = 250
    gravity = 0
    pipes = []
    score = 0
    game_over = False

def draw():
    screen.blit(bg_img, (0, 0))
    screen.blit(bird_img, bird)

    for p in pipes:
        if p["flipped"]:
            screen.blit(p["surface"], (p["rect"].x, p["rect"].y))
        else:
            screen.blit(p["surface"], (p["rect"].x, p["rect"].y))

    score_text = FONT.render(str(score), True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 50))

    if game_over:
        over_text = FONT.render("Game Over", True, (255, 0, 0))
        screen.blit(over_text, (WIDTH // 2 - over_text.get_width() // 2, HEIGHT // 2))

    pygame.display.flip()

def create_pipe():
    height = random.randint(100, 400)
    top_pipe = pygame.transform.flip(pipe_img, False, True)
    bottom_pipe = pipe_img

    pipes.append({
        "rect": pygame.Rect(WIDTH, height - 400, PIPE_WIDTH, 400),
        "surface": top_pipe,
        "flipped": True,
        "passed": False
    })
    pipes.append({
        "rect": pygame.Rect(WIDTH, height + PIPE_GAP, PIPE_WIDTH, 400),
        "surface": bottom_pipe,
        "flipped": False,
        "passed": False
    })

# Boucle principale
reset()
while True:
    clock.tick(60)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if not game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            gravity = jump_strength

        if game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            reset()

    if not game_over:
        gravity += 0.5
        bird.y += gravity

        pipe_timer += 1
        if pipe_timer > 90:
            create_pipe()
            pipe_timer = 0

        for p in pipes:
            p["rect"].x -= 4

        # Collision
        for p in pipes:
            if bird.colliderect(p["rect"]):
                game_over = True

        if bird.top < 0 or bird.bottom > HEIGHT:
            game_over = True

        # Score
        for p in pipes:
            if not p["passed"] and p["rect"].x + PIPE_WIDTH < bird.x:
                p["passed"] = True
                score += 0.5  # 0.5 car chaque tuyau = 2 objets

    draw()