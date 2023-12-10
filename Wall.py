import pygame

class wall:

    def __init__(self, x, y, h, w, color):
        self.rect = pygame.rect.Rect(x,y,w,h)
        self.color = color


    def render(self,window):
        pygame.draw.rect(window, self.rect, self.color)




