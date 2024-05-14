import pygame as py
import sys
import random
import GameofLife
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))
py.init()

BLK = (13,13,13)
WHITE = (242,242,242)
GREY = (38,38,38)
BLUE = (2,56,89)
W,H = 1200,1200

screen = py.display.set_mode((W, H))
font = py.font.Font('build/Urbanist-ExtraBold.ttf', 120)

start_img = py.image.load('build/start_button.png').convert_alpha()
exit_img= py.image.load('build/exit_button.png').convert_alpha()
py.display.set_caption('Main Menu')

class Button():
	def __init__(self,x,y,image,scale):
		width = image.get_width()
		height = image.get_height()
		self.image = py.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self):
		action = False
		mouse_pos = py.mouse.get_pos()
		if self.rect.collidepoint(mouse_pos):
			if py.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True
			if py.mouse.get_pressed()[0] == 0 and self.clicked == True:
				self.clicked = False
		screen.blit(self.image, (self.rect.x, self.rect.y))
		return action
	
start_button = Button(900,800,start_img, 1)
exit_button = Button(150,800,exit_img, 1)
text = font.render('''Game''', True, BLUE, BLK)
text2 = font.render('''of Life''', True, BLUE, BLK)
textrect = text.get_rect()
textrect2 = text.get_rect()
textrect.center = (600, 400)
textrect2.center = (600, 600)

def pop():
	run = True
	while run:
		
		screen.fill(BLK)
		screen.blit(text,textrect)
		screen.blit(text2,textrect2)
		if start_button.draw() == True:
			GameofLife.play()
			

		if exit_button.draw() == True:
			run = False

		for event in py.event.get():
			if event.type == py.QUIT:
				run = False
				break

		py.display.update()

	py.quit()
pop()
