# JetpackJoyride
### How to run:
    python3 main.py
### Packages required:
### About Jetpack Joyride:
    Jetpack Joyride is a 2011 side-scrolling endless runner action video game created 
    by Halfbrick Studios. The game features the same protagonist from Monster Dash,
    Barry Steakfries, who the player controls as he steals a jet pack from a top-secret laboratory. 
    The game has been met with very favorable reviews, and has won numerous awards.
### About Game:
   * This is an interactive game with numerous features.
   * You are given 100 sec to win the game.
   * Random generation of all elements.
   * Random ordering of various hurdles
   * Smooth physics simiulation
   * Fire implementation, which shoots fireballs towards players.
   * Smart enemy, dragon which always tries to follows Mondo
   * Coins can be collected
   * Colors for characters
   * Follow OOP concepts
   * Powerups like Shields and Powerups.
    
### Description of files:
* objects.py

  
  This file contains classes of coins, bullet, obstacle.
* dragon.py
  
  This file contains classes of dragon(enemy) and its fire.
* input.py
  
  This file is for taking input
  This file is for exception
* board.py

  
  This file creates the background of the game.
* main.py
  
  This file contains the main loop.
* mando.py

  This file contains class of mondo.

### Inheritance:
  mando class is inherited from person.
  Dragon class is inherited from person.
### Encapsulation :
  The fact that I’m using classes and objects suffice for this!
### Abstraction :
  This is used in mando,dragon,etc many class.
### Polymorphism:
  bullet is changing for dragon,mando.
### Controls:
w for up,d for right, a for left, b for shoot, space for shield, p for nitro.
