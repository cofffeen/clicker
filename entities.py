import pygame as pg
from config import *
import random as r

class Button_Main(pg.sprite.Sprite):
	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.transform.scale(pg.image.load(B1).convert_alpha(), BUTTON_SIZE)
		self.pic = self.image.copy()
		self.rect = self.image.get_rect()
		self.rect.topleft = (300, 0)
		self.coins = 0
		self.power = 1
		self.passive = 0
		self.time = 0
		self.font = pg.font.SysFont('Comic Sans MS', 20)

	def update(self, lmb, coins, power, passive, ms):
		self.time += ms
		self.passive = passive
		self.coins = coins
		self.power = power
		if self.time >= 1000:
			self.coins += self.passive
			self.time -= 1000
		if lmb:
			x, y = pg.mouse.get_pos()
			if self.rect.left <= x <= self.rect.right and self.rect.top <= y <= self.rect.bottom:
				self.on_pressed()

		self.image = self.pic.convert_alpha()

		text = self.font.render('Главная кнопка', True, RED)
		x, y = self.rect.size
		w, h = text.get_size()
		self.image.blit(text, ((x - w) // 2, y // 2 - h))

	def on_pressed(self):
		self.coins += self.power

	def info(self):
		return self.coins, self.power, self.passive


class Button_Active(pg.sprite.Sprite):
	def __init__(self, name):
		pg.sprite.Sprite.__init__(self)
		self.level = 0
		self.font = pg.font.SysFont('Comic Sans MS', 20)
		self.font_2 = pg.font.SysFont('Comic Sans MS', 20)
		
		if name  == 'base':
			self.image = pg.transform.scale(pg.image.load(B2).convert_alpha(), BUTTON_SIZE)
			self.pic = self.image.copy()
			self.rect = self.image.get_rect()
			self.rect.topleft = (0, 0)
			self.price = 10
			self.bonus = 1
		elif name == 'ultra':
			self.image = pg.transform.scale(pg.image.load(B2).convert_alpha(), BUTTON_SIZE)
			self.pic = self.image.copy()
			self.rect = self.image.get_rect()
			self.rect.topleft = (0, BUTTON_SIZE[1])
			self.price = 1000
			self.bonus = 10000
		elif name == 'extra-super':
			self.image = pg.transform.scale(pg.image.load(B2).convert_alpha(), BUTTON_SIZE)
			self.pic = self.image.copy()
			self.rect = self.image.get_rect()
			self.rect.topleft = (0, BUTTON_SIZE[1] * 2)
			self.price = 100000
			self.bonus = 1000000
		


	def update(self, lmb, coins, power, passive, ms):
		if lmb:
			x, y = pg.mouse.get_pos()
			if self.rect.left <= x <= self.rect.right and self.rect.top <= y <= self.rect.bottom:
				coins, power = self.on_pressed(coins, power)

		self.image = self.pic.convert_alpha()
		text = self.font_2.render('Активный доход', True, RED)
		w, h = text.get_size()
		x, y = self.rect.size
		self.image.blit(text, ((x - w) // 2, y // 2 - 2 * h  - 35))
		text = self.font.render('Уровень: ' + str(self.level), True, RED)
		w, h = text.get_size()
		x, y = self.rect.size
		self.image.blit(text, ((x - w) // 2, y // 2 - 2 * h))
		text = self.font.render('Бонус: ' + str(self.bonus), True, RED)
		w, h = text.get_size()
		x, y = self.rect.size
		self.image.blit(text, ((x - w) // 2, y // 2 - h))
		text = self.font.render('Цена: ' + f'{self.price:.1f}', True, RED)
		w, h = text.get_size()
		self.image.blit(text, ((x - w) // 2, y // 2))

		return coins, power, passive

	def on_pressed(self, coins, power):
		if coins >= self.price:
			coins -= self.price
			power += self.bonus
			self.price *= 1.1
			self.level += 1
		return coins, power


class Button_Passive(pg.sprite.Sprite):
	def __init__(self, name):
		pg.sprite.Sprite.__init__(self)
		self.level = 0
		self.font = pg.font.SysFont('Comic Sans MS', 20)
		self.font_2 = pg.font.SysFont('Comic Sans MS', 20)
		if name  == 'base':
			self.image = pg.transform.scale(pg.image.load(B3).convert_alpha(), BUTTON_SIZE)
			self.pic = self.image.copy()
			self.rect = self.image.get_rect()
			self.rect.topleft = (600, 0)
			self.price = 10
			self.bonus = 1
		elif name == 'ultra':
			self.image = pg.transform.scale(pg.image.load(B3).convert_alpha(), BUTTON_SIZE)
			self.pic = self.image.copy()
			self.rect = self.image.get_rect()
			self.rect.topleft = (600, BUTTON_SIZE[1])
			self.price = 1000
			self.bonus = 10000
		elif name == 'extra-super':
			self.image = pg.transform.scale(pg.image.load(B3).convert_alpha(), BUTTON_SIZE)
			self.pic = self.image.copy()
			self.rect = self.image.get_rect()
			self.rect.topleft = (600, BUTTON_SIZE[1] * 2)
			self.price = 100000
			self.bonus = 1000000

	def update(self, lmb, coins, power, passive, ms):
		if lmb:
			x, y = pg.mouse.get_pos()
			if self.rect.left <= x <= self.rect.right and self.rect.top <= y <= self.rect.bottom:
				coins, passive = self.on_pressed(coins, passive)

		self.image = self.pic.convert_alpha()
		text = self.font_2.render('Пассивный доход', True, RED)
		w, h = text.get_size()
		x, y = self.rect.size
		self.image.blit(text, ((x - w) // 2, y // 2 - 2 * h  - 35))
		text = self.font.render('Уровень: ' + str(self.level), True, RED)
		w, h = text.get_size()
		x, y = self.rect.size
		self.image.blit(text, ((x - w) // 2, y // 2 - 2 * h))
		text = self.font.render('Бонус: ' + str(self.bonus), True, RED)
		w, h = text.get_size()
		x, y = self.rect.size
		self.image.blit(text, ((x - w) // 2, y // 2 - h))
		text = self.font.render('Цена: ' + f'{self.price:.1f}', True, RED)
		w, h = text.get_size()
		self.image.blit(text, ((x - w) // 2, y // 2))

		return coins, power, passive

	def on_pressed(self, coins, passive):
		if coins >= self.price:
			coins -= self.price
			passive += self.bonus
			self.price *= 1.1
			self.level += 1
		return coins, passive

class Info(pg.sprite.Sprite):
	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.transform.scale(pg.image.load(B5).convert_alpha(), (250, 150))
		self.pic = self.image.copy()
		self.rect = self.image.get_rect()
		self.rect.topleft = (300, 300)
		self.price = 1
		self.level = 0
		self.font = pg.font.SysFont('Comic Sans MS', 20)
		self.font_2 = pg.font.SysFont('Comic Sans MS', 15)

	def update(self, lmb, coins, power, passive, ms):
		self.image = self.pic.convert_alpha()
		text = self.font_2.render('Информация', True, RED)
		w, h = text.get_size()
		x, y = self.rect.size
		self.image.blit(text, ((x - w) // 2, y // 2 - 2 * h  - 35))
		text = self.font.render('Сила: ' + str(power), True, RED)
		w, h = text.get_size()
		x, y = self.rect.size
		self.image.blit(text, ((x - w) // 2, y // 2 - 2 * h))
		text = self.font.render('Пассивная: ' + str(passive), True, RED)
		w, h = text.get_size()
		x, y = self.rect.size
		self.image.blit(text, ((x - w) // 2, y // 2 - h))
		text = self.font.render('Монеты: ' + f'{coins:.1f}', True, RED)
		w, h = text.get_size()
		self.image.blit(text, ((x - w) // 2, y // 2))
		
		return coins, power, passive

class Belka(pg.sprite.Sprite):
	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.image.load(BELKA)
		self.image = pg.transform.scale(self.image, BELKA_SIZE)
		self.image.convert_alpha()
		self.rect = self.image.get_rect()
		self.speed = 12
		self.speed_x = self.speed_y = 0

		side = ['top', 'right', 'bottom', 'left']
		side = r.choice(side)
		if side == 'top':
			self.rect.top = 0
			self.rect.left = r.randint(0, WIN_SIZE[0] - BELKA_SIZE[0])
			self.dest = (r.randint(0, WIN_SIZE[0] - BELKA_SIZE[0]), WIN_SIZE[1])
		k = (WIN_SIZE[0] ** 2 + WIN_SIZE[1] ** 2) ** (0.5) / self.speed
		self.speed_x = (self.dest[0] - self.rect.x) / k
		self.speed_y = (self.dest[1] - self.rect.y) / k

	def update(self):
		self.rect.x += self.speed_x
		self.rect.y += self.speed_y

		if self.speed_x > 0:
			if self.rect.x > self.dest[0]:
				if self.speed_y > 0:
					if self.rect.y > self.dest[1]:
						self.kill()
				else:
					if self.rect.y < self.dest[1]:
						self.kill()
		else:
			if self.rect.x < self.dest[0]:
				if self.speed_y > 0:
					if self.rect.y > self.dest[1]:
						self.kill()
				else:
					if self.rect.y < self.dest[1]:
						self.kill()