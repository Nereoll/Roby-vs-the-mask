#Variables classes fonctions jeu
from random import*
import time
import pygame
from pygame.locals import *
#init pygame
pygame.init()
#Variables
#utilitaire
changement_speed=False
run=True
fullscreen=False
dico_key={}
clock = pygame.time.Clock()
souris=1
score_digit=0
indice_vitesse=0
Liste_vitesse=[15,17,20,23,28]
liste_position=[2000,3500,5000,6500,8000]
shuffle(liste_position)
distance1,distance2,distance3,distance4,distance5=liste_position[0],liste_position[1],liste_position[2],liste_position[3],liste_position[4]
#fenetre+icone---------------------------------------------------
monitor=[pygame.display.Info().current_w,pygame.display.Info().current_h]
window = pygame.display.set_mode((1920,1020), SCALED)
iconpy = pygame.image.load ("Sprite/Rico.png")
curseur = pygame.image.load ("Sprite/Rico.png")
#menu1-----------------------------------------------------------
def menu1(souris,window,fullscreen,dico_key,background=pygame.image.load ("Sprite/Menu_base.png"),button=None,score_digit=None):
    score=score_digit
    max_score=csvwandr(score_digit)
    CURSEURY = 0
    CURSEURX = 0
    while souris:
        if dico_key.get(K_F11)==fullscreen:
            window=fullscreen_switch(fullscreen,window)[0]
            fullscreen=fullscreen_switch(fullscreen,window)[1]
            
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type==KEYDOWN:
                if event.key==K_F11:
                    dico_key[K_F11]=fullscreen
            if event.type == MOUSEMOTION:
                CURSEURX = event.pos[0]
                CURSEURY = event.pos[1]
                
            if event.type==MOUSEBUTTONDOWN:
                CURSEURX=event.pos[0]
                CURSEURY=event.pos[1]
                if CURSEURX>=750 and CURSEURX<=1162 and CURSEURY>=500 and CURSEURY<=647 :
                    souris=0
                    window.blit( pygame.image.load ("Sprite/background2.png").convert(), (0, 0))
                    Son.play_son("click")

        window.blit(background,(0,0))
        window.blit(button,(760,500))
        if score!=None:
            draw_text(str(score),60,960,134,None,(0, 0, 0))
            draw_text(str(max_score),60,1200,240,None,(0, 0, 0))
        
        window.blit(curseur, (CURSEURX, CURSEURY))
        pygame.display.flip()
            

    return(not Rico.alive)
#csv----------------------------------------------------------------
def csvwandr(score_digit):
    if score_digit==None:score_digit=0
    highest_score=0
    with open('scores.csv', "a", newline='') as csvfile:
        csvfile.write(str(score_digit)+"\n")
    with open('scores.csv', "r", newline='') as csvfile:
        for nmber in csvfile:
            if int(nmber)>int(highest_score):
                highest_score=nmber
    return(int(highest_score))
                

#affichage----------------------------------------------------------
background = pygame.image.load ("Sprite/background2.png").convert()

speed_button=pygame.image.load("Sprite/Button_speed.png").convert()
speed_button_rect=speed_button.get_rect()
def affic(score_digit,vitesse):
    return(clock.tick(60),
            window.blit(background, (0,0)),
            window.blit(Rico.sprite,(Rico.pos)),
            window.blit(Ogpi.img,(Ogpi.p)),
            window.blit(Ogpi.img2,(Ogpi.p2)),
            window.blit(Opgi.img,(Opgi.p)),
            window.blit(Opgi.img2,(Opgi.p2)),
            window.blit(Ommi.img,(Ommi.p)),
            window.blit(Ommi.img2,(Ommi.p2)),
            window.blit(Ogmi.img,(Ogmi.p)),
            window.blit(Ogmi.img2,(Ogmi.p2)),
            window.blit(Omgi.img,(Omgi.p)),
            window.blit(Omgi.img2,(Omgi.p2)),
            window.blit(Border.sprite, (0,0)),
            window.blit(speed_button,(1683,0)),
            draw_text("Vitesse :"+str(vitesse),30,1800,22,None,(112, 238, 156)),
            pygame.draw.rect(background,(2,54,24), ((1920/2)-100, 1080/3, 200, 150,)),
            draw_text(str(score_digit),100,1920/2,1080/3,background),
            pygame.display.flip())
#contact-------------------------------------------------------
def contact(rectA,rectB):
    if rectB.right < rectA.left:return(False)
    if rectB.bottom < rectA.top:return(False)
    if rectB.left > rectA.right:return(False)
    if rectB.top > rectA.bottom:return(False)
    else:return(True)
#draw_text-----------------------------------------------------
font_n=pygame.font.match_font('arial_black')
def draw_text(text,size,x,y,surf=None,color=(255,255,255)):
    font=pygame.font.Font(font_n,size)
    txt_surf=font.render(text,True,color)
    txt_rect=txt_surf.get_rect()
    txt_rect.midtop=(x,y)
    if surf==None:
        window.blit(txt_surf,txt_rect)
    else:
        surf.blit(txt_surf,txt_rect)
#score---------------------------------------------------------
def score(rectA,rectB):#rectA= main character rectB=Obstacles
    if rectB.right>170 and rectB.right<190:return(True)
#fullscreen_switch---------------------------------------------
def fullscreen_switch(fullscreen,window):
    if fullscreen==False:
        window=pygame.display.set_mode(monitor, FULLSCREEN|SCALED)        #fullscreen
        fullscreen=True
        return(window,fullscreen)
    else:
        window = pygame.display.set_mode((1920,1020),SCALED)#not fullscreen
        fullscreen=False
        return(window,fullscreen)
