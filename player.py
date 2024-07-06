#Here the necessary libraries and classes are imported
import pygame
import math
from sprite import Sprite

#This class defines the player object
#Parameters:
  #screen: Surface
  #position: float[1]
  #size: float[1]
  #colour: int[2]
  #direction: float
  #shoot_timer: int
  #shoot_cooldown: int
class Player(Sprite):
  #This method assigns the class objects with their parameters
  def __init__(
      self,
      screen,
      position,
      size,
      colour,
      direction,
      shoot_timer,
      shoot_cooldown):
    Sprite.__init__(self,screen,position,size,colour)
    self.direction = direction
    self.shoot_timer = shoot_timer
    self.shoot_cooldown = shoot_cooldown

  #This method takes the user input and translates it into
  #Movements in the game
  #Parameters:
    #input: boolean[unknown]
  def controls(self,input):
    SPEED = 1
    SENSITIVITY = 0.05
    
    if input[pygame.K_RIGHT]:
      self.direction -= SENSITIVITY
    if input[pygame.K_LEFT]:
      self.direction += SENSITIVITY

    if input[pygame.K_w]:
      self.position[0] += SPEED*math.cos(self.direction)
      self.position[1] -= SPEED*math.sin(self.direction)
    if input[pygame.K_s]:
      self.position[0] -= SPEED*math.cos(self.direction)
      self.position[1] += SPEED*math.sin(self.direction)
    if input[pygame.K_d]:
      self.position[0] += SPEED*math.sin(self.direction)
      self.position[1] += SPEED*math.cos(self.direction)
    if input[pygame.K_a]:
      self.position[0] -= SPEED*math.sin(self.direction)
      self.position[1] -= SPEED*math.cos(self.direction)

  #This method returns true if the player is shooting
  #Parameters:
    #input: boolean[unknown]
  def shooting(self,input):
    if input[pygame.K_UP]:
      return True
    else:
      return False