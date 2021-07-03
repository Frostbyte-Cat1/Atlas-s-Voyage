import pygame as py
from pygame.draw import rect
py.init()

#programIcon = py.image.load('')
#py.display.set_icon(programIcon)
py.display.set_caption("Atlas's Voyage")
screen = py.display.set_mode((720,480))
screen.fill((255,255,255))

color=(255,0,0)
x = 100
y = 445
width = 30
height = 30
vel = 0.4

running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    keys = py.key.get_pressed()
    if keys[py.K_a] and x > vel + 5:
        x -= vel
    # vel + 5 = 5.4, this is so that the border spacing on the right side is the same as the leaft side
    if keys[py.K_d] and x < 720-width-5.4:
        x += vel
    #elif so that by holding eg. d and left arrow keys together, player won't double in speed
    elif keys[py.K_LEFT] and x > vel + 5:
        x -= vel
    elif keys[py.K_RIGHT] and x < 720-width-5.4:
        x += vel
    screen.fill((255,255,255))


    py.draw.rect(screen,color,(x,y,width,height))
    py.display.update()












py.quit()   