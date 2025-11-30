import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установка размеров окна
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))

# Установка заголовка окна
pygame.display.set_caption("Пong")

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Определение размеров ракеток и мяча
paddle_width = 10
paddle_height = 100
ball_size = 10

# Начальные позиции ракеток и мяча
paddle1_y = screen_height / 2 - paddle_height / 2
paddle2_y = screen_height / 2 - paddle_height / 2
ball_x = screen_width / 2
ball_y = screen_height / 2
ball_speed_x = 5
ball_speed_y = 5

# Скорость ракеток
paddle_speed = 5

# Счет
score1 = 0
score2 = 0

# Основной цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Перемещение ракеток
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1_y -= paddle_speed
    if keys[pygame.K_s]:
        paddle1_y += paddle_speed
    if keys[pygame.K_UP]:
        paddle2_y -= paddle_speed
    if keys[pygame.K_DOWN]:
        paddle2_y += paddle_speed

    # Перемещение мяча
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Столкновение с ракетками
    if ball_x <= paddle_width and ball_y >= paddle1_y and ball_y <= paddle1_y + paddle_height:
        ball_speed_x *= -1
    elif ball_x >= screen_width - paddle_width - ball_size and ball_y >= paddle2_y and ball_y <= paddle2_y + paddle_height:
        ball_speed_x *= -1

    # Столкновение с краями экрана
    if ball_y <= 0 or ball_y >= screen_height - ball_size:
        ball_speed_y *= -1

    # Гол!
    if ball_x <= 0:
        score2 += 1
        ball_x = screen_width / 2
        ball_y = screen_height / 2
    elif ball_x >= screen_width - ball_size:
        score1 += 1
        ball_x = screen_width / 2
        ball_y = screen_height / 2

    # Отрисовка всего
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (0, paddle1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, (screen_width - paddle_width, paddle2_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, (ball_x, ball_y, ball_size, ball_size))
    pygame.draw.aaline(screen, WHITE, (screen_width / 2, 0), (screen_width / 2, screen_height))
    font = pygame.font.Font(None, 72)
    text = font.render(str(score1) + " - " + str(score2), 1, WHITE)
    screen.blit(text, (screen_width / 2 - text.get_width() / 2, 10))

    # Обновление дисплея
    pygame.display.flip()
    pygame.time.Clock().tick(60)
