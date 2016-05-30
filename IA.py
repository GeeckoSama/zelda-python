from turtle import*
from random import*
from variable import*
from chargement_image import*
from matrice_map import*

##Fonction de L'IA des monstre
def mob_fun(mob,mob_move,alea_mob):
    #fonction de clignotement des monstre lors de degats recue
    for i in range(3): #on teste les variable des 3 monstres
        if mob_move[i][10]==True: #degat==True
            if mob_move[i][11]<6: #on fait clignote el monstre 6 fois
                if mob_move[i][11]%2==0: #on alterne les apparition du monstre
                    mob[i][0].st()
                else:
                    mob[i][0].ht()
                mob_move[i][11]+=1
            else:
                mob[i][0].st() #on remontre le monstre puis remet les variable d'origine
                mob_move[i][10]=False
                mob_move[i][11]=0
                
    if mob_move[alea_mob][5]==False and mob_move[alea_mob][7]==False:#si le mob est ni en deplacement ni en attaque
        mob_move[alea_mob][9]=randrange(0,100) #alea_move=random(nombre aleatoire)
    if mob_move[alea_mob][9]>=0 and mob_move[alea_mob][9]<5: #si le nombre aleatoire vaut 0 on se deplace vers le haut
        mob_move[alea_mob][4]=0
        if mob_move[alea_mob][5]==True: #la variable en deplacement passe a true
            if mob_move[alea_mob][6]%2==0: #si cpt est pair
                mob_move[alea_mob][1]+=2    #on augmente de 2 pixel sur y
            else:
                mob_move[alea_mob][1]+=3 # ou de 3 pixel afin d'avoir un total de 25 pixels de deplacement
        else:
            if m_map1[mob_move[alea_mob][2]-1][mob_move[alea_mob][3]]==0: #si on est pas bloquer par la matrice
                mob_move[alea_mob][5]=True                                  #la variable en deplacement passe a true
                m_map1[mob_move[alea_mob][2]][mob_move[alea_mob][3]]=0   #on deplace le monstre dans la matrice
                mob_move[alea_mob][2]-=1
                m_map1[mob_move[alea_mob][2]][mob_move[alea_mob][3]]=6
                
    elif mob_move[alea_mob][9]>=10 and mob_move[alea_mob][9]<15: #vers le bas
        mob_move[alea_mob][4]=1
        if mob_move[alea_mob][5]==True:
            if mob_move[alea_mob][6]%2==0: #si cpt est pair
                mob_move[alea_mob][1]-=2
            else:
                mob_move[alea_mob][1]-=3
        else:
            if m_map1[mob_move[alea_mob][2]+1][mob_move[alea_mob][3]]==0: #matrice=0
                mob_move[alea_mob][5]=True #in_deplacement=True
                m_map1[mob_move[alea_mob][2]][mob_move[alea_mob][3]]=0
                mob_move[alea_mob][2]+=1
                m_map1[mob_move[alea_mob][2]][mob_move[alea_mob][3]]=6
                
    elif mob_move[alea_mob][9]>=20 and mob_move[alea_mob][9]<25: #vers la gauche
        mob_move[alea_mob][4]=2
        if mob_move[alea_mob][5]==True:
            if mob_move[alea_mob][6]%2==0: #si cpt est pair
                mob_move[alea_mob][0]-=2
            else:
                mob_move[alea_mob][0]-=3
        else:
            if m_map1[mob_move[alea_mob][2]][mob_move[alea_mob][3]-1]==0: #matrice=0
                mob_move[alea_mob][5]=True #in_deplacement=True
                m_map1[mob_move[alea_mob][2]][mob_move[alea_mob][3]]=0
                mob_move[alea_mob][3]-=1
                m_map1[mob_move[alea_mob][2]][mob_move[alea_mob][3]]=6
                
    elif mob_move[alea_mob][9]>=30 and mob_move[alea_mob][9]<35: #vers la droite
        mob_move[alea_mob][4]=3
        if mob_move[alea_mob][5]==True:
            if mob_move[alea_mob][6]%2==0: #si cpt est pair
                mob_move[alea_mob][0]+=2
            else:
                mob_move[alea_mob][0]+=3
        else:
            if m_map1[mob_move[alea_mob][2]][mob_move[alea_mob][3]+1]==0: #matrice=0
                mob_move[alea_mob][5]=True #in_deplacement=True
                m_map1[mob_move[alea_mob][2]][mob_move[alea_mob][3]]=0
                mob_move[alea_mob][3]+=1
                m_map1[mob_move[alea_mob][2]][mob_move[alea_mob][3]]=6

    if mob_move[alea_mob][5]==True:#in_move
        mob[alea_mob][0].goto(mob_move[alea_mob][0],mob_move[alea_mob][1]) #goto xmob et ymob
        if mob_move[alea_mob][6]<11: #cpt<10
            mob[alea_mob][0].shape(octobrock[mob_move[alea_mob][4]][mob_move[alea_mob][6]]) #shape(direction+cpt)
            mob_move[alea_mob][6]+=1 #cpt++
            if mob_move[alea_mob][6]==11: #cpt==10
                mob_move[alea_mob][6]=0 #cpt=0
                mob_move[alea_mob][5]=False #in_move=False
                mob[alea_mob][0].shape(octobrock[mob_move[alea_mob][4]][0]) #shape fix

    #partie pour l'attaque des monstre
    if mob_move[alea_mob][9]>=40 and mob_move[alea_mob][9]<55 and mob_move[alea_mob][7]==False: #si la variable aleatoire vaut 5 et que l'on est pas en deplacement
        mob_move[alea_mob][7]=True #in_attack=true
        mob[alea_mob][1].goto(mob_move[alea_mob][0],mob_move[alea_mob][1]) #place la t_attack sur le mob
        mob[alea_mob][1].st()#montre la turtle d'attaque
                 
    if mob_move[alea_mob][7]: #in_attack==True
        
        if mob_move[alea_mob][4]==0: #vers le haut
            mob[alea_mob][1].goto(mob_move[alea_mob][0],mob_move[alea_mob][1]+mob_move[alea_mob][8]*25) #deplace de 25*cpt
            mob[alea_mob][1].shape(graine1) #shape de la graine
            mob_move[alea_mob][8]+=1 #cpt_attack++
            if mob_move[alea_mob][8]==10: #parcourue 10 case
                 mob[alea_mob][1].ht() #cacher la turtle
                 mob_move[alea_mob][8]=0 #cpt=0
                 mob_move[alea_mob][7]=False
            elif m_map1[mob_move[alea_mob][2]-mob_move[alea_mob][8]][mob_move[alea_mob][3]]==5: #toucher le joueur
                 link[3]-=mob[alea_mob][4] #degat du monstre sur link
                 link_move[10]=True         #fait clignote link
                 mob[alea_mob][1].ht()
                 mob_move[alea_mob][8]=0
                 mob_move[alea_mob][7]=False
            elif m_map1[mob_move[alea_mob][2]-mob_move[alea_mob][8]][mob_move[alea_mob][3]]==1: #toucher un obstacle
                 mob[alea_mob][1].ht()
                 mob_move[alea_mob][8]=0
                 mob_move[alea_mob][7]=False

        if mob_move[alea_mob][4]==1: #vers le bas
            mob[alea_mob][1].goto(mob_move[alea_mob][0],mob_move[alea_mob][1]-mob_move[alea_mob][8]*25) #deplace de 25*cpt
            mob[alea_mob][1].shape(graine1) #shape de la graine
            mob_move[alea_mob][8]+=1 #cpt_attack++
            if mob_move[alea_mob][8]==5:
                 mob[alea_mob][1].ht()
                 mob_move[alea_mob][8]=0
                 mob_move[alea_mob][7]=False
            elif m_map1[mob_move[alea_mob][2]+mob_move[alea_mob][8]][mob_move[alea_mob][3]]==5:
                 link[3]-=mob[alea_mob][4]
                 link_move[10]=True
                 mob[alea_mob][1].ht()
                 mob_move[alea_mob][8]=0
                 mob_move[alea_mob][7]=False
            elif m_map1[mob_move[alea_mob][2]+mob_move[alea_mob][8]][mob_move[alea_mob][3]]==1:
                 mob[alea_mob][1].ht()
                 mob_move[alea_mob][8]=0
                 mob_move[alea_mob][7]=False

        if mob_move[alea_mob][4]==2: #vers la gauche
            mob[alea_mob][1].goto(mob_move[alea_mob][0]-mob_move[alea_mob][8]*25,mob_move[alea_mob][1]) #deplace de 25*cpt
            mob[alea_mob][1].shape(graine1) #shape de la graine
            mob_move[alea_mob][8]+=1 #cpt_attack++
            if mob_move[alea_mob][8]==5:
                 mob[alea_mob][1].ht()
                 mob_move[alea_mob][8]=0
                 mob_move[alea_mob][7]=False
            elif m_map1[mob_move[alea_mob][2]][mob_move[alea_mob][3]-mob_move[alea_mob][8]]==5:
                 link[3]-=mob[alea_mob][4]
                 link_move[10]=True
                 mob[alea_mob][1].ht()
                 mob_move[alea_mob][8]=0
                 mob_move[alea_mob][7]=False
            elif m_map1[mob_move[alea_mob][2]][mob_move[alea_mob][3]-mob_move[alea_mob][8]]==1:
                 mob[alea_mob][1].ht()
                 mob_move[alea_mob][8]=0
                 mob_move[alea_mob][7]=False

        if mob_move[alea_mob][4]==3: #vers la droite
            mob[alea_mob][1].goto(mob_move[alea_mob][0]+mob_move[alea_mob][8]*25,mob_move[alea_mob][1]) #deplace de 25*cpt
            mob[alea_mob][1].shape(graine1) #shape de la graine
            mob_move[alea_mob][8]+=1 #cpt_attack++
            if mob_move[alea_mob][8]==5:
                 mob[alea_mob][1].ht()
                 mob_move[alea_mob][8]=0
                 mob_move[alea_mob][7]=False
            elif m_map1[mob_move[alea_mob][2]][mob_move[alea_mob][3]+mob_move[alea_mob][8]]==5:
                 link[3]-=mob[alea_mob][4]
                 link_move[10]=True
                 mob[alea_mob][1].ht()
                 mob_move[alea_mob][8]=0
                 mob_move[alea_mob][7]=False
            elif m_map1[mob_move[alea_mob][2]][mob_move[alea_mob][3]+mob_move[alea_mob][8]]==1:
                 mob[alea_mob][1].ht()
                 mob_move[alea_mob][8]=0
                 mob_move[alea_mob][7]=False
