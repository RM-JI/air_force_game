# step 1, init the game and load image

# 1.1 - Import library
import pygame

# 1.2 - Initialize the game 
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
keep_going = True

# 1.3 - Load images
player = pygame.image.load("airplane.png")
size = (150,75)
player = pygame.transform.scale(player, size)
background = pygame.image.load("sky_background.jpg")
background = pygame.transform.scale(background, (width, height))
player_speed = 0.5
bullets=[]
bullet = pygame.image.load("bullet.jpg")
bulletPos[0]=bulletPos[0]+1
screen.blit(bullet,bulletPos)
index = 0
# 1.4 - use loep the op to kegame running 
key_up=key_down=key_left=key_right = False
player_pos=[130,100]
while keep_going:
    # 1.5 - clear the screen before drawing it again
    screen.fill(0)
    screen.blit(background,(0,0))
    #1.6 - draw the screen elements
    screen.blit(player, (player_pos))
    #1.7 - update the screen
    pygame.display.flip() # will update the contents of the entire display, and faster than .update()
    # 1.8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type==pygame.QUIT:
            keep_going = False
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                keep_going = False
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_UP:
              key_up=True
            elif event.key==pygame.K_LEFT:
              key_left=True
            elif event.key==pygame.K_DOWN:
              key_down=True
            elif event.key==pygame.K_RIGHT:
              key_right=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_UP:
              key_up=False
            elif event.key==pygame.K_LEFT:
              key_left=False
            elif event.key==pygame.K_DOWN:
              key_down=False
            elif event.key==pygame.K_RIGHT:
              key_right=False
    if (player_pos[1] >= 0):
        if key_up:
            player_pos[1]-=player_speed
    if (player_pos[1] <= height-75):
        if key_down:
            player_pos[1]+=player_speed
    if (player_pos[0] >= 0):
        if key_left:
            player_pos[0]-=player_speed
    if (player_pos[0] <= width-150):
       if key_right:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
            player_pos[0]+=player_speed
    if event.type==pygame.MOUSEBUTTONDOWN or (event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE):
        bullets.append(player_pos[0])
        bullets.append(player_pos[1])
    
    if 
        if bulletPos[0]<-64 or bulletPos[0]>640 or bulletPos[1]<-64 or bulletPos[1]>480:
            bullets.pop(index)  #remove from list
            index =+ 1
#1.9 exit pygame and python
pygame.quit()
exit(0)