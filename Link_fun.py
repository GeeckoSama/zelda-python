from turtle import*
from variable import*
from chargement_image import*
from matrice_map import*
##from musique import*

#fonction de gestion du personnage
def link_fun(link,link_move,alea_mob):
    if link_move[5]:                        #si le personnage est en mouvement
        if link_move[4]==0:                 #si la direction est vers le haut
            if link_move[6]<6:         #tant que le compteur de mouvement est inferieur a 6
                link_move[1]+=4        #se deplace de 6 fois 4 pixels sur
            else:
                link_move[1]+=1        #sinon on se deplace de 1 pixel sur y afin d'avoir 25 pixel de deplacement total
            
        elif link_move[4]==1: #vers le bas
            if link_move[6]<6:
                link_move[1]-=4
            else:
                link_move[1]-=1
                 
        elif link_move[4]==2: #vers la gauche
            if link_move[6]<6:
                link_move[0]-=4        #se deplace de 6 fois 4 pixels sur x
            else:
                link_move[0]-=1
                 
        elif link_move[4]==3: #vers la droite
            if link_move[6]<6:
                link_move[0]+=4
            else:
                link_move[0]+=1

        #on deplace la turtle du personnage avec les nouveaux x et y de la turtle
        link[0].goto(link_move[0],link_move[1])
        
        if link_move[6]<7:                                              #quand le compteur de deplacement est inferieur a 7
            link[0].shape(link_image[link_move[4]][link_move[6]]) #la turtle du personnage prend l'image de deplacement en fonction du compteur
            link_move[6]+=1                                             #incrementation de compteur de deplacement
            if link_move[6]==7:         #si le compteur vaut 7
                link_move[6]=0          #on le remet a 0
                link[0].shape(link_image[link_move[4]][0])          #et la turtle prend la forme fixe

                #si la direction est 0(vers le haut)
                if link_move[4]==0:
                    m_map1[link_move[2]][link_move[3]]=0 #ancienne case =0
                    link_move[2]-=1 #deplacement dans la matrice
                    m_map1[link_move[2]][link_move[3]]=5 #new case=5
                elif link_move[4]==1:#vers le bas
                    m_map1[link_move[2]][link_move[3]]=0 #ancienne case =0
                    link_move[2]+=1 #deplacement dans la matrice
                    m_map1[link_move[2]][link_move[3]]=5 #new case=5
                elif link_move[4]==2:#vers la gauche
                    m_map1[link_move[2]][link_move[3]]=0 #ancienne case =0
                    link_move[3]-=1 #deplacement dans la matrice
                    m_map1[link_move[2]][link_move[3]]=5 #new case=5
                elif link_move[4]==3:#vers la droite
                    m_map1[link_move[2]][link_move[3]]=0 #ancienne case =0
                    link_move[3]+=1 #deplacement dans la matrice
                    m_map1[link_move[2]][link_move[3]]=5 #new case=5
                link_move[5]=False #in_move=False)

    #gestion de l'attaque
    if link_move[8]:#si le personnage est en attaque
        if link_move[9]<4: #si le compteur est inferieur a 4
            link[0].shape(link_attack[link_move[4]][link_move[9]]) #shape attack(compteur)
            link_move[9]+=1 #incrementation du compteur
            #si la direction est vers le haut et que la case suivante possede un ennemie et que le compteur = 3
            if link_move[4]==0 and m_map1[link_move[2]-1][link_move[3]]==6 and link_move[9]==3: #si le personnage va vers le haut et que la case de la matrice suivante est libre et que le compteur d'attaque =3
                #on test quel monstre a et touche 
                for i in range(0,3): #on test chaque monstre
                    if link[0].distance(mob[i][0])==25:#on verifie la distance de chaque monstres avec le joueur si c'est = 25
                        mob[i][3]=mob[i][3]-link[4]    #on fait baisser la vie du monstre
                        mob_degat=i                    #on recupere la variable i
                        mob_move[mob_degat][10]=True   #on lance le glignotement du monstre touche
            #si la direction est vers le bas
            elif link_move[4]==1 and m_map1[link_move[2]+1][link_move[3]]==6 and link_move[9]==3:
                for i in range(0,3): 
                    if link[0].distance(mob[i][0])==25:
                        mob[i][3]=mob[i][3]-link[4]
                        mob_degat=i
                        mob_move[mob_degat][10]=True
            #si elle est vers la gauche
            elif link_move[4]==2 and m_map1[link_move[2]][link_move[3]-1]==6 and link_move[9]==3:
                for i in range(0,3):
                    if link[0].distance(mob[i][0])==25:
                        mob[i][3]=mob[i][3]-link[4]
                        mob_degat=i
                        mob_move[mob_degat][10]=True
            #si elle est vers la droite
            elif link_move[4]==3 and m_map1[link_move[2]][link_move[3]+1]==6 and link_move[9]==3:
                for i in range(0,3):
                    if link[0].distance(mob[i][0])==25:
                        mob[i][3]=mob[i][3]-link[4]
                        mob_degat=i
                        mob_move[mob_degat][10]=True
                        
        #sinon on remet l'image du personnage fixe
        #on remet le compteur a 0
        #et on passe le booleen en attaque a false
        else:
            link[0].shape(link_attack[link_move[4]][4])
            link_move[9]=0
            link_move[8]=False
            
    if link_move[10]==True: #degat == True
        if link_move[11]<10: #tant que le compteur est inferieur 10
            if link_move[11]%2==0: #alterne si on montre la turtle ou pas
                link[0].ht() #cache la turtle
            else:
                link[0].st() #montre la turtle
            link_move[11]+=1
        else:
            link[0].st() #quand on fini on montre la turtle
            link_move[11]=0     #on repasse les variable d'origine
            link_move[10]=False

            
