import pygame as pg

print('Setup start')
pg.init()
# Criando uma janela
window = pg.display.set_mode(size=(600, 480))
print('Setup end')

print('Loop Start')
while True:
    # Check for all events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            # Close window
            pg.quit()
            # end pygame
            quit()
