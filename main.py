#Written by Hashim Kadhom

#Imports required classes and libraries
import pygame
import math
import random
from sprite import Sprite
from player import Player
from enemy import Enemy
from interface import Interface
from ray import Ray

#Here pygame is intitialized
pygame.init()

#Here the window is set up
SCREEN_DIMENSIONS = (800,500)
win = pygame.display.set_mode(SCREEN_DIMENSIONS)

#Block parameters are set up here
BLOCK_COLOUR = [255,255,255]
BLOCK_SIZE = [30,30]
block_list = []
block_data = [
  [1,1,1,1,1,1,1],
  [1,0,0,0,0,0,1],
  [1,0,0,1,0,0,1],
  [1,0,0,0,0,0,1],
  [1,0,1,0,0,1,1],
  [1,0,1,0,0,0,1],
  [1,0,1,0,0,0,1],
  [1,0,0,0,0,0,1],
  [1,0,0,0,1,0,1],
  [1,0,0,0,1,0,1],
  [1,1,0,0,1,0,1],
  [1,0,0,0,0,0,1],
  [1,0,0,1,0,0,1],
  [1,0,0,0,0,0,1],
  [1,1,1,1,1,1,1],
]
for row_number in range(len(block_data)):
  for column_number in range(len(block_data[row_number])):
    if block_data[row_number][column_number] == 1:
      block_list.append(Sprite(
        win,
        [column_number*BLOCK_SIZE[0],
         row_number*BLOCK_SIZE[1]],
        BLOCK_SIZE,
        BLOCK_COLOUR))

#Player parameters
PLAYER_COLOUR = [255,255,0]
PLAYER_SIZE = [10,10]
player = Player(win,[100,220],PLAYER_SIZE,PLAYER_COLOUR,0,0,1000)

#Enemy parameters
ENEMY_COLOUR = (255,0,0)
ENEMY_SIZE = [10,10]
health = 2
SPEED = 0.5
enemy_list = []

#Wave parameters
wave_parameters = {"spawn_cooldown": 0,"enemies_to_spawn": 0}

#Interface parameters
interface = Interface(win,[0,400],SCREEN_DIMENSIONS,10,0,0)

#Ray data is stored here
ray_list = []

#Column data is stored here
wall_columns = []
enemy_columns = []

