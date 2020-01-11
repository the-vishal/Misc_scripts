import pygame
import sys
import random
import time

check_errors = pygame.init()

if check_errors[1]>0:
    print(f"( ! ) Had {check_errors[1]} initialization errors")
    sys.exit(-1)#error code -1(conventionally)

else:
    print(f"( + ) PyGame Successfully initialized !")

playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption("Snake Game")

#colors
red = pygame.Color(255,0,0) #game over
green = pygame.Color(0,255,0) #snake
black = pygame.Color(0,0,0) #score
white = pygame.Color(255,255,255) #background
brown = pygame.Color(162,42,42) #food

fpsController = pygame.time.Clock() #ref time

snakePos = [200,50]
snakeBody = [[200,50],[190,50],[180,50]]   #starting body 3 blocks
speed = 12
score = 0

#placing food
foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
foodSpawn = True #if food exists

direction = 'RIGHT'
changeto = direction

#Game over Function
def gameOver():
	myFont = pygame.font.SysFont('consolas', 60)
	GOsurface = myFont.render('Game Over !!', True, red) #text, anti-aliasing, color, bgrnd
	GOrect = GOsurface.get_rect()
	GOrect.midtop =(360,15)
	playSurface.blit(GOsurface, GOrect)
	get_score(scene=0)
	pygame.display.update()
	time.sleep(2)
	pygame.quit()
	sys.exit()

def get_score(scene=1):
	sfont = pygame.font.SysFont('consolas', 30)
	sSurface = sfont.render(f"Score : {score}", True, black)
	srect = sSurface.get_rect()
	srect.midtop =[(360,100),(600,20)][scene==1]
	playSurface.blit(sSurface, srect)


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
		    pygame.quit()
		    sys.exit()
		    
		elif event.type == pygame.KEYDOWN:
		    if event.key == pygame.K_RIGHT or  event.key == ord('d'):
		        changeto = 'RIGHT'
		        
		    if event.key == pygame.K_LEFT or  event.key == ord('a'):
		        changeto = 'LEFT'
		        
		    if event.key == pygame.K_UP or  event.key == ord('w'):
		        changeto = 'UP'
		        
		    if event.key == pygame.K_DOWN or  event.key == ord('s'):
		        changeto = 'DOWN'

		    if event.key == pygame.K_ESCAPE:
		        pygame.event.post(pygame.event.Event(pygame.QUIT))
		        
		#validating opposite moves
	if changeto == 'RIGHT' and not direction == 'LEFT':
	    direction = 'RIGHT'
	if changeto == 'LEFT' and not direction == 'RIGHT':
	    direction = 'LEFT'
	if changeto == 'UP' and not direction == 'DOWN':
	    direction = 'UP'
	if changeto == 'DOWN' and not direction == 'UP':
	    direction = 'DOWN'
	    
	#making moves
	if direction == 'RIGHT':
	    snakePos[0]+=10
	if direction == 'LEFT':
	    snakePos[0]-=10
	if direction == 'UP':
	    snakePos[1]-=10
	if direction == 'DOWN':
	    snakePos[1]+=10
	        
	#snakeBody mechanism
	snakeBody.insert(0,list(snakePos)) #moving snake

	if snakePos[0]==foodPos[0] and snakePos[1]==foodPos[1]:
	    foodSpawn =False
	    speed +=1
	    score +=10

	else:
	    snakeBody.pop()

	if not foodSpawn:
	    foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]

	foodSpawn = True

	playSurface.fill(white)

	for pos in snakeBody:
	    pygame.draw.rect(playSurface, green, pygame.Rect(pos[0],pos[1],10,10))

	pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0],foodPos[1],10,10))

	if snakePos[0]<=0 or snakePos[0]>=720 or snakePos[1]>=460 or snakePos[1]<=0:
		gameOver()

	for pos in snakeBody:
	    pygame.draw.rect(playSurface, green, pygame.Rect(pos[0],pos[1],10,10))

	pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0],foodPos[1],10,10))
	get_score()
	if snakePos[0]<=0 or snakePos[0]>=720 or snakePos[1]>=460 or snakePos[1]<=0:
		gameOver()

	for block in snakeBody[1:]:
		if snakePos[0]==block[0] and snakePos[1]==block[1]:
			gameOver() 

	pygame.display.update()
	fpsController.tick(speed)