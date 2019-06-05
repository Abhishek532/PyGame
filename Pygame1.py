import pygame
pygame.init()

reso_x=852 #resolution 
reso_y=480

win = pygame.display.set_mode((reso_x,reso_y)) #Window Size
pygame.display.set_caption("My Game") #Window Name

x=100
y=200 #Starting coordinates of object

width=64
height=64 #Dimensions of object

hori_vel=20 #vel of object
ver_vel=0

bg=pygame.image.load("Game/bg.jpg")
stand=pygame.image.load("Game/standing.png")
#*All images are 64x64*
leftMotion=["Game/L1.png","Game/L2.png","Game/L3.png","Game/L4.png","Game/L5.png","Game/L6.png","Game/L7.png","Game/L8.png","Game/L9.png"]
rightMotion=["Game/R1.png","Game/R2.png","Game/R3.png","Game/R4.png","Game/R5.png","Game/R6.png","Game/R7.png","Game/R8.png","Game/R9.png"]
isJump =False #object not jumping initially
jumpCount=10

totLeft=0
totRight=0


def road():
    pygame.draw.rect(win,(45,45,45),(0,425,852,45))
    j=10 
    for i in range(20):
        pygame.draw.rect(win,(255,255,255),(j,445,40,7))
        j+=100
    pygame.draw.rect(win,(0,0,255),(325,447,20,20))
    pygame.draw.rect(win,(255,0,0),(675,447,20,20))
        
def goingLeft(speedMultiplier):
    global x,hori_vel
    if x >hori_vel:
        newspeed=hori_vel*speedMultiplier
        x=(x-newspeed)

def goingRight(speedMultiplier):
    global reso_x,x,width,hori_vel
    if x<reso_x-width-hori_vel:
        newspeed=hori_vel*speedMultiplier
        x=(x+newspeed)



run=True
while run: #Main Loop
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
            
    moveLeft=False
    moveRight=False
    
    pygame.display.update()

    if x>=295 and x<=315 and pygame.key.get_pressed()[pygame.K_f]: #Portal
        isJump=False
        x=680
        y=400
    if x>=640 and x<=675 and pygame.key.get_pressed()[pygame.K_f]:
        isJump=False
        x=325
        y=400

    if y<reso_y-height-ver_vel and not(isJump):
        moveDown=True
        moveUp=False
        ver_vel+=4
        y+=ver_vel
        if y>=410:
            ver_vel=0
    
###########MOVEMENT##########
            
    if pygame.key.get_pressed()[pygame.K_e]: #Press E to exit
        run=False
    if pygame.key.get_pressed()[pygame.K_r]: #Press R to reset position-buggy with jump
        x=y=100   
        
    if pygame.key.get_pressed()[pygame.K_LSHIFT]: #Sprint
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            goingLeft(0.375)
            moveLeft=True
            moveRight=False
            totLeft+=1
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            goingRight(0.375)
            moveRight=True
            moveLeft=False
            totRight+=1
    elif pygame.key.get_pressed()[pygame.K_RSHIFT]: #Superfast-For debugging-delete later
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            goingLeft(1)
            moveLeft=True
            moveRight=False
            totLeft+=1
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            goingRight(1)
            moveRight=True
            moveLeft=False
            totRight+=1
    else:                    
        if pygame.key.get_pressed()[pygame.K_LEFT]: #Walk
            goingLeft(0.125)
            moveLeft=True
            moveRight=False
            totLeft+=1
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            goingRight(0.125)
            moveRight=True
            moveLeft=False
            totRight+=1
##Jumpcode##

    if not(isJump):
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            isJump =True
    else:
        if jumpCount >= -10:
            neg=1
            if jumpCount<0:
                neg=-1 
            y-=(jumpCount**2)*0.50*neg
            jumpCount-=1                
        else:
            isJump=False
            jumpCount=10
############
    if moveLeft==True:
        win.blit(bg,(0,0))
        road()
        for i in range(len(leftMotion)):
            if totLeft>=len(leftMotion):
                totLeft=0
            win.blit(pygame.image.load(leftMotion[totLeft]),(x,y))
            
    elif moveRight==True:
        win.blit(bg,(0,0)) 
        road()
        for i in range(len(rightMotion)):
            if totRight>=len(rightMotion):
                totRight=0
            win.blit(pygame.image.load(rightMotion[totRight]),(x,y))
    else:
        win.blit(bg,(0,0))
        road()
        win.blit(stand,(x,y))    
########################


        
            

pygame.quit()

