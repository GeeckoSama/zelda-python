#Importation de tous les modules complementaires
#Turtle : partie graphique
#random : generation de nombres aleatoires
#variable : fichier contenant toutes les variables du programme
#chargement image : fichier contenant tous les chargements des images pour les turtles
#matrice map : contient la matrice de la map utilisee pour gerer les collisions et les personnages
#Link fun : regroupe toutes les fonctions gerant le personnage jouable, les fonctions de deplacement
#les fonctions d'attaques, la gestion des degats
#IA : regroupe les fonctions de gestion des ennemies, deplacements, attaque, degats
#musique : gestion de la musique du jeu
from turtle import*
from random import*
from variable import*
from chargement_image import*
from matrice_map import*
from Link_fun import*
from IA import*
##from musique import*

#fonction de fin de jeu, affiche un ecran de fin
def game_over():
    link[0].ht() #on cache le personnage
    for i in range(3): #on cache tous les mosntres
        mob[i][0].ht()
        mob[i][1].ht()
        triforce[i].ht() #on cache toute les triforce
    for i in range(4):
        lt_interface[i].ht() #on cache l'interface
    bgpic("image\game_over.gif")

#fonction de fin de jeu si le joueur a gagner
def winner():
    link[0].ht()
    for i in range(3):
        mob[i][0].ht()
        mob[i][1].ht()
        triforce[i].ht()
    for i in range(4):
        lt_interface[i].ht()
    bgpic("image\win.gif")

#fonction de gestion de l'interface (point de vie joueur represente par des coeurs pleins ou vides)
#si la vie du personnage est inferieure a 3 la turtle devient vide en consequence de la vie du joueur
def gest_inter():
    for i in range(1,4):
        if link[3]==i or link[3]>i:
            lt_interface[i].shape(coeur_e)
        else:
            lt_interface[i].shape(coeur_v)

#boucle principale
#boucle verifiant que le jeu n'est pas fini ou perdu
#appel la fonction de gestion de l'interface
#tant que le joueur est encore en vie on continue
#creation d'une variable aleatoire definissant le monstre a  deplacer
#appel de la fonction de deplacement du joueur
#tant que le monstre est en vie on peut lancer la fonction
#sinon on fait disparaetre le monstre
#on fait deplacer le monstre
#si le personnage n'a plus de vie on arrete le jeu
#sinon on rappelle la boucle au bout de 20ms
def game_boucle():          #Fonction principale (Le jeu)
    gest_inter()
    if link[1]==True:
        alea_mob=randrange(3)#selection du monstre
        link_fun(link,link_move,alea_mob)
        if mob[alea_mob][3]<=0: #point de vie du monstre =0
            mob[alea_mob][2]=False
            mob[alea_mob][0].ht() #on cache sa turtle et celle de l'attaque
            mob[alea_mob][1].ht()
            m_map1[mob_move[alea_mob][2]][mob_move[alea_mob][3]]=0 #remplace dans la matrice le monstre par 0
        if mob[1][2]==False and mob[2][2]==False and mob[2][2]==False or link[2]==3: #si tout les monstres sont mort ou si toute la triforce est reunie
            winner() #appel fonction vous avez gagner
        if mob[alea_mob][2]==True: #si le monstre est en vie
            mob_fun(mob,mob_move,alea_mob)    
        if link[3]==0: #si les point de vie du personnage sont a 0
            link[1]=False #le personnage est mort
        ontimer(game_boucle,20) 
    else:
        game_over()

#fonction pour fermer la fenetre turtle avec la touche k
def exit_game():
    bye()

#fonction de mise en place de l'interface joueur(point de vie)
#les variable x et y sont les coordonnees de la mise en place de l'interface
#on deplace les turtles, on les fait apparaetre avec l'image d'un coeur plein
def interface_fun():
    x=-350
    y=270
    for i in range(4):
        lt_interface[i].up()
        if i==0:
            lt_interface[i].goto(x,y)
            lt_interface[i].shape(interface)
            lt_interface[i].st()
        else:
            lt_interface[i].goto(x,y)
            lt_interface[i].shape(coeur_e)
            lt_interface[i].st()
            x+=50

