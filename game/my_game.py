#i copied a lot of the code from the example file, to make sure the program runs.

import pygame
import random 

pygame.init()

screen_width = 1040
screen_height = 680 
screen = pygame.display.set_mode((screen_width,screen_height))

player = pygame.image.load("player.jpg")
prize = pygame.image.load("prize.jpg")
enemy1 = pygame.image.load("monster.jpg")
enemy2 = pygame.image.load("monster.jpg")
enemy3 = pygame.image.load("monster.jpg")

# a player, prize and three enemies are created and all necessary modules are called. pygame is also initialized

player = pygame.transform.scale(player, (75,75))
prize = pygame.transform.scale(prize, (75,75))
enemy1 = pygame.transform.scale(enemy1, (100,150))
enemy2 = pygame.transform.scale(enemy2, (100,150))
enemy3 = pygame.transform.scale(enemy3, (100,150))
#the images are resized as they are too large. i used the following page to help me to resize the images:
#https://stackoverflow.com/questions/43046376/how-to-change-an-image-size-in-pygame


image_height = player.get_height()
image_width = player.get_width()

enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()

enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()

enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()

prize_height = prize.get_height()
prize_width = prize.get_width()

#all the objects' sizes are obtained in order to create the boxes later on in the program

playerXPosition = 100
playerYPosition = 50
#the player object starts at a set place on the screen

enemy1XPosition =  screen_width
enemy1YPosition =  random.randint(0, screen_height - enemy1_height)
if enemy1YPosition < 0 :
    enemy1YPosition  = enemy1YPosition + 300
elif enemy1YPosition > 680 :
    enemy1YPosition = enemy1YPosition - 300

enemy2XPosition =  screen_width
enemy2YPosition =  enemy1YPosition + 150

if enemy2YPosition < 0:
    enemy2YPosition =  enemy1YPosition + 300
elif enemy2YPosition > 680:
    enemy2YPosition =  enemy1YPosition - 300
    
enemy3XPosition =  screen_width
enemy3YPosition =  enemy2YPosition + 150
if enemy3YPosition < 0:
    enemy3YPosition =  enemy2YPosition + 300
elif enemy3YPosition > 680:
    enemy3YPosition =  enemy2YPosition - 300
#the enemy positions are random. i tried to get the enemies to not overlap eachother and also tried to get the enemies to
#not appear below the screen

prizeXPosition = screen_width + 250
prizeYPosition = random.randint(0, screen_height - prize_height)
#the prize Y position is random and the X position is behind the enemies

keyUp= False
keyDown = False
keyLeft = False
keyRight = False

while 1: 

    screen.fill(0) 
    screen.blit(player, (playerXPosition, playerYPosition))
    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    
    screen.blit(prize, (prizeXPosition, prizeYPosition))
    #the above code initializes the screen and places the objects on the screen
    
    pygame.display.flip() 
    #the above code updates the screen
    
    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        #the above code checks if the user quits the game
        
        
        if event.type == pygame.KEYDOWN:
        #the above code checks if the user presses a key
            
            if event.key == pygame.K_UP:  
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
            #the above code checks which key is pressed
        
        
        
        if event.type == pygame.KEYUP:
        #the above code checks if the user stops pressing a key
                      
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
            #the above code checks which key the user stops pressing
            
    if keyUp == True:
        if playerYPosition > 0 : 
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - image_height:
            playerYPosition += 1
            
    if keyLeft == True:
        if playerXPosition > 0 : 
            playerXPosition -= 1
    if keyRight == True:
        if playerXPosition < screen_width - image_width:
            playerXPosition += 1
    #the above code moves the player object according to which key is pressed, it also makes sure the player object does not go beyond
    #the parameters of the screen
    
    playerBox = pygame.Rect(player.get_rect())
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    enemyBox1 = pygame.Rect(enemy1.get_rect())
    enemyBox1.top = enemy1YPosition
    enemyBox1.left = enemy1XPosition
    
    enemyBox2 = pygame.Rect(enemy2.get_rect())
    enemyBox2.top = enemy2YPosition
    enemyBox2.left = enemy2XPosition
    
    enemyBox3 = pygame.Rect(enemy3.get_rect())
    enemyBox3.top = enemy3YPosition
    enemyBox3.left = enemy3XPosition
    
    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition
    #the above code creates a box for each of the objects, which will be used to detect if they collide in the code below
    
    if playerBox.colliderect(enemyBox1) or playerBox.colliderect(enemyBox2) or playerBox.colliderect(enemyBox3):
        print("Game Over!")
        pygame.quit()
        exit(0)
    #the above code checks if the player collides with one of the enemies, if it does the user loses the game so the game quits and 
    #an appropriate message is displayed  
    
    if playerBox.colliderect(prizeBox):
        print("You win!")
        pygame.quit()
        exit(0)
    #the above code checks if the player collides with the prize, if it does the user wins the game so the game quits and an appropriate message is displayed
    
    if (enemy1XPosition < 0 - enemy1_width) and (enemy2XPosition < 0 - enemy2_width) and (enemy3XPosition < 0 - enemy3_width) :
        print("Game Over!")
        pygame.quit()
        exit(0)
    #the above code checks if all the enemies touches the left side of the screen, if it does the user loses the game so the game quits and 
    #an appropriate message is displayed
    
    enemy1XPosition -= 0.30
    enemy2XPosition -= 0.30
    enemy3XPosition -= 0.30
    prizeXPosition -= 0.30