#This function contains the main loop and sequences
#All the other functions
def main():
  #Initial game state
  game_state = "menu_screen"
  
  TIME_DELAY = 10
  running = True
  while running:
    pygame.time.delay(TIME_DELAY)

    #This checks if the user closes the program
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()

    #This checks if the user is on the menu
    if game_state == "menu_screen":
      win.fill((0,0,0))
      
      win.blit(
      pygame.transform.scale(
      pygame.image.load("screens/menu_screen.png"),
        (800,500)),(0,0))

      #This registers whether the user has clicked the PLAY button
      if (pygame.mouse.get_pressed()[0] 
          and pygame.mouse.get_pos()[0] > 325 
          and pygame.mouse.get_pos()[0] < 477 
          and pygame.mouse.get_pos()[1] > 280 
          and pygame.mouse.get_pos()[1] < 330):
        game_state = "game_screen"

        #This resets the interface
        interface.health = 10
        interface.wave = 0
        interface.points = 0

        #This resets the player
        player.position = [100,220]
        player.direction = 0

        #This resets the enemies
        enemy_list.clear()
        wave_parameters = {
          "spawn_cooldown": pygame.time.get_ticks(),
          "enemies_to_spawn": 0
        }

      #This registers whether the user has clicked the CREDITS button
      if (pygame.mouse.get_pressed()[0] 
          and pygame.mouse.get_pos()[0] > 325 
          and pygame.mouse.get_pos()[0] < 477 
          and pygame.mouse.get_pos()[1] > 423 
          and pygame.mouse.get_pos()[1] < 474):
        game_state = "credits_screen"

      #This registers whether the user has clicked the CONTROLS button
      if (pygame.mouse.get_pressed()[0] 
          and pygame.mouse.get_pos()[0] > 294 
          and pygame.mouse.get_pos()[0] < 511 
          and pygame.mouse.get_pos()[1] > 351 
          and pygame.mouse.get_pos()[1] < 399):
        game_state = "controls_screen"

      pygame.display.update()

    #This checks if the user is on the credits
    if game_state == "credits_screen":
      win.fill((0,0,0))
      
      win.blit(
      pygame.transform.scale(
      pygame.image.load("screens/credits_screen.png"),
        (800,500)),(0,0))

      #This registers whether the user has clicked the RETURN button
      if (pygame.mouse.get_pressed()[0] 
          and pygame.mouse.get_pos()[0] > 348 
          and pygame.mouse.get_pos()[0] < 487 
          and pygame.mouse.get_pos()[1] > 46 
          and pygame.mouse.get_pos()[1] < 87): 
        game_state = "menu_screen"
      
      pygame.display.update()

    #This checks if the user is on the controls screen
    if game_state == "controls_screen":
      win.fill((0,0,0))
      
      win.blit(
      pygame.transform.scale(
      pygame.image.load("screens/controls_screen.png"),
        (800,500)),(0,0))

      #This registers whether the user has clicked the RETURN button
      if (pygame.mouse.get_pressed()[0] 
          and pygame.mouse.get_pos()[0] > 357 
          and pygame.mouse.get_pos()[0] < 496 
          and pygame.mouse.get_pos()[1] > 45 
          and pygame.mouse.get_pos()[1] < 85):
        game_state = "menu_screen"
      
      pygame.display.update()

    #This checks if the user is on the shop screen
    if game_state == "shop_screen":
      win.fill((0,0,0))
      
      win.blit(
      pygame.transform.scale(
      pygame.image.load("screens/shop_screen.png"),
        (800,500)),(0,0))

      #This registers whether the user has clicked the RETURN button
      if (pygame.mouse.get_pressed()[0] 
          and pygame.mouse.get_pos()[0] > 348 
          and pygame.mouse.get_pos()[0] < 487 
          and pygame.mouse.get_pos()[1] > 46 
          and pygame.mouse.get_pos()[1] < 87): 
        game_state = "game_screen"

      #This registers whether the user's mouse is on HEALTH RESTORE
      if (pygame.mouse.get_pos()[0] > 152 
          and pygame.mouse.get_pos()[0] < 271 
          and pygame.mouse.get_pos()[1] > 337 
          and pygame.mouse.get_pos()[1] < 392):
            
        #This displays ths item's description
        render_shop_description(
          "THIS WILL MAKE YOU",
          "FULLY HAPPY AGAIN",
          "(BACK TO FULL HP)",
          "FOR A 100 POINTS"
        )

        #This checks if the user clicked, if they have enough
        #Points, they will recieve the item. Otherwise, they
        #Will be returned to the game
        if pygame.mouse.get_pressed()[0]:
          if interface.points >= 100:
            interface.health = 10
            interface.points -= 100
            game_state = "game_screen"
          else:
            render_shop_description(
              "",
              "       NOT ENOUGH",
              "            POINTS",
              ""
            )
            pygame.display.update()
            pygame.time.delay(700)

      #This registers whether the user's mouse is on SHOOTING UPGRADE
      if (pygame.mouse.get_pos()[0] > 534 
          and pygame.mouse.get_pos()[0] < 652 
          and pygame.mouse.get_pos()[1] > 337 
          and pygame.mouse.get_pos()[1] < 389):

        #This displays ths item's description
        render_shop_description(
          "THIS WILL DECREASE",
          "THE TIME IT TAKES",
          "TO SHOOT AGAIN",
          "FOR A 100 POINTS"
        )

        #This checks if the user clicked, if they have enough
        #Points, they will recieve the item. Otherwise, they
        #Will be returned to the game
        if pygame.mouse.get_pressed()[0]:
          if interface.points >= 100:
            player.shoot_cooldown /= 2
            interface.points -= 100
            game_state = "game_screen"
          else:
            render_shop_description(
              "",
              "       NOT ENOUGH",
              "            POINTS",
              ""
            )
            pygame.display.update()
            pygame.time.delay(700)
      
      pygame.display.update()

    #This checks if the user has fainted
    if game_state == "death_screen":
      win.fill((0,0,0))
      
      win.blit(
      pygame.transform.scale(
      pygame.image.load("screens/death_screen.png"),
        (800,500)),(0,0))

      #This registers whether the user has clicked the MENU button
      if (pygame.mouse.get_pressed()[0] 
          and pygame.mouse.get_pos()[0] > 325 
          and pygame.mouse.get_pos()[0] < 491 
          and pygame.mouse.get_pos()[1] > 138 
          and pygame.mouse.get_pos()[1] < 191):
        game_state = "menu_screen"

      pygame.display.update()

    #This checks if the user is playing the game  
    if game_state == "game_screen":
      win.fill((0,0,0))

      #The user's keyboard input is stored here
      input = pygame.key.get_pressed()
      
      #Here the rays are formulated
      produce_rays()
  
      #Here the player's movement and controls are processed
      player.controls(input)
  
      #Here the waves are processed
      if (wave_parameters["enemies_to_spawn"] == 0 
          and len(enemy_list) == 0):
        interface.wave += 1
        interface.points += 10
        wave_parameters["enemies_to_spawn"] = interface.wave
  
      if (wave_parameters["enemies_to_spawn"] > 0 
          and pygame.time.get_ticks() 
          - wave_parameters["spawn_cooldown"] > 2000):
        enemy_spawn = random.choice(
            [[30,30],
             [150,30],
             [30,390],
             [150,390]]) 
        enemy_list.append(Enemy(
          win,
          enemy_spawn,
          ENEMY_SIZE,
          ENEMY_COLOUR,
          SPEED,
          health,
          0))
        wave_parameters["enemies_to_spawn"] -= 1
        wave_parameters["spawn_cooldown"] = pygame.time.get_ticks()
            
      
      #Here the entity-block collisions are processed
      for block in block_list:
        if player.check_collision(block.position,block.size):
          block_physics(player,block)
        for enemy in enemy_list:
          if enemy.check_collision(block.position,block.size):
            block_physics(enemy,block)
  
      #Here the enemies are processed
      for enemy in enemy_list:
        enemy.chase(player.position,player.size)
        if (enemy.attacking(player.position,player.size) 
            and pygame.time.get_ticks() 
            - enemy.attack_cooldown > 1000):
          interface.health -= 1
          enemy.attack_cooldown = pygame.time.get_ticks()
      
      #Here the player's interface is visualized
      interface.render()
  
      #Here, every column is drawn
      for wall in wall_columns:
        wall.draw()
      for enemy in enemy_columns:
        enemy.draw()
  
      #Here the columns are formulated based off the rays
      wall_columns.clear()
      enemy_columns.clear()
      for ray in ray_list:
        ray_distance = ray.get_block_distance(block_list,enemy_list)
        produce_visual_column(ray_list.index(ray),ray_distance)
        
        #This segment manages the shooting process
        if (ray_list.index(ray) == 20
            and pygame.time.get_ticks() - player.shoot_timer 
              > player.shoot_cooldown 
            and player.shooting(input)):
          render_shoot()
          player.shoot_timer = pygame.time.get_ticks()
              
          #If an enemy is 'hittable'
          if ray_distance[1] < 130:
            enemy_list[ray_distance[2]].health -= 1
            interface.points += 1
            
            #If enemy reaches 0 health
            if enemy_list[ray_distance[2]].health <= 0:
              enemy_list.pop(ray_distance[2])
              interface.points += 5

      #This visualizes the player's crosshair
      render_crosshair()

      #This checks if the player has fainted
      if interface.health <= 0:
        game_state = "death_screen"

      #This checks if the player has entered the shop
      if input[pygame.K_TAB]:
        game_state = "shop_screen"

      # for block in block_list:
      #   block.draw()

      # for enemy in enemy_list:
      #   enemy.draw()

      # player.draw()

      pygame.display.update()

