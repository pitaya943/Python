# Ref: https://www.a1k0n.net/2011/07/20/donut-math.html
import pygame
import math
import colorsys
import os

pygame.init()

white = (255, 255, 255)
green = (0, 255, 0)
black = (0, 0, 0)
hue = 0

RES = WIDTH, HEIGHT = 800, 800
FPS = 60

os.environ['SDL_VIDEO_CENTERED'] = '1'
screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 20, bold=True)
pygame.display.set_caption('Donut')

# Char's separate size
x_separator = 8
y_separator = 16

rows = HEIGHT // y_separator
columns = WIDTH // x_separator
screen_size = rows * columns

# For rotating animation and coordinate start
inside_x_start, inside_y_start = 0, 0
outside_x_start, out_side_start = 0, 0

A, B = 0, 0
C, D = 0, 0

x_offset = columns / 2
y_offset = rows / 2

theta_spacing = 10
phi_spacing = 3

chars = ".,-~:;=!*#$@"


def hsv2rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))


def text_display(letter, x_start, y_start, shiftColorOrNot=False):
    if shiftColorOrNot:
        textColor = hsv2rgb(hue, 1, 1)
    else:
        textColor = white
    text = font.render(str(letter), True, textColor)
    screen.blit(text, (x_start, y_start))


paused = False
running = True

while running:

    clock.tick(FPS)
    pygame.display.set_caption("FPS: {:.2f}".format(clock.get_fps()))
    screen.fill((black))

    fillWith = [0] * screen_size
    secondFillWith = [0] * screen_size

    blank = [' '] * screen_size
    secondBlank = [' '] * screen_size

    for j in range(0, 628, theta_spacing):  # From 0 to 2pi
        for i in range(0, 628, phi_spacing):  # From 0 to 2pi

            # Inside donut parameter
            sini = math.sin(i)
            sinj = math.sin(j)
            sinA = math.sin(A)
            sinB = math.sin(B)
            cosi = math.cos(i)
            cosj = math.cos(j)
            cosA = math.cos(A)
            cosB = math.cos(B)

            holeSize = cosj + 4
            E = 1 / (sini * holeSize * sinA + sinj * cosA + 15)
            t = sini * holeSize * cosA - sinj * sinA

            x = int(x_offset + 40 * E * (cosi * holeSize * cosB - t * sinB))
            y = int(y_offset + 20 * E * (cosi * holeSize * sinB + t * cosB))
            index = int(x + columns * y)

            lumIndex = int(8 * ((sinj * sinA - sini * cosj * cosA) * cosB - sini * cosj *
                                sinA - sinj * cosA - cosi * cosj * sinB))

            if rows > y and y > 0 and x > 0 and columns > x and E > fillWith[index]:
                fillWith[index] = E
                blank[index] = chars[lumIndex if lumIndex > 0 else 0]

            # Outside donut parameter
            sSini = math.sin(i)
            sSinj = math.sin(j)
            sinC = math.sin(C)
            sinD = math.sin(D)
            sCosi = math.cos(i)
            sCosj = math.cos(j)
            cosC = math.cos(C)
            cosD = math.cos(D)

            sHoleSize = sCosj + 4
            F = 1 / (sSini * sHoleSize * sinC + sSinj * cosC + 6)
            sT = sSini * sHoleSize * cosC - sSinj * sinC

            sX = int(x_offset + 40 * F *
                     (sCosi * sHoleSize * cosD - sT * sinD))
            sY = int(y_offset + 20 * F *
                     (sCosi * sHoleSize * sinD + sT * cosD))
            sIndex = int(sX + columns * sY)

            sLumIndex = int(8 * ((sSinj * sinC - sSini * sCosj * cosC) * cosD - sSini * sCosj *
                                 sinC - sSinj * cosC - sCosi * sCosj * sinD))

            if rows > sY and sY > 0 and sX > 0 and columns > sX and F > secondFillWith[index]:
                secondFillWith[sIndex] = F
                secondBlank[sIndex] = chars[sLumIndex if sLumIndex > 0 else 0]

    if inside_y_start == rows * y_separator - y_separator:
        inside_y_start = 0

    if out_side_start == rows * y_separator - y_separator:
        out_side_start = 0

    # Outside donut
    for i in range(len(secondBlank)):
        C += 0.00002
        D += 0.00001
        if i == 0 or i % columns:
            text_display(secondBlank[i], outside_x_start, out_side_start)
            outside_x_start += x_separator
        else:
            out_side_start += y_separator
            outside_x_start = 0
            text_display(secondBlank[i], outside_x_start, out_side_start)
            outside_x_start += x_separator
    # Inside donut
    for i in range(len(blank)):
        A += 0.00004
        B += 0.00002
        if i == 0 or i % columns:
            text_display(blank[i], inside_x_start, inside_y_start, True)
            inside_x_start += x_separator
        else:
            inside_y_start += y_separator
            inside_x_start = 0
            text_display(blank[i], inside_x_start, inside_y_start, True)
            inside_x_start += x_separator

    hue += 0.01

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
