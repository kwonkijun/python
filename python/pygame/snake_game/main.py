import pygame
import sys
import time
import random

from pygame.locals import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH / GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT / GRID_SIZE


WHITE = (255,255,255)
GREEN = (0,50,0)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake(object):
	def __init__(self):
		self.create()
		self.color = GREEN

	def create(self):
		self.length = 2
		self.positions = [(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)]
		self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

	def control(self, xy):
		if(xy[0] * -1, xy[1] * -1) == self.direction:
			return
		else:
			self.direction = xy
	
	def move(self):
		cur = self.positions[0]
		x, y = self.direction
		new = ((cur[0] +(x + GRID_SIZE) % WINDOW_WIDTH ))

if __name__ == '__main__':
	pygame.init() # 초기화
	window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32) # 창크기
	pygame.display.set_caption('Snake Game') # 제목
	surface = pygame.Surface(window.get_size()) # 실제 게임이 들어갈 곳
	surface = surface.convert()
	surface.fill(WHITE)
	clock = pygame.time.Clock()
	pygame.key.set_repeat(1,40)
	window.blit(surface, (0,0))