#This function manages block physics
#Parameters:
  #entity: a player or enemy object
  #block: a block object
def block_physics(entity,block):
  #BUFFER refers to how thick the collision barriers are
  BUFFER = 2

  #This checks if the entity is on the block's top face
  #And moves them away if so
  top_face = Sprite(
    win,
    [block.position[0] + BUFFER,
     block.position[1]],
    [block.size[0] - 2*BUFFER,
     BUFFER],
    (0,0,0))
  if entity.check_collision(top_face.position,top_face.size):
    entity.position[1] = top_face.position[1] - entity.size[1]

  #This checks if the entity is on the block's bottom face
  #And moves them away if so
  bottom_face = Sprite(
    win,
    [block.position[0] + BUFFER,
     block.position[1] + block.size[1] - BUFFER],
    [block.size[0] - 2*BUFFER,BUFFER],
    (0,0,0))
  if entity.check_collision(bottom_face.position,bottom_face.size):
    entity.position[1] = bottom_face.position[1] + bottom_face.size[1]

  #This checks if the entity is on the block's right face
  #And moves them away if so
  right_face = Sprite(
    win,
    [block.position[0] + block.size[0] - BUFFER,
     block.position[1] + BUFFER],
    [BUFFER,block.size[1] - 2*BUFFER],
    (0,0,0))
  if entity.check_collision(right_face.position,right_face.size):
    entity.position[0] = right_face.position[0] + right_face.size[0]

  #This checks if the entity is on the block's left face
  #And moves them away if so
  left_face = Sprite(
    win,
    [block.position[0],
     block.position[1] + BUFFER],
    [BUFFER,block.size[1] - 2*BUFFER],
    (0,0,0))
  if entity.check_collision(left_face.position,left_face.size):
    entity.position[0] = left_face.position[0] - entity.size[0]

