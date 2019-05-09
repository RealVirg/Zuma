import random
import constant
import pygame
import math

class Ball(object):
	def __init__(self, x, y, color):
		self.x = x
		self.y = y
		self.color = color

4
class Snake(object):
	def __init__(self):
		self.start = (10, 50)
		self.firstTurn = (550, 50)
		self.secondTurn = (550, 550)
		self.thirdTurn = (50, 550)
		self.end = (50, 100)


	def render(self, screen):
		pass