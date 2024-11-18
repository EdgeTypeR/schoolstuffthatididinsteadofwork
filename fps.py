import pygame
import sys
import math

# Alap beállítások
WIDTH, HEIGHT = 800, 600
PLAYER_SPEED = 5
PLAYER_ROT_SPEED = 3  # forgási sebesség fokban

# Pygame inicializálása
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Egyszerű FPS alap")
clock = pygame.time.Clock()

# Játékos kezdő pozíció és irány
player_pos = [WIDTH // 2, HEIGHT // 2]
player_angle = 0  # Kezdeti irány (0 fok)

# Színek
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Segédfüggvény: szöget radiánra váltás
def angle_to_radian(angle):
    return angle * math.pi / 180

# Játék fő ciklusa
running = True
while running:
    screen.fill(BLACK)

    # Események kezelése
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Billentyűzet inputok kezelése
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:  # előre
        player_pos[0] += PLAYER_SPEED * math.cos(angle_to_radian(player_angle))
        player_pos[1] += PLAYER_SPEED * math.sin(angle_to_radian(player_angle))
    if keys[pygame.K_s]:  # hátra
        player_pos[0] -= PLAYER_SPEED * math.cos(angle_to_radian(player_angle))
        player_pos[1] -= PLAYER_SPEED * math.sin(angle_to_radian(player_angle))
    if keys[pygame.K_a]:  # balra
        player_angle -= PLAYER_ROT_SPEED
    if keys[pygame.K_d]:  # jobbra
        player_angle += PLAYER_ROT_SPEED

    # Egyszerű célkereszt kirajzolása
    pygame.draw.line(screen, WHITE, (WIDTH // 2 - 10, HEIGHT // 2), (WIDTH // 2 + 10, HEIGHT // 2), 2)
    pygame.draw.line(screen, WHITE, (WIDTH // 2, HEIGHT // 2 - 10), (WIDTH // 2, HEIGHT // 2 + 10), 2)

    # Játékos kirajzolása (egyszerű háromszög a nézet irányába)
    direction_end_x = player_pos[0] + 20 * math.cos(angle_to_radian(player_angle))
    direction_end_y = player_pos[1] + 20 * math.sin(angle_to_radian(player_angle))
    pygame.draw.circle(screen, WHITE, (int(player_pos[0]), int(player_pos[1])), 5)
    pygame.draw.line(screen, WHITE, player_pos, (direction_end_x, direction_end_y), 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