#fonction de chargement de la map
#on cache les boutons du menu
#on affiche en arriere plan l'image de la map
#on appelle la fonction de l'interface
#on initialise la position de la turtle du joueur
#on lance la boucle de jeu
#on lance la fonction de la gestion des entrees claviers
def load_map1(x,y):         #chargement du jeu
    t_play.ht()
    t_musique.ht()
    t_electro.ht()
    t_dubstep.ht()
    t_classique.ht()
    bgpic("image\map1.gif")
    interface_fun() 
    link[0].goto(-75,50)
    link[0].shape(link_image[1][0])
    for i in range(3):
        mob[i][0].goto(mob_move[i][0],mob_move[i][1])
        mob[i][0].shape(octobrock[0][0])
    t_tri_1.st()
    t_tri_2.st()
    t_tri_3.st()
    print()
    print("Sur ce : Bon courage jeune hÃ©ro vert")
    game_boucle()                   
    keyin()                         

#fonction de mise en place des boutons jouer et musique
def button():    
    t_play.goto(-245,0)              #boutton play
    t_play.shape(b_play)
    t_play.st()
    t_musique.up()                   #boutton musique
    t_musique.goto(-245,-50)
    t_musique.shape(b_musique)
    t_musique.st()
    click()

#fonction de la gestion des entrees sourie afin de cliquer sur les boutons du menu
def click():
    t_play.onclick(load_map1,1) #lance la fonction load_map1 si on click sur le boutton play
##    t_musique.onclick(Menu_musique,1)
##    t_electro.onclick(electro_play,1)
##    t_dubstep.onclick(dubstep_play,1)
##    t_classique.onclick(classique_play,1)

#fonction de gestion du menu musique afin de pouvoir selectionner la musique souhaitÃ©e   
##def Menu_musique(x,y):
##    t_play.ht()
##    t_musique.ht()
##    t_play.goto(-245,-200)
##    t_musique.goto(-600,0)
##    t_play.st()
##    t_electro.up()                 #bouton electro
##    t_electro.goto(-245,0)
##    t_electro.shape(b_electro)
##    t_electro.st()
##    t_dubstep.up()                 #bouton dubstep
##    t_dubstep.goto(-245,-50)
##    t_dubstep.shape(b_dubstep)
##    t_dubstep.st()
##    t_classique.up()                 #bouton classique
##    t_classique.goto(-245,-100)
##    t_classique.shape(b_classique)
##    t_classique.st()
##    click()

#chargement Menu
#definie la taille de la fenetre de jeu
#on affiche en arriÃ¨re plan l'image du menu
#on lance la fonction de gestion des boutons du menu
#on lance la fonction de gestion des clics souris
#on lance la fonction du demarrage de la musique
#on lance la musique
def Menu():
    setup(1000,600)                 #definition de la taille de la fenetre
    bgpic("image\menu.gif")    #affichage du fond d'ecran
    print("Bienvenu dans le jeu Link : The legend of minishcup (les jois du copyright).")
    print()
    print("vous allez incarnÃ© link un petit hÃ©ro (vert, trop vert) trÃ¨s courageux qui possÃ¨de la triforce.")
    print("la triforce se compose en trois partie, le courage, la sagesse et la force.")
    print("malheureusement notre hÃ©ro a Ã©garÃ© ces trois partie (Ã§a arrive mÃªme au meilleur vous savez) et se retrouve sans aide divine (oui car sans cela notre hÃ©ro est nul).")
    print()
    print("votre mission si vous l'accepter sinon fermer le jeu directement")
    print("vous vous trouvez actuellement dans une forÃªt lugubre (est mal faite faut l'avouer)remplie de monstre trÃ¨s dangereur(3 monstres pour Ãªtre prÃ©cie, et qui ne font que jetÃ© des graine)")
    print("vous devez donc aidez link en regroupant les morceaux de la triforce ou Ã©liminÃ© tous les monstres (mission d'une difficultÃ© extreme je tiens a prÃ©ciser)")
    button()                       #lancement de l'affiche des boutons
    click()                        #lancement du reperage des clics
    ##Menu_musique(x,y)

#appel de la fonction du menu, on demarre le jeu
Menu()                      

#fonction speciale pour turtle avec windows
mainloop()
