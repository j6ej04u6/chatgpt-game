import pygame
import sys
import random

pygame.init()

window_size = (800, 600)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Avoid the Balls")

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, , 255)

player_size = 50
player_pos = [window_size[0] // 2, window_size[1] - 2 * player_size]

ball_radius = 20
ball_pos = [random.randint(ball_radius, window_size[0] - ball_radius), 0]
ball_list = [ball_pos]

ball_speed = 5

score = 0

clock = pygame.time.Clock()

def drop_balls(ball_list):
    delay = random.random()
    if len(ball_list) < 10 and delay < 0.1:
        x_pos = random.randint(ball_radius, window_size[0] - ball_radius)
        y_pos = 0
        ball_list.append([x_pos, y_pos])

def draw_balls(ball_list):
    for ball_pos in ball_list:
        pygame.draw.circle(window, blue, ball_pos, ball_radius)

def update_balls(ball_list, score):
    for index, ball_pos in enumerate(ball_list):
        if ball_pos[1] >= 0 and ball_pos[1] < window_size[1]:
            ball_pos[1] += ball_speed
        else:
            ball_list.pop(index)
            score += 1
    return score

def collision_check(player_pos, ball_list):
    for ball_pos in ball_list:
        if detect_collision(player_pos, ball_pos):
            return True
    return False

def detect_collision(player_pos, ball_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]

    b_x = ball_pos[0]
    b_y = ball_pos[1]

    if (b_x >= p_x and b_x < (p_x + player_size)) or (p_x >= b_x and p_x < (b_x + ball_radius)):
        if (b_y >= p_y and b_y < (p_y + player_size)) or (p_y >= b_y and p_y < (b_y + ball_radius)):
            return True
    return False

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            y = player_pos[1]

            if event.key == pygame.K_LEFT:
                x -= player_size
            elif event.key == pygame.K_RIGHT:
                x += player_size

            player_pos = [x, y]

    window.fill(white)

    drop_balls(ball_list)
    score = update_balls(ball_list, score)
    text = "Score: " + str(score)
    pygame.display.set_caption(text)

    if collision_check(player_pos, ball_list):
        game_over = True
        break

    draw_balls(ball_list)

    pygame.draw.rect(window, black, (player_pos[0], player_pos[1], player_size, player_size))

    clock.tick(30)
    pygame.display.update()

pygame.quit()
sys.exit()
