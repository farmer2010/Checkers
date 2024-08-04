import pygame
from random import randint as rand
import figure
pygame.init()

screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Checkers")
background = pygame.Surface((8, 8))
background.fill((171, 127, 66))
for x in range(8):
    for y in range(8):
        if (x % 2 == 0) != (y % 2 == 0):
            pygame.draw.rect(background, (55, 26, 0), (x, y, 1, 1))
background = pygame.transform.scale(background, (1024, 1024))
selection = None

keep_going = True
display_pos = (1920 / 2 - 512, 1080 / 2 - 512)
field = [[None for i in range(8)] for j in range(8)]
for y in range(8):
    for x in range(8):
        if not((x % 2 == 0) != (y % 2 == 0)):
            if y <= 2:
                field[x][y] = figure.Figure((x, y), 1, field)
            elif y >= 5:
                field[x][y] = figure.Figure((x, y), 0, field)
player = 0

def calculate_moves():
    for y in range(8):
        for x in range(8):
            if field[x][y] != None and field[x][y].player == player:
                field[x][y].calculate_moves()

calculate_moves()

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                keep_going = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousepos = pygame.mouse.get_pos()
            if (mousepos[0] > display_pos[0] and mousepos[0] < display_pos[0] + 1024) and (mousepos[1] > display_pos[1] and mousepos[1] < display_pos[1] + 1024):
                pos = (int((mousepos[0] - display_pos[0]) // 128), int((mousepos[1] - display_pos[1]) // 128))
                if field[pos[0]][pos[1]] != None:#если на клетке есть фигура
                    if field[pos[0]][pos[1]].player == player:#если фигура принадлежит текущему игроку, перезаписать выбранную фигуру
                        selection = field[pos[0]][pos[1]]
                    else:#если фигура не принадлежит текущему игроку, сбросить выбранную фигуру
                        selection = None
                if field[pos[0]][pos[1]] == None and selection != None and pos in selection.moves:#если выбрана фигура и она может двигаться, передвижение
                    field[selection.pos[0]][selection.pos[1]] = None
                    selection.pos = pos
                    selection.rect.x = 128 * pos[0] + display_pos[0]
                    selection.rect.y = 128 * pos[1] + display_pos[1]
                    field[pos[0]][pos[1]] = selection
                    selection = None
                    player = not player
                    calculate_moves()
                if selection != None and field[pos[0]][pos[1]] == None and not pos in selection.moves:
                    selection = None
            else:
                selection = None
        screen.fill((90, 90, 90))
        screen.blit(background, (display_pos[0], display_pos[1]))
        #for x in range(8):
        #    for y in range(8):
        #        if field[x][y] == None:
        #            pygame.draw.rect(screen, (255, 255, 255), (128 * x + display_pos[0], 128 * y + display_pos[1], 128, 128))
        #        else:
        #            pygame.draw.rect(screen, (0, 0, 0), (128 * x + display_pos[0], 128 * y + display_pos[1], 128, 128))
        for y in range(8):
            for x in range(8):
                if field[x][y] != None:
                    field[x][y].draw(screen)
        if selection != None:
            for i in range(len(selection.moves)):
                pygame.draw.circle(screen, (0, 255, 0), (128 * selection.moves[i][0] + display_pos[0] + 64, 128 * selection.moves[i][1] + display_pos[1] + 64), 25)
        pygame.display.update()
pygame.quit()
