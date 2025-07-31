import pygame as pg
import random as r
# from pygame.locals import *
from config import *
from entities import *

class Game:
	def __init__(self):
		pg.init()
		self.window = pg.display.set_mode(WIN_SIZE)
		self.menu_running = True
		self.game_running = False
		self.clock = pg.time.Clock()
		self.bg = pg.transform.scale(pg.image.load(BG).convert(), WIN_SIZE)
		self.font = pg.font.SysFont('Comic Sans MS', 50)
		self.button_main = None
		self.buttons = pg.sprite.Group()
		self.lmb = False

	def menu_run(self):
		while self.menu_running:
			self.menu_events()
			self.menu_update()
			self.menu_render()

	def menu_events(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				self.menu_running = False
			if event.type == pg.KEYUP:
				if event.key == pg.K_ESCAPE:
					self.menu_running = False
				if event.key == pg.K_p:
					self.game_running = True
					self.game_run()

	def menu_update(self):
		self.clock.tick(FPS)

	def menu_render(self):
		pg.display.set_caption('Меню')
		self.window.blit(self.bg, (0, 0))
		text = self.font.render('Нажмите P, чтобы начать', True, BLUE)
		self.window.blit(text, (100, 100))	
		pg.display.update()

	def game_run(self):
		for name in NAMES:
			self.buttons.add(Button_Active(name))
		for name in NAMES:
			self.buttons.add(Button_Passive(name))
		self.button_main = Button_Main()
		self.buttons.add(Info())
		while self.game_running:
			self.game_events()
			self.game_update()
			self.game_render()
		self.buttons.empty()
		self.button_main = None

	def game_events(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				self.game_running = False
			if event.type == pg.KEYUP:
				if event.key == pg.K_ESCAPE:
					self.game_running = False
			if event.type == pg.MOUSEBUTTONUP and event.button == 1:
				self.lmb = True

	def game_update(self):
		ms = self.clock.tick(FPS)
		coins, power, passive = self.button_main.info()
		for button in self.buttons:
			coins, power, passive = button.update(self.lmb, coins, power, passive, ms)

		self.button_main.update(self.lmb, coins, power, passive, ms)
		self.lmb = False

	def game_render(self):
		pg.display.set_caption('Игра')
		self.window.blit(self.bg, (0, 0))
		self.buttons.draw(self.window)
		self.window.blit(self.button_main.image, self.button_main.rect.topleft)
		self.belkas.draw(self.window)
		pg.display.update()

game_1 = Game()
game_1.menu_run()