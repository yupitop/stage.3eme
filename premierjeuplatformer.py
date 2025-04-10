import sys
import time
import pygame

pygame.init()


player_img = pygame.image.load("images/mario.png")
player_img = pygame.transform.scale(player_img, (40, 40))


tile_size = 40
cols, rows = 24, 13
width, height = cols * tile_size, rows * tile_size
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mario-Inspired Platformer")
clock = pygame.time.Clock()

# Couleurs
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (139, 69, 19)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)

# Joueur
player = pygame.Rect(1 * tile_size, height - 3 * tile_size, tile_size, tile_size)
velocity_y = 0
grounded = False

# Éléments
platforms = [
    pygame.Rect(0, height - 2 * tile_size, 2 * tile_size, 2 * tile_size),
    pygame.Rect(4 * tile_size, height - 2.25 * tile_size, tile_size, int(0.25 * tile_size)),
    pygame.Rect(9 * tile_size, height - 7 * tile_size, 7 * tile_size, 2 * tile_size),
    pygame.Rect(4 * tile_size, height - 11 * tile_size, 2 * tile_size, 2 * tile_size),
    pygame.Rect(12 * tile_size, height - tile_size, 13 * tile_size, tile_size),
]

blocks = [
    pygame.Rect(14 * tile_size, height - 10 * tile_size, tile_size, tile_size),
    pygame.Rect(15 * tile_size, height - 7 * tile_size, tile_size, tile_size),
    pygame.Rect(15 * tile_size, height - 8 * tile_size, tile_size, tile_size),
    pygame.Rect(1 * tile_size, height - 8 * tile_size, tile_size, tile_size),
]

pipes = [
    pygame.Rect(1 * tile_size, height - 9 * tile_size, tile_size, tile_size),
    pygame.Rect(12 * tile_size, height - 2 * tile_size, tile_size, 2 * tile_size),
]

spike = pygame.Rect(2 * tile_size, height - 2.5 * tile_size, tile_size, int(0.5 * tile_size))
water = pygame.Rect(3 * tile_size, height - 0.5 * tile_size, 7 * tile_size, int(0.5 * tile_size))
trampoline = pygame.Rect(7 * tile_size, height - tile_size, tile_size, tile_size)
vine_anchor = pygame.Rect(6 * tile_size, height - 5 * tile_size, tile_size, tile_size)
zipline_start = pygame.Rect(14 * tile_size, height - 10 * tile_size, tile_size, tile_size)
zipline_end = pygame.Rect(5 * tile_size, height - 10 * tile_size, tile_size, tile_size)

portal = pygame.Rect(24 * tile_size, height - 3 * tile_size, tile_size, 2 * tile_size)

enemy = pygame.Rect(10 * tile_size, height - 7 * tile_size, tile_size, tile_size)
enemy_dir = 1

# Canon et boulets
cannon = pygame.Rect(22 * tile_size, height - 3 * tile_size, tile_size, 2 * tile_size)
bullets = []
last_shot_time = time.time()

font = pygame.font.SysFont(None, 60)

def draw():
    screen.fill(WHITE)
    screen.blit(player_img, player)
    for plat in platforms:
        pygame.draw.rect(screen, BROWN, plat)
    for b in blocks:
        pygame.draw.rect(screen, GRAY, b)
    for p in pipes:
        pygame.draw.rect(screen, GREEN, p)
    pygame.draw.rect(screen, RED, spike)
    pygame.draw.rect(screen, BLUE, water)
    pygame.draw.rect(screen, PURPLE, trampoline)
    pygame.draw.line(screen, (0, 100, 0), vine_anchor.center, (vine_anchor.centerx, vine_anchor.centery + int(1.5 * tile_size)), 5)
    pygame.draw.line(screen, (150, 75, 0), zipline_start.center, zipline_end.center, 3)
    pygame.draw.rect(screen, BLACK, enemy)
    pygame.draw.rect(screen, BLACK, cannon)
    for b in bullets:
        pygame.draw.circle(screen, BLACK, b.center, 10)
    pygame.draw.rect(screen, (255, 215, 0), portal)
    pygame.display.flip()

def reset():
    player.x = 1 * tile_size
    player.y = height - 3 * tile_size
    bullets.clear()

def victory():
    text = font.render("Victory!", True, (0, 128, 0))
    screen.blit(text, (width // 2 - 100, height // 2))
    pygame.display.flip()
    pygame.time.delay(3000)
    pygame.quit()
    sys.exit()

def game_over():
    text = font.render("Game Over", True, (255, 0, 0))
    screen.blit(text, (width // 2 - 130, height // 2))
    pygame.display.flip()
    pygame.time.delay(3000)
    reset()

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    dx = 0
    if keys[pygame.K_LEFT]:
        dx = -5
    if keys[pygame.K_RIGHT]:
        dx = 5
    if keys[pygame.K_SPACE] and grounded:
        velocity_y = -12

    velocity_y += 0.5
    dy = velocity_y

    player.x += dx

    grounded = False
    player.y += dy
    for plat in platforms + blocks:
        if player.colliderect(plat):
            if velocity_y > 0:
                player.bottom = plat.top
                grounded = True
                velocity_y = 0

    if player.colliderect(spike) or player.colliderect(water) or player.colliderect(enemy) or any(player.colliderect(b) for b in bullets):
        game_over()

    if player.colliderect(trampoline):
        velocity_y = -14

    if vine_anchor.collidepoint(player.center):
        player.x = trampoline.x
        player.y = trampoline.y - tile_size
        velocity_y = -5

    if zipline_start.collidepoint(player.center):
        player.x = zipline_end.x
        player.y = zipline_end.y
        velocity_y = 0

    if pipes[0].colliderect(player):
        player.x = 12 * tile_size
        player.y = height - 4 * tile_size

    if player.colliderect(portal):
        victory()

    enemy.x += enemy_dir
    if enemy.x > 13 * tile_size or enemy.x < 10 * tile_size:
        enemy_dir *= -1

    if time.time() - last_shot_time > 3:
        bullets.append(pygame.Rect(cannon.x, cannon.y, 20, 20))
        last_shot_time = time.time()

    for b in bullets:
        b.x -= 5
    bullets = [b for b in bullets if b.x > 12 * tile_size]

    draw()
print()
pygame.quit()
sys.exit()