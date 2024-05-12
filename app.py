import sys, time, pygame
from models.racket import Racket
from models.ball import Ball
pygame.init()

size = width, height = 630, 440
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

racket1 = Racket(color="", speed= 2.5, position_x= 30, key_up='z', key_down='s')
racket2 = Racket(color="", speed= 2.5, position_x= width - 30,key_up= 'p', key_down='m')

ball = Ball(speed=2, size=20,width=width, height=height)


while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	ball.move()
	ball.touch_border(width=width, height=height)
	ball.touch_racket(racket1, racket2)

	
		
	racket1.racket_move(screen_heigth=height)
	racket2.racket_move(screen_heigth=height)

			

	screen.fill(black)
	screen.blit(ball.surface, ball.rect)
	screen.blit(racket1.get_surface(), racket1.get_rect())
	screen.blit(racket2.get_surface(), racket2.get_rect())
	time.sleep(0.01)
	pygame.display.flip()