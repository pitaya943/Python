import os
from math import cos, sin
import pygame
import colorsys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
hue = 0

os.environ['SDL_VIDEO_CENTERED'] = '1'
RES = WIDTH, HEIGHT = 800, 800
FPS = 60

pixel_width = 15
pixel_height = 15

x_pixel = 0
y_pixel = 0

x_pixel2 = 0
y_pixel2 = 0

screen_width = WIDTH // pixel_width
screen_height = HEIGHT // pixel_height
screen_size = screen_width * screen_height

A, B = 0, 0

theta_spacing = 10
phi_spacing = 2

chars = ".,-~:;=!*#$@"

R1 = 10
R2 = 40
K2 = 100
K1 = screen_height * K2 * 3 / (8 * (R1 + R2))

# inside donut
sR1 = 10
sR2 = 40
sK2 = 100
sK1 = screen_height * sK2 * 3 / (16 * (sR1 + sR2))

pygame.init()

screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 20, bold=True)


def hsv2rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))


def text_display(char, x, y):
    text = font.render(str(char), True, hsv2rgb(hue, 1, 1))
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)


white = (255, 255, 255)


def text_display2(char, x, y):
    text = font.render(str(char), True, white)
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)


k = 0
k2 = 0

paused = False
running = True
while running:
    clock.tick(FPS)
    pygame.display.set_caption("FPS: {:.2f}".format(clock.get_fps()))
    screen.fill(BLACK)

    output = [' '] * screen_size
    zbuffer = [0] * screen_size

    output2 = [' '] * screen_size
    zbuffer2 = [0] * screen_size

    # theta goes around the cross-sectional circle of a torus, from 0 to 2pi
    for theta in range(0, 628, theta_spacing):
        # phi goes around the center of revolution of a torus, from 0 to 2pi
        for phi in range(0, 628, phi_spacing):

            cosA = cos(A)
            sinA = sin(A)
            cosB = cos(B)
            sinB = sin(B)

            costheta = cos(theta)
            sintheta = sin(theta)
            cosphi = cos(phi)
            sinphi = sin(phi)

            # x, y coordinates before revolving
            circlex = R2 + R1 * costheta
            circley = R1 * sintheta

            circlex2 = sR2 + sR1 * costheta
            circley2 = sR1 * sintheta

            # 3D (x, y, z) coordinates after rotation
            x = circlex * (cosB * cosphi + sinA * sinB *
                           sinphi) - circley * cosA * sinB
            y = circlex * (sinB * cosphi - sinA * cosB *
                           sinphi) + circley * cosA * cosB
            z = K2 + cosA * circlex * sinphi + circley * sinA
            ooz = 1 / z  # one over z

            x2 = circlex2 * (cosB * cosphi - sinA * sinB *
                             sinphi) - circley2 * cosA * sinB
            y2 = circlex2 * (sinB * cosphi + sinA * cosB *
                             sinphi) + circley2 * cosA * cosB
            z2 = sK2 + cosA * circlex2 * sinphi + circley2 * sinA
            ooz2 = 1 / z2

            # x, y projection
            xp = int(screen_width / 2 + K1 * ooz * x)
            yp = int(screen_height / 2 - K1 * ooz * y)

            xp2 = int(screen_width / 2 + sK1 * ooz2 * x2)
            yp2 = int(screen_height / 2 - sK1 * ooz2 * y2)

            position = xp + screen_width * yp
            position2 = xp2 + screen_width * yp2

            # luminance (L ranges from -sqrt(2) to sqrt(2))
            L = cosphi * costheta * sinB - cosA * costheta * sinphi - sinA * sintheta + cosB * (
                cosA * sintheta - costheta * sinA * sinphi)

            L2 = cosphi * costheta * sinB - cosA * costheta * sinphi - sinA * sintheta + cosB * (
                cosA * sintheta - costheta * sinA * sinphi)

            if ooz > zbuffer[position]:
                # larger ooz means the pixel is closer to the viewer than what's already plotted
                zbuffer[position] = ooz
                # we multiply by 8 to get luminance_index range 0..11 (8 * sqrt(2) = 11)
                luminance_index = int(L * 8)
                output[position] = chars[luminance_index if luminance_index > 0 else 0]

            if ooz2 > zbuffer2[position2]:
                # larger ooz means the pixel is closer to the viewer than what's already plotted
                zbuffer2[position2] = ooz2
                # we multiply by 8 to get luminance_index range 0..11 (8 * sqrt(2) = 11)
                luminance_index = int(L2 * 8)
                output2[position2] = chars[luminance_index if luminance_index > 0 else 0]

    for i in range(screen_height):
        y_pixel += pixel_height
        for j in range(screen_width):
            x_pixel += pixel_width
            text_display(output[k], x_pixel, y_pixel)
            k += 1
        x_pixel = 0
    y_pixel = 0
    k = 0

    # for i in range(screen_height):
    #     y_pixel2 += pixel_height
    #     for j in range(screen_width):
    #         x_pixel2 += pixel_width
    #         text_display2(output2[k2], x_pixel2, y_pixel2)
    #         k2 += 1
    #     x_pixel2 = 0
    # y_pixel2 = 0
    # k2 = 0

    A += 0.15
    B += 0.035

    hue += 0.005

    if not paused:
        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                paused = not paused
