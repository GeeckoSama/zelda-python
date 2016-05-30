from turtle import*
from chargement_image import*

##Link
#variable(de mouvement)du personnage
x_link,y_link,casx_link,casy_link,direc,in_move,cpt_dep,link_fix,in_attack,cpt_attack,degat,cpt_degat=-75,50,10,17,0,False,0,0,False,0,False,0

#variable (de jeu) du personnage
stat,live,pv,attack=0,True,3,1

#turtle du personnage
t_link=clone()
t_link.up()

#liste mouvement
link_move=[x_link,y_link,casx_link,casy_link,direc,in_move,cpt_dep,link_fix,in_attack,cpt_attack,degat,cpt_degat]

#liste jeu  (personnage)
link=[t_link,live,stat,pv,attack,link_move,link_image]


##Monstres
#variable (de mouvement) de chaque monstres
x_mob_1,y_mob_1,casx_mob_1,casy_mob_1,direc_mob_1,in_move_mob_1,cpt_dep_mob_1,in_attack_mob_1,cpt_attack_mob_1,alea_move_1,m_degat_1,m_cpt_degat_1=375,50,10,35,0,False,0,False,0,0,False,0
x_mob_2,y_mob_2,casx_mob_2,casy_mob_2,direc_mob_2,in_move_mob_2,cpt_dep_mob_2,in_attack_mob_2,cpt_attack_mob_2,alea_move_2,m_degat_2,m_cpt_degat_2=-375,-200,20,5,0,False,0,False,0,0,False,0
x_mob_3,y_mob_3,casx_mob_3,casy_mob_3,direc_mob_3,in_move_mob_3,cpt_dep_mob_3,in_attack_mob_3,cpt_attack_mob_3,alea_move_3,m_degat_3,m_cpt_degat_3=-75,-75,15,17,0,False,0,False,0,0,False,0


#variable (de jeu) de chaque monstres
live_mob_1,Pv_mob_1,attack_mob_1=True,3,1
live_mob_2,Pv_mob_2,attack_mob_2=True,3,1
live_mob_3,Pv_mob_3,attack_mob_3=True,3,1


#Turtle de chaque monstres
#Monstre 1
t_mob_1=clone()
t_attack_mob_1=clone()
t_mob_1.up()
t_attack_mob_1.up()
t_attack_mob_1.ht()
#Monstre 2
t_mob_2=clone()
t_attack_mob_2=clone()
t_mob_2.up()
t_attack_mob_2.up()
t_attack_mob_2.ht()
#Monstre 3
t_mob_3=clone()
t_attack_mob_3=clone()
t_mob_3.up()
t_attack_mob_3.up()
t_attack_mob_3.ht()

#matrice des mouvements
mob_move=[[x_mob_1,y_mob_1,casx_mob_1,casy_mob_1,direc_mob_1,in_move_mob_1,cpt_dep_mob_1,in_attack_mob_1,cpt_attack_mob_1,alea_move_1,m_degat_1,m_cpt_degat_1],
          [x_mob_2,y_mob_2,casx_mob_2,casy_mob_2,direc_mob_2,in_move_mob_2,cpt_dep_mob_2,in_attack_mob_2,cpt_attack_mob_2,alea_move_2,m_degat_2,m_cpt_degat_2],
          [x_mob_3,y_mob_3,casx_mob_3,casy_mob_3,direc_mob_3,in_move_mob_3,cpt_dep_mob_3,in_attack_mob_3,cpt_attack_mob_3,alea_move_3,m_degat_3,m_cpt_degat_3]]


#matrice de jeu
mob=[[t_mob_1,t_attack_mob_1,live_mob_1,Pv_mob_1,attack_mob_1,octobrock],
     [t_mob_2,t_attack_mob_2,live_mob_2,Pv_mob_2,attack_mob_2,octobrock],
     [t_mob_3,t_attack_mob_3,live_mob_3,Pv_mob_3,attack_mob_3,octobrock]]

#Variable aleatoire definissant le monstre
alea_mob=0
mob_degat=0

##Turtle pour l'interface
t_interface=clone()
t_coeur_1=clone()
t_coeur_2=clone()
t_coeur_3=clone()
t_interface.ht()
t_coeur_1.ht()
t_coeur_2.ht()
t_coeur_3.ht()
#liste des turtles pour l'interface
lt_interface=[t_interface,t_coeur_1,t_coeur_2,t_coeur_3]

#Turtle pour le Menu
t_play=clone()
t_musique=clone()
t_retour=clone()
t_electro=clone()
t_dubstep=clone()
t_classique=clone()
t_play.up()
t_musique.up()
t_retour.up()
t_electro.up()
t_dubstep.up()
t_classique.up()
t_play.ht()
t_musique.ht()
t_retour.ht()
t_electro.ht()
t_dubstep.ht()
t_classique.ht()

#trutel pour la triforce
t_tri_1=clone()
t_tri_1.ht()
t_tri_1.up()
t_tri_1.speed(0)
t_tri_1.goto(75,-50)
t_tri_1.shape(s_triforce)
t_tri_2=clone()
t_tri_2.ht()
t_tri_2.up()
t_tri_2.speed(0)
t_tri_2.goto(400,75)
t_tri_2.shape(s_triforce)
t_tri_3=clone()
t_tri_3.ht()
t_tri_3.up()
t_tri_3.speed(0)
t_tri_3.goto(400,-200)
t_tri_3.shape(s_triforce)

triforce=[t_tri_1,t_tri_2,t_tri_3]
