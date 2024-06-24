import pygame
import math

pygame.init()
pygame.display.set_caption("TIC TAC TOE")

WIDTH = 320
HEIGHT = 350

win = pygame.display.set_mode((WIDTH, HEIGHT))

text_font = pygame.font.SysFont("arial", 80)
text_font2 = pygame.font.SysFont("arial", 30)

cross = []
circle = []

r = True
key = True
toggle = False

winner = []


def draw_text(text, font, col, x, y):
    global win
    img = font.render(text, True, col)
    win.blit(img, (x, y))


def draw_board():
    global win, key
    win.fill((0, 0, 50))
    draw_circles()
    draw_crosses()

    for i in range(0, 3):
        for j in range(0, 3):
            pygame.draw.rect(win, (255, 255, 255), (10 + 100 * i, 10 + 100 * j, 100, 100), 5)

    if not len(winner) == 0:
        text = winner.copy()
        draw_text(text.pop(), text_font2, (200, 0, 0), 10, 320)
        key = False


def draw_circles():
    for k in circle:
        x = k[0] * 100 + 30
        y = k[1] * 100 + 20
        draw_text("0", text_font, (255, 0, 255), x, y)


def draw_crosses():
    for k in cross:
        x = k[0] * 100 + 30
        y = k[1] * 100 + 20
        draw_text("X", text_font, (0, 255, 0), x, y)


def fill_box(pos, sign):
    valid = True
    new = []
    for k in range(0, 2):
        if 10 < pos[k] < 310:
            new.append(math.floor((pos[k] - 10) / 100))
        else:
            valid = False
    arr = []
    arr.extend(cross)
    arr.extend(circle)
    for n in arr:
        if n == new:
            valid = False

    if valid:
        if sign:
            circle.append(new)
            won = wining(circle, new)
            if won:
                winner.append('0 won')

        else:
            cross.append(new)
            won = wining(cross, new)
            if won:
                winner.append('X won')

        size = len(circle) + len(cross)

        if not won and size == 9:
            winner.append('DRAWN')


def wining(curr, pos):
    x = pos[0]
    y = pos[1]

    point = [0, 0, 0, 0]

    for k in range(0, 3):
        if [k, y] in curr:
            point[0] += 1
        if [x, k] in curr:
            point[1] += 1
        if [k, k] in curr:
            point[2] += 1
        if [k, 2 - k] in curr:
            point[3] += 1

    if 3 in point:
        return True


def reset():
    global circle, cross, winner, key, toggle

    circle = []
    cross = []
    winner = []
    key = True
    toggle = False


def main():
    global r, toggle
    run = True
    while run:
        pygame.time.delay(50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if pygame.mouse.get_pressed()[0] and r and key:
            mouse_position = pygame.mouse.get_pos()
            r = False
            fill_box(mouse_position, toggle)
            toggle = not toggle

        if pygame.mouse.get_rel()[0]:
            r = True

        keys = pygame.key.get_pressed()

        if keys[pygame.K_r]:
            reset()

        draw_board()
        pygame.display.update()


main()
