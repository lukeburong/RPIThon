#Alpha, with Sarah Lasonia's edits! RasPi FTW!
#2012

import pygame, random, time, player_info, moveable_dude, os # They forgot os -.-
from pygame.locals import *
from random import randint

randnum = randint(2,3) # 1 to 4, code is inclusive

pygame.init()

if randnum == 1:	# Sarah added randomised titles.
	rand = "Oh no, not the Aliens!"

if randnum == 2:	# Sarah added randomised titles.
	rand = "Spaaaccceee!"

if randnum == 3:	# Sarah added randomised titles.
	rand = "Developed by the RasPi Community!"

if randnum == 4:	# Sarah added randomised titles.
	rand = "Cheeseburgers are tasty."

screen = pygame.display.set_mode((640,480), 0)
screensize = screen.get_size()
center = [320,240]
centership = [288,226]
pygame.display.set_caption("Raspithon Game | A collaborative Project | " + rand) # Sarah added randomised titles.
pygame.mouse.set_visible(False) # We don't want the mouse to block the way.

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
# pygame.mixer.music.play(-1) As requested until we finish

#Display the ship
player = player_info.Player(screen)
alien = player_info.Alien(screen, clock)
move = moveable_dude.MoveableDude()
allSprites = pygame.sprite.Group(player)

moveable_dude.initialiseDudes(10) #Creds to Cakez0r for helping me out with this

while running:
    screen.blit(background,(0,0)) # comment
    pygame.display.flip() # comment
    milliseconds = clock.tick(fps) # comment
    hp = player.hp
    playtime += milliseconds / 1000.0 # comment
    text = font.render("Frame rate: %.2f Playtime: %.2fs HP: %.2f" % (clock.get_fps(),playtime,hp), 1, white) # comment
    background.fill(black) # comment
    background.blit(text, (0,0)) # comment
    #pygame.draw.circle(background, (0,0,255), (320,240),25) 
    background.blit(player.image, player.rect)
    background.blit(alien.image, alien.rect)
    moveable_dude.updateAndDrawDudes(background)

    print(player.rect)
  
    alien.add()
    alien.update(1)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                
    
    if hp == 0:
        pygame.quit()
    
    #On keypress        
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_RIGHT]:      # Key right
        player.turnRight()
    if keystate[pygame.K_LEFT]:		# Key Left
        player.turnLeft()
    if keystate[pygame.K_F12]:
        moveable_dude.initialiseDudes(900)
    if keystate[pygame.K_q]:
        pygame.quit()
        

    
