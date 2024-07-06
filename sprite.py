#This imports the necessary libraries
import pygame

#This class defines the general sprite, which can be drawn on
#Used for images, and for collision boxes
#Parameters:
  #screen: Surface
  #position: float[1]
  #size: float[1]
  #colour: int[2]
class Sprite:
  #This method assigns the class objects with their parameters
  def __init__(self,screen,position,size,colour):
    self.screen = screen
    self.position = position
    self.size = size
    self.colour = colour

  #This method draws the sprite on to the screen surface
  def draw(self):
    pygame.draw.rect(
      self.screen,
      self.colour,
      self.position + self.size)

  #This method checks if the sprite has collided with any
  #Other entities of a certain position and size
  #Parameters:
    #entity_position: float[1]
    #entity_size: float[1]
  def check_collision(self,entity_position,entity_size):
    if (self.position[0] + self.size[0] > entity_position[0] 
        and self.position[0] < entity_position[0] + entity_size[0] 
        and self.position[1] + self.size[1] > entity_position[1] 
        and self.position[1] < entity_position[1] + entity_size[1]):
      return True
    else:
      return False