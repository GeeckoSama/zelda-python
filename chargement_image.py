from turtle import*

#recuperation des liens des images

#image fixe et en mouvement de link
fix_up_1="image/link/fix_up.gif"
fix_down_1="image/link/fix_down.gif"
fix_left_1="image/link/fix_left.gif"
fix_right_1="image/link/fix_right.gif"
m_up_1="image/link/mup_1.gif"
m_up_2="image/link/mup_2.gif"
m_up_3="image/link/mup_3.gif"
m_up_4="image/link/mup_4.gif"
m_up_5="image/link/mup_5.gif"
m_up_6="image/link/mup_6.gif"
m_down_1="image/link/mdown_1.gif"
m_down_2="image/link/mdown_2.gif"
m_down_3="image/link/mdown_3.gif"
m_down_4="image/link/mdown_4.gif"
m_down_5="image/link/mdown_5.gif"
m_down_6="image/link/mdown_6.gif"
m_left_1="image/link/mleft_1.gif"
m_left_2="image/link/mleft_2.gif"
m_left_3="image/link/mleft_3.gif"
m_left_4="image/link/mleft_4.gif"
m_left_5="image/link/mleft_5.gif"
m_left_6="image/link/mleft_6.gif"
m_right_1="image/link/mright_1.gif"
m_right_2="image/link/mright_2.gif"
m_right_3="image/link/mright_3.gif"
m_right_4="image/link/mright_4.gif"
m_right_5="image/link/mright_5.gif"
m_right_6="image/link/mright_6.gif"
a_up_1="image/link/hit_up_1.gif"
a_up_2="image/link/hit_up_2.gif"
a_up_3="image/link/hit_up_3.gif"
a_up_4="image/link/hit_up_4.gif"
a_down_1="image/link/hit_down_1.gif"
a_down_2="image/link/hit_down_2.gif"
a_down_3="image/link/hit_down_3.gif"
a_down_4="image/link/hit_down_4.gif"
a_left_1="image/link/hit_left_1.gif"
a_left_2="image/link/hit_left_2.gif"
a_left_3="image/link/hit_left_3.gif"
a_left_4="image/link/hit_left_4.gif"
a_right_1="image/link/hit_right_1.gif"
a_right_2="image/link/hit_right_2.gif"
a_right_3="image/link/hit_right_3.gif"
a_right_4="image/link/hit_right_4.gif"

#mouvements du monstre
oc_haut_1="image/monstre/octobrock/move_up1.gif"
oc_haut_2="image/monstre/octobrock/move_up2.gif"
oc_haut_hit_1="image/monstre/octobrock/attack_up1.gif"
oc_haut_hit_2="image/monstre/octobrock/attack_up2.gif"
oc_bas_1="image/monstre/octobrock/move_down1.gif"
oc_bas_2="image/monstre/octobrock/move_down2.gif"
oc_bas_hit_1="image/monstre/octobrock/attack_down1.gif"
oc_bas_hit_2="image/monstre/octobrock/attack_down2.gif"
oc_gauche_1="image/monstre/octobrock/move_left1.gif"
oc_gauche_2="image/monstre/octobrock/move_left2.gif"
oc_gauche_git_1="image/monstre/octobrock/attack_left1.gif"
oc_gauche_hit_2="image/monstre/octobrock/attack_left2.gif"
oc_droite_1="image/monstre/octobrock/move_right1.gif"
oc_droite_2="image/monstre/octobrock/move_right2.gif"
oc_droite_hit_1="image/monstre/octobrock/attack_right1.gif"
oc_droite_hit_2="image/monstre/octobrock/attack_right2.gif"
graine1="image/monstre/octobrock/graine1.gif"

#interface
coeur_e="image/interface/coeur-entier.gif"
coeur_v="image/interface/coeur-vide.gif"
interface="image/interface/interface.gif"

#Menu
b_play=("image/Menu/play.gif")
b_retour=("image/Menu/retour.gif")
b_musique=("image/Menu/musique.gif")
b_electro=("image/Menu/electro.gif")
b_dubstep=("image/Menu/dubstep.gif")
b_classique=("image/Menu/classique.gif")

#triforce
s_triforce=("image/triforce.gif")

