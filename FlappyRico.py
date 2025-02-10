#Main
import pygame
from pygame.locals import *
from Variables import*
pygame.init()
pygame.mixer.init()
#Création de la fenetre
pygame.display.set_caption("FloRico")
pygame.display.set_icon(iconpy)
#Importation des éléments
affic(score_digit,Liste_vitesse[indice_vitesse])
choix=randint(0,6)     
#Boucle principale
pygame.key.set_repeat(400, 30)
menu1(souris,window,fullscreen,dico_key,pygame.image.load ("Sprite/Menu_base.png").convert(),pygame.image.load ("Sprite/Button_play.png"))
while run==True:
        if Rico.alive==True:
                
                if Rico.pos.y<32:
                        while Rico.pos.y<=935:
                                Rico.die()
                                affic(score_digit,Liste_vitesse[indice_vitesse])
                if Rico.pos.y>=935:
                        affic(score_digit,Liste_vitesse[indice_vitesse])
                        Rico.alive=False
                        window.blit(Rico.spritedead,(Rico.pos))
                        pygame.display.flip()
                if contact(Rico.pos,Ogpi.p)==True:
                        while Rico.pos.y<=935:
                            Rico.die()
                            affic(score_digit,Liste_vitesse[indice_vitesse])
                if contact(Rico.pos,Ogpi.p2)==True:
                        while Rico.pos.y<=935:
                            Rico.die()
                            affic(score_digit,Liste_vitesse[indice_vitesse])
                if contact(Rico.pos,Opgi.p)==True:
                        while Rico.pos.y<=935:
                            Rico.die()
                            affic(score_digit,Liste_vitesse[indice_vitesse])
                if contact(Rico.pos,Opgi.p2)==True:
                        while Rico.pos.y<=935:
                            Rico.die()
                            affic(score_digit,Liste_vitesse[indice_vitesse])
                if contact(Rico.pos,Ommi.p)==True:
                        while Rico.pos.y<=935:
                            Rico.die()
                            affic(score_digit,Liste_vitesse[indice_vitesse])
                if contact(Rico.pos,Ommi.p2)==True:
                        while Rico.pos.y<=935:
                            Rico.die()
                            affic(score_digit,Liste_vitesse[indice_vitesse])
                if contact(Rico.pos,Ogmi.p)==True:
                        while Rico.pos.y<=935:
                            Rico.die()
                            affic(score_digit,Liste_vitesse[indice_vitesse])
                if contact(Rico.pos,Ogmi.p2)==True:
                        while Rico.pos.y<=935:
                            Rico.die()
                            affic(score_digit,Liste_vitesse[indice_vitesse])
                if contact(Rico.pos,Omgi.p)==True:
                        while Rico.pos.y<=935:
                            Rico.die()
                            affic(score_digit,Liste_vitesse[indice_vitesse])
                if contact(Rico.pos,Omgi.p2)==True:
                        while Rico.pos.y<=935:
                            Rico.die()
                            affic(score_digit,Liste_vitesse[indice_vitesse])
                if score_digit==42 and Rico.sprite==Rico.spritedead:
                        window.blit(pygame.image.load ("Sprite/sus.jpg"),(0,0))
                        draw_text("SUS",500,1920/2,1080/5,None,(255, 130, 0))
                        csvwandr(score_digit)
                        pygame.display.flip()
                        Son.play_son("sus")
                        run=False
                else:
                        Rico.fall()
                        Ogpi.deplacement()
                        Opgi.deplacement()
                        Ommi.deplacement()
                        Ogmi.deplacement()
                        Omgi.deplacement()
                        if score(Rico.pos,Ogpi.p)==True:score_digit+=1
                        if score(Rico.pos,Opgi.p)==True:score_digit+=1
                        if score(Rico.pos,Ommi.p)==True:score_digit+=1
                        if score(Rico.pos,Ogmi.p)==True:score_digit+=1
                        if score(Rico.pos,Omgi.p)==True:score_digit+=1
                        if score_digit%10==0 and score_digit!=0:
                                if Ogpi.speed<28 and changement_speed==False:
                                        indice_vitesse+=1
                                        Ogpi.speed=Liste_vitesse[indice_vitesse]
                                        Opgi.speed=Liste_vitesse[indice_vitesse]
                                        Ommi.speed=Liste_vitesse[indice_vitesse]
                                        Ogmi.speed=Liste_vitesse[indice_vitesse]
                                        Omgi.speed=Liste_vitesse[indice_vitesse]
                                        changement_speed=True
                        else:changement_speed=False
                        if dico_key.get(K_SPACE)==True:
                                Rico.jump()
                        if dico_key.get(K_F11)==fullscreen:
                                window=fullscreen_switch(fullscreen,window)[0]
                                fullscreen=fullscreen=fullscreen_switch(fullscreen,window)[1]
                        affic(score_digit,Liste_vitesse[indice_vitesse])

                for event in pygame.event.get():
                        if event.type == QUIT:
                                run= False
                                print ("Fin de session")
                                pygame.quit()                   #close the window
                        elif event.type==KEYDOWN :
                                if event.key==K_F11:
                                        dico_key[K_F11]=fullscreen                   #resize the window (fullscreen/normal)
                                if event.key==K_SPACE or event.key==K_UP:
                                        dico_key[K_SPACE]=True
                        elif event.type==KEYUP:
                                if event.key==K_SPACE or event.key==K_UP:
                                        dico_key[K_SPACE]=False


        else:
        
                for event in pygame.event.get():
                        if event.type == QUIT:
                                run= False 
                                print ("Fin de session")                                
                                pygame.quit()

                Rico.alive=menu1(souris,window,fullscreen,dico_key,pygame.image.load ("Sprite/Menu_Score.png"),pygame.image.load ("Sprite/Button_retry.png"),score_digit)
                time.sleep(0.2)
                Rico.pos.y,Rico.pos.x=330,185
                indice_vitesse=0
                Ogpi.p.x,Ogpi.p2.x,Ogpi.speed=Ogpi.origin_pos,Ogpi.origin_pos,Liste_vitesse[indice_vitesse]
                Opgi.p.x,Opgi.p2.x,Opgi.speed=Opgi.origin_pos,Opgi.origin_pos,Liste_vitesse[indice_vitesse]
                Ommi.p.x,Ommi.p2.x,Ommi.speed=Ommi.origin_pos,Ommi.origin_pos,Liste_vitesse[indice_vitesse]
                Ogmi.p.x,Ogmi.p2.x,Ogmi.speed=Ogmi.origin_pos,Ogmi.origin_pos,Liste_vitesse[indice_vitesse]
                Omgi.p.x,Omgi.p2.x,Omgi.speed=Omgi.origin_pos,Omgi.origin_pos,Liste_vitesse[indice_vitesse]
                score_digit=0
                dico_key={}
                
time.sleep(8.5)                
pygame.quit()
 
