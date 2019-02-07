import pygame
import os
pygame.init()

win = pygame.display.set_mode((600,600)) #Window Size
pygame.display.set_caption("My Game") #Window Name

x=100
y=500 #Starting coordinates of object
width=32
height=32 #Dimensions of object
vel=20 #speed of object


def leftAnimation(cycle):
    for i in range (cycle):
        leftImages= pygame.image.load(os.path.join("Game/L" + str(i+1) + "E.png")).convert()
        win.blit(leftImages,(x,y))

isJump =False #object not jumping initially
jumpCount=10

def goingLeft(speedMultiplier):
    global x,vel
    if x >vel:
        newspeed=vel*speedMultiplier
        x=(x-newspeed)
        
        
        
def goingRight(speedMultiplier):
    global x,width,vel
    if x<600-width-vel:
        newspeed=vel*speedMultiplier
        x=(x+newspeed)


run=True
while run: #Main Loop
    pygame.time.delay(60) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
######MOVEMENT#####    
    if pygame.key.get_pressed()[pygame.K_LSHIFT]: #Sprint
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            goingLeft(1)
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            goingRight(1)
            
    elif  pygame.key.get_pressed()[pygame.K_LCTRL]: #Slow
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            goingLeft(0.125)
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            goingRight(0.125)
    else:                    
        if pygame.key.get_pressed()[pygame.K_LEFT]: #Walk
            goingLeft(0.5)
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            goingRight(0.5)
            
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
########################
            
        
        
    win.fill((66, 244, 232))
    pygame.display.update()


pygame.quit()


