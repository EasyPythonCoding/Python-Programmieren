# Pygame Importieren
import pygame as pg
import sys

# Pygame Initialisieren
pg.init()

# Fenster Breite und Höhe
WIDTH = 1280 # Pixel
HEIGHT = 800 # Pixel

FPS = 120

# Fenster erstellen
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

# Fenster Titel setzen
pg.display.set_caption("Fenster 1 - Python Tutorial")

# Gameloop
while True:

    # Eventloop
    for event in pg.event.get():
        
        # Fenster Beenden
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    
    # Fenster Inhalt
    screen.fill("white")

    # Fenster Update
    pg.display.update()
    clock.tick(FPS)
