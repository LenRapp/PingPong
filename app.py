import sys, time, pygame
from models.racket import Racket
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()
racket1 = Racket(color="", speed= 2.5, position_x= 30, key_up='z', key_down='s')
racket2 = Racket(color="", speed= 2.5, position_x= width - 30,key_up= 'p', key_down='m')



while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	ballrect = ballrect.move(speed)
	if ballrect.left < 0 or ballrect.right > width:
		speed[0] = -speed[0]
	if ballrect.top < 0 or ballrect.bottom > height:
		speed[1] = -speed[1]
		
	racket1.racket_move()
	racket2.racket_move()

			

	screen.fill(black)
	# screen.blit(ball, ballrect)
	screen.blit(racket1.get_surface(), racket1.get_rect())
	screen.blit(racket2.get_surface(), racket2.get_rect())
	time.sleep(0.01)
	pygame.display.flip()