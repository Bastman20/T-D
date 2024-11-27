import pygame as pg
import  constants as c

#bring in pygame for use in the code
pg.init()

time = pg.time.Clock() #clock



#create game window 
screen = pg.display.set_mode((c.ScreenWidth, c.ScreenHeight))
pg.display.set_caption("Tower Defense")

#images
ei = pg.image.load() #enemy image

#To loop the game
run = True
while run:

    time.tick(c.Ticky)
   
    for stuff in pg.event.get():
        if stuff.type == pg.QUIT:
            run = False



pg.quit()