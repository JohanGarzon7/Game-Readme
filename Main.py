import pygame
import sys
import random

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Pygame Project")
clock = pygame.time.Clock()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


player_size = 50
player_pos = [WIDTH // 2, HEIGHT - 2 * player_size]
player_speed = 7

enemy_size = 50
enemy_speed = 5
enemies = []

def drop_enemies(enemies):
    if len(enemies) < 10:
        x_pos = random.randint(0, WIDTH - enemy_size)
        enemies.append([x_pos, 0])


def draw_enemies(enemies):
    for enemy in enemies:
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_size, enemy_size))


def update_enemy_positions(enemies):
    for idx, enemy in enumerate(enemies):
        if enemy[1] >= 0 and enemy[1] < HEIGHT:
            enemy[1] += enemy_speed
        else:
            enemies.pop(idx)


def detect_collision(player_pos, enemy_pos):
    px, py = player_pos
    ex, ey = enemy_pos

    if (ex < px < ex + enemy_size or ex < px + player_size < ex + enemy_size) and \
       (ey < py < ey + enemy_size or ey < py + player_size < ey + enemy_size):
        return True
    return False
while True:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += player_speed

    drop_enemies(enemies)
    update_enemy_positions(enemies)
  
    for enemy in enemies:
        if detect_collision(player_pos, enemy):
            print("Game Over!")
            pygame.quit()
            sys.exit()
          
    pygame.draw.rect(screen, BLUE, (player_pos[0], player_pos[1], player_size, player_size))
    draw_enemies(enemies)

    pygame.display.update()
    clock.tick(30)
