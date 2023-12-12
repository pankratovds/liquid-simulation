import pygame as pg
pg.init()
pg.draw.rect(50, 50, 100, 100)
def visualize(event):
    if event.button== self.mouse_button:
       if self.rect.contains(event.pos, 1, 1):
           main()
for event in pg.event.get():
    if event.type==pg.MOUSEBUTTONDOWN:
        visualize()
class Rect:
    default_color = "brown"
    def __init__(self, width, height):
        self.width = 50
        self.height = 50
        
class Text:  

sc = pygame.display.set_mode((300,200))
sc.fill((255, 255, 255))

f1 = pygame.font.Font(None, 36)
text1 = f1.render('Модель: квадрат', 1, (180, 0, 0))
text2 = f2.render('Модель: треугольник', 1, (180, 0, 0))
text3 = f3.render('Модель: круг', 1, (180, 0, 0))


sc.blit(text1, (10, 50))
sc.blit(text2, (10, 50))
sc.blit(text3, (10, 50))


pygame.display.update()

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

        
        
