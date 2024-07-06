#Here the necessary libraries are imported
import pygame

#This class manages background parameters like wave number
#health, points, while displaying them for the user to see
#Parameters:
  #screen: Surface
  #position: float[1]
  #screen_dimensions: int[1]
  #health: int
  #wave: int
  #points: int
class Interface:
  #This method assigns the class objects with their parameters
  def __init__(
      self,
      screen,
      position,
      screen_dimensions,
      health,
      wave,
      points):
    self.screen = screen
    self.position = position
    self.screen_dimensions = screen_dimensions
    self.health = health
    self.wave = wave
    self.points = points

  #This method renders the interface onto the screen
  def render(self):
    font = pygame.font.SysFont("Comic Sans MS",35)
    
    #This draws the base of the interface
    pygame.draw.rect(
      self.screen,
      (255,255,255),
      (self.position[0],self.position[1],
       self.screen_dimensions[0],
       self.screen_dimensions[1] - self.position[1]))

    #This writes the wave number
    self.screen.blit(font.render(
      f"WAVE: {str(self.wave)}",
      False,(0,0,0)),(self.position[0] + 600,self.position[1] + 30))

    #This writes the points number
    self.screen.blit(font.render(
      f"POINTS: {str(self.points)}",
      False,(0,0,0)),(self.position[0] + 250,self.position[1] + 30))

    #This displays the player's health as images
    #Only if the health is between 0 and 11
    if self.health > 0 and self.health < 11:
      self.screen.blit(
        pygame.transform.scale(
        pygame.image.load(
          f"health_indicators/health_indicator_{str(self.health)}.png"),
          (90,90)),(self.position[0] + 15,self.position[1] + 5))