#Obstacle_g_pi-------------------------------------------------
class Obstacle_g_pi(pygame.sprite.Sprite):
    def __init__(self,distance=2000):
        super().__init__()
        self.origin_pos=distance
        self.distance=distance
        self.img=pygame.image.load("Sprite/obstacle2.png").convert()
        self.p=self.img.get_rect()
        self.p.y=612
        
        self.img2=pygame.image.load("Sprite/obstacle0r.png").convert()
        self.p2=self.img2.get_rect()
        self.p2.y=32

        self.p.x,self.p2.x=self.distance,self.distance
        self.speed=Liste_vitesse[indice_vitesse]
    def deplacement(self):
        self.p.x-=self.speed
        self.p2.x-=self.speed
        if self.p.x<-50:
            self.p.x,self.p2.x=8000,8000
#Obstacle_p_gi--------------------------------------------------
class Obstacle_p_gi(pygame.sprite.Sprite):
    def __init__(self,distance):
        super().__init__()
        self.origin_pos=distance
        self.distance=distance
        self.img=pygame.image.load("Sprite/obstacle0.png").convert()
        self.p=self.img.get_rect()
        self.p.y=754

        
        self.img2=pygame.image.load("Sprite/obstacle2r.png").convert()
        self.p2=self.img2.get_rect()       
        self.p2.y=32

        
        self.p.x,self.p2.x=self.distance,self.distance
        self.speed=Liste_vitesse[indice_vitesse]
    def deplacement(self):
        self.p.x-=self.speed
        self.p2.x-=self.speed
        if self.p.x<-50:
            self.p.x,self.p2.x=8000,8000
#Obstacle_m_mi---------------------------------------------------
class Obstacle_m_mi(pygame.sprite.Sprite):
    def __init__(self,distance):
        super().__init__()
        self.origin_pos=distance
        self.distance=distance
        self.img=pygame.image.load("Sprite/obstacle1.png").convert()
        self.p=self.img.get_rect()
        self.p.y=697

        self.img2=pygame.image.load("Sprite/obstacle1r.png").convert()
        self.p2=self.img2.get_rect()
        self.p2.y=32

        self.p.x,self.p2.x=self.distance,self.distance
        self.speed=Liste_vitesse[indice_vitesse]
    def deplacement(self):
        self.p.x-=self.speed
        self.p2.x-=self.speed
        if self.p.x<-50:
            self.p.x,self.p2.x=8000,8000
#Obstacle_g_mi----------------------------------------------------
class Obstacle_g_mi(pygame.sprite.Sprite):
    def __init__(self,distance):
        super().__init__()
        self.origin_pos=distance
        self.distance=distance
        self.img=pygame.image.load("Sprite/obstacle2.png").convert()
        self.p=self.img.get_rect()
        self.p.y=612


        self.img2=pygame.image.load("Sprite/obstacle1r.png").convert()
        self.p2=self.img2.get_rect()
        self.p2.y=32

        
        self.p.x,self.p2.x=self.distance,self.distance
        self.speed=Liste_vitesse[indice_vitesse]
    def deplacement(self):
        self.p.x-=self.speed
        self.p2.x-=self.speed
        if self.p.x<-50:
            self.p.x,self.p2.x=8000,8000
#Obstacle_m_gi-----------------------------------------------------
class Obstacle_m_gi(pygame.sprite.Sprite):
    def __init__(self,distance):
        super().__init__()
        self.origin_pos=distance
        self.distance=distance
        self.img=pygame.image.load("Sprite/obstacle1.png").convert()
        self.p=self.img.get_rect()
        self.p.y=697

        
        self.img2=pygame.image.load("Sprite/obstacle2r.png").convert()
        self.p2=self.img2.get_rect()       
        self.p2.y=32

        
        self.p.x,self.p2.x=self.distance,self.distance
        self.speed=15
    def deplacement(self):
        self.p.x-=self.speed
        self.p2.x-=self.speed
        if self.p.x<-50:
            self.p.x,self.p2.x=8000,8000
#border-----------------------------------------------------
class Border(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprite=pygame.image.load("Sprite/border2.png").convert_alpha()      
#personnage--------------------------------------------------
class Rico(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprite = pygame.image.load ("Sprite/Rico.png").convert_alpha()
        self.spritedead=pygame.image.load ("Sprite/Ricodead.png").convert_alpha()
        self.pos = self.sprite.get_rect()
        self.alive=True
        self.speed=4
        self.pos.y=330
        self.pos.x=185
    def jump(self):
        self.pos.y-=self.speed*3
        self.sprite=pygame.image.load ("Sprite/Ricojump.png").convert_alpha()
    def fall(self):
        self.pos.y+=self.speed
        self.sprite=pygame.image.load ("Sprite/Rico.png").convert_alpha()
    def die(self):
        self.sprite=self.spritedead
        self.pos.y+=self.speed*4
        Rico.alive=False
#sound------------------------------------------------------
class Son():
    def __init__(self):
        self.all_son={"sus":pygame.mixer.Sound('Sound/AMOGUS.mp3'),
                      "click":pygame.mixer.Sound("Sound/Click.mp3")
                      }
        self.volume=pygame.mixer.music.set_volume(0.2)
    def play_son(self,name):
        self.all_son[name].play()
#-----------------------------------------------------------
Border=Border()
Rico=Rico()
Ogpi=Obstacle_g_pi(distance1)
Opgi=Obstacle_p_gi(distance2)
Ommi=Obstacle_m_mi(distance3)
Ogmi=Obstacle_g_mi(distance4)
Omgi=Obstacle_m_gi(distance5)
Son=Son()
