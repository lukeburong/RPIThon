
#test

import pygame, random, time, player_info
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640,480), 0)
screensize = screen.get_size()
center = [320,240]
centership = [288,226]
pygame.display.set_caption("Raspithon Game")

font = pygame.font.Font(None, 32)

fps = 60
clock = pygame.time.Clock()

black = [0,0,0]
white = [255,255,255]

background = pygame.Surface(screensize)
background = background.convert()
background.fill(black)

logo = "rptlogo.png"
logoload = pygame.image.load(logo)

running = True
playtime = 0.0
bgmusic = pygame.mixer.music.load("backgroundmusic.mp3")
pygame.mixer.init()
#pygame.mixer.music.play(-1) As requested until we finish


#Display the ship
player = player_info.Player(screen)
alien = player_info.Alien(screen, clock)
allSprites = pygame.sprite.Group(player)

while running:
    screen.blit(background,(0,0))
    pygame.display.flip()
    milliseconds = clock.tick(fps)
    playtime += milliseconds / 1000.0
    text = font.render("Frame rate: %.2f Playtime: %.2fs" % (clock.get_fps(),playtime), 1, white)
    background.fill(black)
    background.blit(text, (0,0))
    #pygame.draw.circle(background, (0,0,255), (320,240),25) 
    background.blit(player.image, player.rect)
    background.blit(alien.image, alien.rect)
    print(player.rect)
  
    alien.add()
    alien.update(1)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                
    
    #On keypress
    
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_RIGHT]:      
        player.turnRight()
    if keystate[pygame.K_LEFT]:
        player.turnLeft()
    

    