import pygame

class Figure():
    def __init__(self, pos, player, field):
        self.field = field
        self.display_pos = (1920 / 2 - 512, 1080 / 2 - 512)
        self.pos = pos
        self.player = player
        self.image = pygame.Surface((128, 128))
        self.image.fill((255, 0, 0))
        self.image.set_colorkey((255, 0, 0))
        pygame.draw.circle(self.image, (255 * (not self.player), 255 * (not self.player), 255 * (not self.player)), (64, 64), 50)
        self.rect = self.image.get_rect()
        self.rect.x = 128 * self.pos[0] + self.display_pos[0]
        self.rect.y = 128 * self.pos[1] + self.display_pos[1]
        if self.player == 0:
            self.movelist = ((-1, -1), (1, -1))
        else:
            self.movelist = ((-1, 1), (1, 1))
        self.attacklist = ((-1, -1), (1, -1), (-1, 1), (1, 1))
        self.moves = []

    def calculate_moves(self):
        for i in range(4):
            
        self.moves = []
        for i in range(2):
            new_pos = (self.pos[0] + self.movelist[i][0], self.pos[1] + self.movelist[i][1])
            if new_pos[0] >= 0 and new_pos[0] <= 7 and new_pos[1] >= 0 and new_pos[1] <= 7:
                if self.field[new_pos[0]][new_pos[1]] == None:
                    self.moves.append(new_pos)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
