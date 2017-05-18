import pygame

window = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Example')
screen = pygame.Surface((620, 460))
class Sprite:
    def __init__(self,x_pos,y_pos,filename,r,g,b):
        self.x = x_pos
        self.y = y_pos
        self.bitmap = pygame.image.load(filename)
        self.bitmap.set_colorkey((r,g,b))
    def render(self):
        screen.blit(self.bitmap,(self.x, self.y))
def inte(x1, x2 ,y1, y2):
    if (x1 > x2 - 40) and (x1 < x2 + 40) and (y1 > y2 + 40) and (y1 < y2 + 40):
        return 1
    else:
        return 0

hero = Sprite(0,400, 'piu.png',255,255,255)
hero.up = True
zet = Sprite(200, 100, 'enemy.png',0,0,0)
zet.up = False

done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False

    screen.fill((100,10,50))

    if hero.up == True:
        hero.y -=1
        if hero.y ==0:
            hero.up = False
    else:
        hero.y +=1
        if hero.y == 350:
            hero.up = True

    if zet.up == True:
        hero.y -=1
        if hero.y ==0:
            hero.up = False
    else:
        hero.y +=1
        if hero.y == 350:
            hero.up = True

    if inte(zet.x, hero.x, zet.y, hero.y) == True:
        hero.up = False
        zet.up = True

    hero.render()
    zet.render()
    window.blit(screen, (10,10))
    pygame.display.flip()
    pygame.time.delay(5)
