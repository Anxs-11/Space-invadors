import pygame
import random
import math
from pygame import mixer # helps to manage musics

pygame.init()

screen=pygame.display.set_mode((800,600))  #(width,height)

#player
p=pygame.image.load("/Users/mohdanas/Desktop/🐍 projects/space Invadors game/Player.png")
px=370
py=480
pxchange=0
def player(x,y):
    screen.blit(p,(x,y)) #blit means to draw

#enemy
e=[]
ex=[]
ey=[]
exchange=[]
eychange=[]
n_enemies=6
for i in range(n_enemies):
    e.append(pygame.image.load("/Users/mohdanas/Desktop/🐍 projects/space Invadors game/enemy.png"))
    ex.append(random.randint(0,735))
    ey.append(random.randint(50,150))
    exchange.append(0.3)
    eychange.append(40)
    
def enemy(x,y,i):
    screen.blit(e[i],(x,y))

#bullet
bu=pygame.image.load("/Users/mohdanas/Desktop/🐍 projects/space Invadors game/bullet.png")
bx=0
by=480
bxchange=0
bychange=1
bstate="ready" #ready state when bullet cant be seen on screen 
                #bstate=fire . when bullet is fired
def fire_bullet(x,y):
    global bstate
    bstate="fire"
    screen.blit(bu,(x+16,y+10)) #x+16,y+10 extra isilye add kiye h bcz thora left and down se fire ni hogi bullet
    
#collision detection
def col(ex,ey,bx,by):
    dis=math.sqrt(math.pow(ex-bx,2) + math.pow(ey-by,2))
    if dis<27:
        return True
    else:
        return False
    

score=0 #score
font=pygame.font.Font('freesansbold.ttf',32)
tx=10
ty=10
def show_score(x,y):
    sc=font.render("Score : "+str(score),True,(255,255,255))
    screen.blit(sc,(x,y))


#game over
over_font=pygame.font.Font('freesansbold.ttf',50)
def game_over():
    overt=over_font.render("GAME OVER ! ",True,(255,255,255))
    screen.blit(overt,(200,250))
    
#background image
bg=pygame.image.load("/Users/mohdanas/Desktop/🐍 projects/space Invadors game/space.jpg")

#background music
mixer.music.load("/Users/mohdanas/Desktop/🐍 projects/space Invadors game/bgmusic.mp3")
mixer.music.play(-1)#-1 means repeat music 

# is line ke badd programm end ho jata to to isiliyw window ni rukti. h bcz prgrm is executed
# to make window on always\
#but jese hi while loop use krre h programm humesha excuting condition me rahega or window
# on rahega

s=True
while (s):
    screen.fill((0,0,0)) #changing color of screen
    screen.blit(bg,(-200,-400)) #background image drawing here
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            s=False
            
            
        #if keystroke is passed check whether its right or left 
        if i.type==pygame.KEYDOWN : #this means some left or right kerstroke is pressed
            if i.key==pygame.K_LEFT:
                pxchange=-0.7
            if i.key==pygame.K_RIGHT:
                pxchange=0.7
            if i.key==pygame.K_SPACE:
                if bstate=="ready":
                    b_sound=mixer.Sound("/Users/mohdanas/Desktop/🐍 projects/space Invadors game/shot.mp3")
                    b_sound.play()
                    bx=px #gets cooradinate of player when bullet is fired
                    fire_bullet(bx,by)
        if i.type==pygame.KEYUP : #this means some left or right kerstroke is unreleased
            if i.key==pygame.K_LEFT or i.key==pygame.K_RIGHT:
                pxchange=0
        
   #checking for player boundaries 
    px+=pxchange
    if px<=0:
        px=0
    elif px>=736:   #(800-image length)
        px=736
    
    #checking for enemy boundaries
    for i in range(n_enemies):
        if ey[i]>470:
            for j in range(n_enemies):
                ey[i]=2000
            game_over()
           
            break
    
        ex[i]+=exchange[i]
        if ex[i]<=0:
            exchange[i]=0.3
            ey[i]+=eychange[i]
        elif ex[i]>=736:   #(800-image length)
            exchange[i]=-0.3
            ey[i]+=eychange[i]
        #collsion
        collision=col(ex[i],ey[i],bx,by)
        if collision:
            c_sound=mixer.Sound("/Users/mohdanas/Desktop/🐍 projects/space Invadors game/explosion.mp3")
            c_sound.play()
            by=480
            bstate="ready"
            score+=1
            ex[i]=random.randint(0,735)
            ey[i]=random.randint(50,150)
            
        enemy(ex[i],ey[i],i)
    
    #bullet movement
    if by<=0:
        by=480
        bstate="ready"
    if bstate=="fire":
        fire_bullet(bx,by)
        by-=bychange
        
    


       
    
    
    player(px,py) #should call after screen.fill otherwise color will overwrite 
    show_score(tx,ty)
    pygame.display.update() #to update screen each time program runs
    

    