#enregistrement des images en shape turtle
register_shape(fix_up_1)
register_shape(fix_down_1)
register_shape(fix_left_1)
register_shape(fix_right_1)
register_shape(m_up_1)
register_shape(m_up_2)
register_shape(m_up_3)
register_shape(m_up_4)
register_shape(m_up_5)
register_shape(m_up_6)
register_shape(m_down_1)
register_shape(m_down_2)
register_shape(m_down_3)
register_shape(m_down_4)
register_shape(m_down_5)
register_shape(m_down_6)
register_shape(m_left_1)
register_shape(m_left_2)
register_shape(m_left_3)
register_shape(m_left_4)
register_shape(m_left_5)
register_shape(m_left_6)
register_shape(m_right_1)
register_shape(m_right_2)
register_shape(m_right_3)
register_shape(m_right_4)
register_shape(m_right_5)
register_shape(m_right_6)
register_shape(a_up_1)
register_shape(a_up_2)
register_shape(a_up_3)
register_shape(a_up_4)
register_shape(a_down_1)
register_shape(a_down_2)
register_shape(a_down_3)
register_shape(a_down_4)
register_shape(a_left_1)
register_shape(a_left_2)
register_shape(a_left_3)
register_shape(a_left_4)
register_shape(a_right_1)
register_shape(a_right_2)
register_shape(a_right_3)
register_shape(a_right_4)

register_shape(oc_haut_1)
register_shape(oc_haut_2)
##register_shape(oc_haut_hit_1)
##register_shape(oc_haut_hit_2)
register_shape(oc_bas_1)
register_shape(oc_bas_2)
##register_shape(oc_bas_hi_t1)
##register_shape(oc_bas_hi_t2)
register_shape(oc_gauche_1)
register_shape(oc_gauche_2)
##register_shape(oc_gauche_hit_1)
##register_shape(oc_gauche_hit_2)
register_shape(oc_droite_1)
register_shape(oc_droite_2)
##register_shape(oc_droite_hit_1)
##register_shape(oc_droite_hit_2)
register_shape(graine1)

#interface
register_shape(coeur_e)
register_shape(coeur_v)
register_shape(interface)

#Menu
register_shape(b_play)
register_shape(b_musique)
register_shape(b_retour)
register_shape(b_electro)
register_shape(b_dubstep)
register_shape(b_classique)

#Triforce
register_shape(s_triforce)

#liste des mouvements
link_image=[[fix_up_1,m_up_1,m_up_2,m_up_3,m_up_4,m_up_5,m_up_6],
           [fix_down_1,m_down_1,m_down_2,m_down_3,m_down_4,m_down_5,m_down_6],
           [fix_left_1,m_left_1,m_left_2,m_left_3,m_left_4,m_left_5,m_left_6],
           [fix_right_1,m_right_1,m_right_2,m_right_3,m_right_4,m_right_5,m_right_6]]

##global hit_down
link_attack=[[a_up_1,a_up_2,a_up_2,a_up_1,fix_up_1],
             [a_down_1,a_down_2,a_down_2,a_down_1,fix_down_1],
             [a_left_1,a_left_2,a_left_2,a_left_1,fix_left_1],
             [a_right_1,a_right_2,a_right_2,a_right_1,fix_right_1]]

#mouvement monstre
#monstre 1 octobrock
octobrock=[[oc_haut_1,oc_haut_2,oc_haut_1,oc_haut_2,oc_haut_1,oc_haut_2,oc_haut_1,oc_haut_2,oc_haut_1,oc_haut_2,graine1],
           [oc_bas_1,oc_bas_2,oc_bas_1,oc_bas_2,oc_bas_1,oc_bas_2,oc_bas_1,oc_bas_2,oc_bas_1,oc_bas_2,graine1],
           [oc_gauche_1,oc_gauche_2,oc_gauche_1,oc_gauche_2,oc_gauche_1,oc_gauche_2,oc_gauche_1,oc_gauche_2,oc_gauche_1,oc_gauche_2,graine1],
           [oc_droite_1,oc_droite_2,oc_droite_1,oc_droite_2,oc_droite_1,oc_droite_2,oc_droite_1,oc_droite_2,oc_droite_1,oc_droite_2,graine1]]

