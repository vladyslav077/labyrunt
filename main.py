import pygame

import Character
import Enemy
import gold
from Wall import wall
from gold import Gold

pygame.init()

window = pygame.display.set_mode((800, 500))
fps = pygame.time.Clock()

fon = pygame.image.load("background2.png")
fon = pygame.transform.scale(fon, (800, 500))

pacman = Character.Character(250, 350, 50, 50, 5, "hero.png")
enemy = Enemy.Enemy(200, 300, 50, 50, 5, "cyborg.png", 100, 200, 300, 300)
gold = goldenemy.Gold(50, 50, 75, 75, "treasure.png")
game = True
walls = []
walls.append(wall(220, 40, 100, 20,(255,255,0)))
walls.append(wall(220, 40, 100, 20,(255,255,0)))
while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()
    pacman.move()
    enemy.move()
    window.fill((123, 255, 123))
    window.blit(fon, (0, 0))
    pacman.render(window)
    enemy.render(window)
    gold.render(window)
    for Wall in walls:
        Wall.render(window)
    pygame.display.flip()
    fps.tick(60)
