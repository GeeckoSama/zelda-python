#importation du module pygame pouvant gérer le son du jeu
import pygame
from pygame.locals import*
from pygame.mixer import*
from random import*

#fonction lançant la musique type electro
def electro_play(x,y):
    pygame.mixer.music.load("musique/electro1.wav")
    pygame.mixer.music.play()
    print("musique play")

#def dubstep_play():
def dubstep_play(x,y):
    pygame.mixer.music.load("musique/dub1.wav")
    pygame.mixer.music.play()
    print("musique play")

#fonction lançant la musique type classique
def classique_play(x,y):
    pygame.mixer.music.load("musique/clas1.wav")
    pygame.mixer.music.play()
    print("musique play")

#bruitage personnage
def voice():
    rand=randrange(3)
    if rand==0:
        voice=pygame.mixer.Sound("musique/voice1.wav")
    elif rand==1:
        voice=pygame.mixer.Sound("musique/voice2.wav")
    else:
        voice=pygame.mixer.Sound("musique/voice3.wav")
    voice.play()

#fonction de démarrage du module son de pygame
#on ouvre une fenêtre (obligatoire)
#on donne la taille de la fenêtre
def menu_play():
    pygame.init()
    fenetre = pygame.display.set_mode((100,50))

#variable booléenne pour la fonction de pause de la musique
pause=False
Music=[pause]

#fonction de pause/reprise de la musique
def pause_play():
    if Music[0]==False:
        pygame.mixer.music.pause()
        Music[0]=True
    else:
        pygame.mixer.music.unpause()
        Music[0]=False


##menu_play()
##electro_play()
