#Here the necessary libraries and classes are imported
import pygame
from interface import Interface
from sprite import Sprite

#This class defines an enemy object
#Parameters:
  #screen: Surface
  #position: float[1]
  #size: float[1]
  #colour: int[2]
  #speed: float
  #health: int
  #attack_cooldown: int
class Enemy(Sprite):
  #This method assigns the class objects with their parameters
  def __init__(
      self,
      screen,
      position,
      size,
      colour,
      speed,
      health,
      attack_cooldown):
    Sprite.__init__(self,screen,position,size,colour)
    self.speed = speed
    self.health = health
    self.attack_cooldown = attack_cooldown

  #This method updates the enemy's position to get closer to a certain entity.
  #While accounting for its size, the enemy will stop if they get too close
  #To the entity
  #Parameters:
    #entity_position: float[1]
    #entity_size: float[1]
  def chase(self,entity_position,entity_size):
    ATTACK_BUFFER = 5
    if not self.check_collision(
      [entity_position[0] - ATTACK_BUFFER,
       entity_position[1] - ATTACK_BUFFER],
      [entity_size[0] + 2*ATTACK_BUFFER,
       entity_size[1] + 2*ATTACK_BUFFER]):
      if self.position[0] > entity_position[0]:
        self.position[0] -= self.speed
      if self.position[0] < entity_position[0]:
        self.position[0] += self.speed
      
      if self.position[1] > entity_position[1]:
        self.position[1] -= self.speed
      if self.position[1] < entity_position[1]:
        self.position[1] += self.speed

  #This method returns True if the enemy is within attacking range
  #Parameters:
    #entity_position: float[1]
    #entity_size: float[1]
  def attacking(self,entity_position,entity_size):
    ATTACK_BUFFER = 5
    if self.check_collision(
      [entity_position[0] - ATTACK_BUFFER,
       entity_position[1] - ATTACK_BUFFER],
      [entity_size[0] + 2*ATTACK_BUFFER,
       entity_size[1] + 2*ATTACK_BUFFER]):
      return True
    else:
      return False