#This function clears the ray data and appends it
#With new rays, so new data may be collected
def produce_rays():
  ray_list.clear()
  RAY_AMOUNT = 40
  for ray_number in range(RAY_AMOUNT):
    direction_change = (math.pi / (3*(RAY_AMOUNT - 1)))
    ray_list.append(Ray(
      [player.position[0] + player.size[0]/2,
       player.position[1] + player.size[1]/2],
      player.direction + direction_change*(RAY_AMOUNT - 1)/2 
      - direction_change*ray_number))

#This function produces the user's visuals
#Based off how far the player is from the wall
#Parameters:
  #ray_number: integer
  #ray_distance: int[1]
def produce_visual_column(ray_number,ray_distance):
  
  #This segment creates the wall columns
  wall_colour = (
    255 - 2*ray_distance[0],
    255 - 2*ray_distance[0],
    255 - 2*ray_distance[0]
  )
  if wall_colour[0] < 0:
    wall_colour = (0,0,0)
    
  wall_columns.append(Sprite(
    win,
    [ray_number*SCREEN_DIMENSIONS[0]/len(ray_list),
     ray_distance[0]],
    [SCREEN_DIMENSIONS[0]/len(ray_list),
     400 - 2*ray_distance[0]],
    wall_colour))

  #This segment creates the entity columns
  enemy_colour = (255 - 2*ray_distance[1],0,0)
  if enemy_colour[0] > 0:     
    enemy_columns.append(Sprite(
      win,
      [ray_number*SCREEN_DIMENSIONS[0]/len(ray_list),
       50 + ray_distance[1]],
      [SCREEN_DIMENSIONS[0]/len(ray_list),
       350 - 2*ray_distance[1]],
      enemy_colour))
  else:
    enemy_colour = (0,0,0)
    enemy_columns.append(Sprite(win,[0,0],[0,0],enemy_colour))

#This function renders the player's crosshair
def render_crosshair():
  CROSSHAIR_SIZE = 5
  pygame.draw.rect(
    win,(255,255,0),
    (SCREEN_DIMENSIONS[0]/2 - CROSSHAIR_SIZE/2,
     SCREEN_DIMENSIONS[1]/2 - 50 - CROSSHAIR_SIZE/2,
     CROSSHAIR_SIZE,
     CROSSHAIR_SIZE))

#This function visualizes the shooting effect
def render_shoot():
  EFFECT_SIZE = 30
  pygame.draw.rect(
    win,(255,255,0),
    (SCREEN_DIMENSIONS[0]/2 - EFFECT_SIZE/2,
     SCREEN_DIMENSIONS[1]/2 - 50 - EFFECT_SIZE/2,
     EFFECT_SIZE,
     EFFECT_SIZE))
  pygame.display.update()
  pygame.time.delay(150)

#This function creates a text box that follows the player's mouse
#Parameters:
  #line_1: string
  #line_2: string
  #line_3: string
  #line_4: string
def render_shop_description(line_1,line_2,line_3,line_4):
  FONT = 13
  pygame.draw.rect(
    win,(255,255,255),
    (pygame.mouse.get_pos()[0],
     pygame.mouse.get_pos()[1] - 70,
     155,80))
  win.blit(pygame.font.SysFont("Comic Sans MS",FONT).render(
    line_1,
    False,(0,0,0)),[
    pygame.mouse.get_pos()[0] + 5,
    pygame.mouse.get_pos()[1] - 65])
  win.blit(pygame.font.SysFont("Comic Sans MS",FONT).render(
    line_2,
    False,(0,0,0)),[
    pygame.mouse.get_pos()[0] + 5,
    pygame.mouse.get_pos()[1] - 45])
  win.blit(pygame.font.SysFont("Comic Sans MS",FONT).render(
    line_3,
    False,(0,0,0)),[
    pygame.mouse.get_pos()[0] + 5,
    pygame.mouse.get_pos()[1] - 25])
  win.blit(pygame.font.SysFont("Comic Sans MS",FONT).render(
    line_4,
    False,(0,0,0)),[
    pygame.mouse.get_pos()[0] + 5,
    pygame.mouse.get_pos()[1] - 5])

main()