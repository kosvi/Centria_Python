#!/usr/bin/python3

import pygame, sys, random
from snake import Snake
from food import Food
from pygame.locals import *

# https://coderslegacy.com/python/python-pygame-tutorial/
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
food = Food(WIDTH, HEIGHT, snake.size, WHITE, snake.head)
points = 0

# https://stackoverflow.com/questions/43441996/how-to-display-game-over-screen-and-you-win-screen-in-pygame
# https://www.geeksforgeeks.org/python-display-text-to-pygame-window/
def game_over_screen():
  DISPLAYSURF.fill(pygame.Color(255,0,0))
  font = pygame.font.Font("freesansbold.ttf", 32)
  text = font.render("GAME OVER", True, BLACK, BLUE)
  textRect = text.get_rect()
  textRect.center = (WIDTH // 2, HEIGHT // 2)
  DISPLAYSURF.blit(text, textRect)

def show_score(score):
  font = pygame.font.Font("freesansbold.ttf", 12)
  text = font.render(f"Score {score}", True, WHITE)
  textRect = text.get_rect()
  textRect.topleft = (0,0)
  DISPLAYSURF.blit(text, textRect)

# https://coderslegacy.com/python/python-pygame-tutorial/
while True:
  if not snake.collide:
    DISPLAYSURF.fill(pygame.Color(0, 0, 0))
    show_score(points)
    current = snake.head
    while current.next != None:
      current = current.next
      pygame.draw.rect(DISPLAYSURF, BLUE, (current.x, current.y, snake.size, snake.size))
    pygame.draw.rect(DISPLAYSURF, GREEN, (snake.head.x, snake.head.y, snake.size, snake.size))
    pygame.draw.rect(DISPLAYSURF, food.type, (food.x, food.y, food.size, food.size))
    snake.move()
    if food.check_hit(snake.head)>0:
      points += 1
      snake.add_cell()
      food = Food(WIDTH, HEIGHT, snake.size, WHITE, snake.head)
  elif snake.collide:
    game_over_screen()

  for event in pygame.event.get():
    if event.type == KEYDOWN:
      if event.key == K_DOWN:
        snake.set_direction("DOWN")
      elif event.key == K_UP:
        snake.set_direction("UP")
      elif event.key == K_LEFT:
        snake.set_direction("LEFT")
      elif event.key == K_RIGHT:
        snake.set_direction("RIGHT")
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  pygame.display.update()
  CLOCK.tick(30)

