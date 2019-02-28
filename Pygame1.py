import pygame
import os
pygame.init()

reso_x=852 #resolution 
reso_y=480

win = pygame.display.set_mode((reso_x,reso_y)) #Window Size
pygame.display.set_caption("My Game") #Window Name

x=100
y=400 #Starting coordinates of object

width=32
height=32 #Dimensions of object

vel=20 #speed of object

bg=pygame.image.load("Game/bg.jpg")
stand=pygame.image.load("Game/standing.png")
left1=pygame.image.load("Game/L1.png")
right1=pygame.image.load("Game/R1.png")

leftMotion=["Game/L1.png","Game/L2.png","Game/L3.png","Game/L4.png","Game/L5.png","Game/L6.png","Game/L7.png","Game/L8.png","Game/L9.png"]
rightMotion=["Game/R1.png","Game/R2.png","Game/R3.png","Game/R4.png","Game/R5.png","Game/R6.png","Game/R7.png","Game/R8.png","Game/R9.png"]
isJump =False #object not jumping initially
jumpCount=10

totLeft=0
totRight=0

def goingLeft(speedMultiplier):
    global x,vel
    if x >vel:
        newspeed=vel*speedMultiplier
        x=(x-newspeed)

def goingRight(speedMultiplier):
    global reso_x,x,width,vel
    if x<reso_x-width-vel:
        newspeed=vel*speedMultiplier
        x=(x+newspeed)        

run=True
while run: #Main Loop
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    moveLeft=False
    moveRight=False
    anime=True
    
    pygame.display.update()
    
######MOVEMENT#####
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
            
##    elif  pygame.key.get_pressed()[pygame.K_LCTRL]: #Slow
##        if pygame.key.get_pressed()[pygame.K_LEFT]:
##            goingLeft(0.125)
##            moveLeft=True
##            moveRight=False
##            totLeft+=1
##        if pygame.key.get_pressed()[pygame.K_RIGHT]:
##            goingRight(0.125)
##            moveRight=True
##            moveLeft=False
##            totRight+=1
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
            
    if not(isJump):
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            isJump =True
            
            
    else:
        if jumpCount >= -10:
            neg=1
            if jumpCount<0:
                neg=-1 
            y-=(jumpCount**2)*0.5*neg
            jumpCount-=1                

        else:
            isJump=False
            jumpCount=10

            
    if moveLeft==True:
        win.blit(bg,(0,0))        
        for i in range(len(leftMotion)):
            if totLeft>=len(leftMotion):
                totLeft=0
            win.blit(pygame.image.load(leftMotion[totLeft]),(x,y))
            
    elif moveRight==True:
        win.blit(bg,(0,0))
        for i in range(len(rightMotion)):
            if totRight>=len(rightMotion):
                totRight=0
            win.blit(pygame.image.load(rightMotion[totRight]),(x,y))
    else:
        win.blit(bg,(0,0))
        win.blit(stand,(x,y))
    if pygame.key.get_pressed()[pygame.K_RSHIFT]: #del later
        print(totLeft)
    
########################
            

pygame.quit()

