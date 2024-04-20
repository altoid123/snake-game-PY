import pygame
import random

pygame.init()
square_width = 750
pixel_width = 50
screen = pygame.display.set_mode([square_width] * 2)
clock = pygame.time.Clock()
running = True


def generate_starting_position():
    position_range = (pixel_width // 2, square_width - pixel_width // 2, pixel_width)
    return [random.randrange(*position_range), random.randrange(*position_range)]


def reset():
    target.center = generate_starting_position()
    snake_pixel.center = generate_starting_position()
    return snake_pixel.copy()


def reflect_off_bounds(snake_segment):
    if snake_segment.bottom >= square_width or snake_segment.top <= 0:
        snake_direction[1] *= -1
    if snake_segment.left <= 0 or snake_segment.right >= square_width:
        snake_direction[0] *= -1


snake_pixel = pygame.rect.Rect([0, 0, pixel_width - 2, pixel_width - 2])
snake_pixel.center = generate_starting_position()
snake = [snake_pixel.copy()]
snake_direction = [0, 0]
snake_length = 1

target = pygame.rect.Rect([0, 0, pixel_width - 2, pixel_width - 2])
target.center = generate_starting_position()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    for segment in snake:
        reflect_off_bounds(segment)

    if snake_pixel.center == target.center:
        target.center = generate_starting_position()
        snake_length += 1
        snake.append(snake_pixel.copy())

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        snake_direction = [0, -pixel_width]
    if keys[pygame.K_s]:
        snake_direction = [0, pixel_width]
    if keys[pygame.K_a]:
        snake_direction = [-pixel_width, 0]
    if keys[pygame.K_d]:
        snake_direction = [pixel_width, 0]

    for snake_part in snake:
        pygame.draw.rect(screen, "green", snake_part)

    pygame.draw.rect(screen, "red", target)

    snake_pixel.move_ip(snake_direction)
    snake = [snake_pixel.copy()] + snake[:-1]

    pygame.display.flip()

    clock.tick(10)

pygame.quit()
