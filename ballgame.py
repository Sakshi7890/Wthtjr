# Importing the liberary
import pygame
# Initializing the pygame library
pygame.init()

# Creating the drawing window
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Bouncing Ball")
# setting the initial postion
x=240
y=0
# defining the variables for color scheme
red = (255,0,0)
blue = (0,0,255)
black= (0, 0, 0)
white=(255,255,255)
# variable to change the direction of ball
Dir_ch=0
color= red # initial color of ball
# Run until the user asks to quit
running = True
clock= pygame.time.Clock()
while running:
    #pygame.time.delay(10)
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
           # Fill the background with white
        screen.fill((255, 255, 255))
        if Dir_ch % 2 == 0: 
            while  y <= 350:
                
                y = y+5
                screen.fill(white)
                pygame.draw.circle(screen, (0, 0, 255), (x, y), 40)
                #clock.tick(3)
                #pygame.time.delay(10)
        else:
            while y >= 30:
                
                y= y-5
                screen.fill(white)
                pygame.draw.circle(screen, (0, 0, 255), (x, y), 40) 
                #clock.tick(3)
        pygame.time.delay(10)
        pygame.display.update()
    Dir_ch+=1      
#clock.tick(3)
    
pygame.quit()
