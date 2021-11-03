#!/usr/bin/python3

import pygame, sys, random
from snake import Snake
from pygame.locals import *

pygame.init()
WIDTH = 300
HEIGHT = 300
DISPLAYSURF = pygame.display.set_mode((WIDTH,HEIGHT))
BLACK = pygame.Color(0,0,0)
WHITE = pygame.Color(255,255,255)
GREEN = pygame.Color(0,255,0)
BLUE = pygame.Color(0,0,255)
CLOCK = pygame.time.Clock()

snake = Snake(WIDTH, HEIGHT)

while True:
  DISPLAYSURF.fill(pygame.Color(0, 0, 0))
  current = snake.head
  while current.next != None:
    current = current.next
    pygame.draw.rect(DISPLAYSURF, BLUE, (current.x, current.y, snake.size, snake.size))
  pygame.draw.rect(DISPLAYSURF, GREEN, (snake.head.x, snake.head.y, snake.size, snake.size))
  snake.move()
  if random.randint(0,10)==10:
    snake.add_cell()
  for event in pygame.event.get():
    if event.type == KEYDOWN:
      if event.key == K_DOWN:
        snake.direction = "DOWN"
      elif event.key == K_UP:
        snake.direction = "UP"
      elif event.key == K_LEFT:
        snake.direction = "LEFT"
      elif event.key == K_RIGHT:
        snake.direction = "RIGHT"
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  pygame.display.update()
  CLOCK.tick(30)
