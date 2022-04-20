from pygame import *
from time import sleep
win_width=800
win_height=500
window=display.set_mode((win_width,win_height))
display.set_caption("PINGPONG")
back = (200, 255, 255)#цвет для фона
FPS=150
clock = time.Clock()

class GameSprite(sprite.Sprite):
	def __init__(self, img,width,height,x,y,speed):
		super().__init__()
		self.width = width
		self.height = height
		self.image = transform.scale( image.load(img) ,(self.width,self.height) )
		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y
		self.speed=speed
	def reset(self):
		window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
	def __init__(self,img,width,height,x,y,speed):
		super().__init__(img,width,height,x,y,speed)
	def update_L(self):
		keys=key.get_pressed()
		#Движение вверх-вних по клавишам K_w и K_s
		if keys[K_w] and self.rect.y>0:
			self.rect.y -= self.speed
		elif keys[K_s] and self.rect.y + self.height<win_height:
			self.rect.y += self.speed
	def update_R(self):
		keys=key.get_pressed()
		if keys[K_UP] and self.rect.y>0:
			self.rect.y -= self.speed
		elif keys[K_DOWN] and self.rect.y + self.height<win_height:
			self.rect.y += self.speed
		#Движение вверх-вних по клавишам K_UP и K_DOWN
		#НЕ ЗАБУДБТЕ ПРО ОГРАНИЧЕНИЯ, ЧТОБЫ РАКЕТКА НЕ ВЫХОДИЛА ЗА ПОЛЕ
		
speed_x = 3
speed_y = 3
pointsL=0
pointsR=0
font.init()
font14=font.SysFont('Arial',14)
textL= font14.render("Очки:"+str(pointsL),True,(255,0,0))
textR= font14.render("Очки:"+str(pointsR),True,(255,0,0))
font20=font.SysFont('Arial',20)
textWinL = font20.render("Победила ЛЕВАЯ ракетка!",True,(255,0,0))
textWinR = font20.render("Победила ПРАВАЯ ракетка!",True,(255,0,0))

ball = GameSprite(img="tenis_ball.png",width=50,height=50,x=200,y=200,speed=1)
racket1 = Player(img="racket.png",width=50,height=150,x=30,y=200,speed=4)
racket2 = Player(img="racket.png",width=50,height=150,x=720,y=200,speed=4)
while True:
	window.fill(back)
	window.blit(textR,(750,30))
	window.blit(textL,(20,30))
	ball.reset()
	racket1.reset()
	racket2.reset()
	racket1.update_L()
	racket2.update_R()
	display.update()
	ball.rect.y+=speed_y
	ball.rect.x+=speed_x
	if sprite.collide_rect(ball,racket1) or sprite.collide_rect(ball,racket2):
		speed_x=-speed_x

	if (ball.rect.y < 0) or ball.rect.y + ball.height> win_height:
		speed_y= -speed_y

	if ball.rect.x < 0:
		ball.rect.x=400
		ball.rect.y=200
		pointsR += 1
		textR= font14.render("Очки"+str(pointsR),True,(255,0,0))

	if ball.rect.x+ball.width > win_width:
		ball.rect.x=400
		ball.rect.y=200
		pointsL +=1
		textL= font14.render("Очки"+str(pointsL),True,(255,0,0))
	if pointsL >= 10:
		window.blit(textWinL, (win_width//2, win_height//2))
		display.update()
		sleep(4)
		quit()
	if pointsR >= 10:
		window.blit(textWinR, (win_width//2, win_height//2))
		display.update()
		sleep(4)
		quit()
	for i in event.get(): 
		if i.type==QUIT:
			quit() 
	clock.tick(FPS)