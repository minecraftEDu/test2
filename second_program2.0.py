# coding: utf8
import pygame
import random

# задааем размер окна, создаем окно размера size
size = [400, 400]
window = pygame.display.set_mode(size)
# задаем имя - в кавычках, т.к. текст - это строка
pygame.display.set_caption('My second file')
speed = 1
screen = pygame.Surface(size)

class Sprite:
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)
    def render(self):
        screen.blit(self.bitmap,(self.x, self.y))


def Intersect(s1_x, s2_x, s1_y, s2_y):
    if ((s1_x>s2_x-40) and (s1_x<s2_x+40) and (s1_y>s2_y-40) and (s1_y<s2_y+40)):
        return 1
    else:
        return 0

# создание персонажей
# герой
hero = Sprite(200, 350, 'archer.png')
# переменные-"переключатели" движения для героя
hero.right = True
hero.up = True
# враг
enemy = Sprite(200, 3, 'dragon.png')
# переменные-"переключатели" движения для врага
enemy.right = True
enemy.up = False

weapon = Sprite(-100, -100, 'arrow.png')
weapon.push = False

running = True
while running:
    # обработка событий
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running  = False
        # движение героя
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                if hero.x > 10:
                    hero.x -= 10
            if e.key == pygame.K_RIGHT:
                if hero.x < 350:
                    hero.x += 10
            if e.key == pygame.K_UP:
                if hero.y > 200:
                    hero.y -= 10
            if e.key == pygame.K_DOWN:
                if hero.y < 350:
                    hero.y += 10
            if e.key == pygame.K_SPACE:
                if weapon.push == False:
                    weapon.x = hero.x - 15
                    weapon.y = hero.y
                    weapon.push = True
    # задайте фоновый цвет
    screen.fill([23, 198, 93])

    # движение персонажей - аналогично тому,
    # что делали с квадратом, но теперь по вертикали
    if enemy.right == True:
        enemy.x += speed
        if enemy.x > 360:
            enemy.right = False
    else:
        enemy.x -= speed
        if enemy.x < 0:
            enemy.right = True
    #enemy.x = random.randint(0, 400)
    #enemy.y = random.randint(0, 400)
    if weapon.push == True:
        weapon.y = weapon.y - 14
        if weapon.y < 0:
            weapon.push = False
            weapon.x = -100
            weapon.y = -100
    # столкновение персонажей
    if Intersect(hero.x, enemy.x, hero.y, enemy.y):
        hero.up = False
        enemy.up = True

    # отображение персонажей
    hero.render()
    enemy.render()
    weapon.render()
    # отображение окна
    window.blit(screen, [0, 0])
    pygame.display.flip()
    pygame.time.delay(50)


pygame.quit()