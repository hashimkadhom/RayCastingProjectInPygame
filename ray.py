#Here the necessary libraries are imported
import pygame
import math

#This class defines a single ray in the game
#With it, the 2D map of the game can be converted
#Into a 3D world for the player
#Parameters:
  #initial_position: float[1]
  #direction: float
class Ray:
  #This method assigns the class objects with their parameters
  def __init__(self,initial_position,direction):
    self.initial_position = initial_position
    self.direction = direction

  #This method will return a three element list that consists
  #Of the block's distance, the enemy's distance, and
  #Which enemy has been hit
  def get_block_distance(self,block_list,enemy_list):
    RENDER_DISTANCE = 130
    SKIP = 4

    distance = [RENDER_DISTANCE,RENDER_DISTANCE,0]
    
    hit_enemy = False
    for increment in range(1,RENDER_DISTANCE,SKIP):
      test_point = [
        self.initial_position[0] + increment*math.cos(self.direction),
        self.initial_position[1] - increment*math.sin(self.direction)
      ] 

      #This segment manages the entity visuals
      if not hit_enemy:
        for enemy in enemy_list:
          if (test_point[0] > enemy.position[0] 
              and test_point[0] < enemy.position[0] + enemy.size[0] 
              and test_point[1] > enemy.position[1] 
              and test_point[1] < enemy.position[1] + enemy.size[1]):
            distance[1] = increment
            distance[2] = enemy_list.index(enemy)
            hit_enemy = True

      #This segment manages the block visuals
      for block in block_list:
        if (test_point[0] > block.position[0] 
            and test_point[0] < block.position[0] + block.size[0] 
            and test_point[1] > block.position[1] 
            and test_point[1] < block.position[1] + block.size[1]):
          distance[0] = increment
          return distance
        
    return distance