##Fonction appeler par le onkey()

def to_up(): #allez vers le haut
    if link_move[7]!=0 and link_move[5]==False: #si link est fixe et la direction !=0
        link_move[7]=0#la variable fixe passe a la direction haut
        link_move[4]=0#la direction prend vers le haut
        link[0].shape(link_image[0][0]) #shape regardez vers le haut
    for i in range(0,3): #on regarde si la distance entre le personnage et les triforce sont =0
        if link[0].distance(triforce[i])==0: #si oui
            triforce[i].goto(350-50*link[2],270) #on deplace la triforce en haut
            link[2]+=1 #on incremente la variable qui compte le nombre de triforce recuperer
    if m_map1[link_move[2]-1][link_move[3]]==0 and link_move[5]==False and link_move[7]==0: #case matrice suivante libre et in_move=False
        link_move[5]=True #in_move=true

def to_down(): #allez vers le bas
    if link_move[7]!=1 and link_move[5]==False: #si link est fixe et la direction !=0
        link_move[7]=1
        link_move[4]=1
        link[0].shape(link_image[1][0]) #shape regardez vers le haut
    for i in range(0,3):
        if link[0].distance(triforce[i])==0:
            triforce[i].goto(350-50*link[2],270)
            link[2]+=1
    if m_map1[link_move[2]+1][link_move[3]]==0 and link_move[5]==False and link_move[7]==1: #case matrice suivante libre et in_move=False
        link_move[5]=True #in_move=true

def to_left(): #allez vers la gauche
    if link_move[7]!=2 and link_move[5]==False: #si link est fixe et la direction !=0
        link_move[7]=2
        link_move[4]=2
        link[0].shape(link_image[2][0]) #shape regardez vers le haut
    for i in range(0,3):
        if link[0].distance(triforce[i])==0:
            triforce[i].goto(350-50*link[2],270)
            link[2]+=1
    if m_map1[link_move[2]][link_move[3]-1]==0 and link_move[5]==False and link_move[7]==2: #case matrice suivante libre et in_move=False
        link_move[5]=True #in_move=true

def to_right(): #allez vers la droite
    if link_move[7]!=3 and link_move[5]==False: #si link est fixe et la direction !=0
        link_move[7]=3
        link_move[4]=3
        link[0].shape(link_image[3][0]) #shape regardez vers le haut
    for i in range(0,3):
        if link[0].distance(triforce[i])==0:
            triforce[i].goto(350-50*link[2],270)
            link[2]+=1
    if m_map1[link_move[2]][link_move[3]+1]==0 and link_move[5]==False and link_move[7]==3: #case matrice suivante libre et pas en deplacement
        link_move[5]=True #en deplacement
        
def attack(): #fonction d'appel de l'attaque
    if link_move[5]==False and link_move[8]==False: #si le personnage n'est ni en deplacement ni en attaque
        link_move[8]=True   #on lance l'attaque
        ##voice() #bruitage d'attaque

#fonction pour fermer la fenetre turtle avec la touche k
def exit_game():
    bye()
    
def keyin():                #Fonction d'enregistrement clavier
    onkey(to_up,"z")            #deplacement vers le haut
    onkey(to_down,"s")          #deplacement vers le bas
    onkey(to_left,"q")          #deplacement vers la gauche
    onkey(to_right,"d")         #dplacement vers la droite
    onkey(attack,"a")           #attaque du joueur
    onkey(exit_game,"k")        #fermer la fenetre turtle
    ##onkey(pause_play,"p")       #met la musique en pause
    listen()                #enregistre les entrees clavier

