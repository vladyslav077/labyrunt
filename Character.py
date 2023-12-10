import pygame


class Character:
    def __init__(self, x, y, h, w, speed, texture):
        self.speed = speed
        self.texture = pygame.image.load(texture)
        self.hit_box = self.texture.get_rect()
        self.hit_box.x = x
        self.hit_box.y = y
        self.texture = pygame.transform.scale(self.texture, (w, h))

    def render(self, window):
        window.blit(self.texture, (self.hit_box.x, self.hit_box.y ))



    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.hit_box.x += self.speed
        if keys[pygame.K_w]:
            self.hit_box.y -= self.speed
        if keys[pygame.K_a]:
            self.hit_box.x -= self.speed
        if keys[pygame.K_s]:
            self.hit_box.y += self.speed

