# Game of Life
A recreation of famous simulation "Conway's Game of Life" by John Horton Conway, complimented with adjustable speeds and various controls.

![Gospers_glider_gun](https://github.com/yagizdas/Game-of-Life/assets/165295777/b5924ce5-3c46-4a83-88e1-b3eb3c5207a8)

## Game Rules:
At each step in time, the following transitions occur:

     Any live cell with fewer than two live neighbors dies, as if by underpopulation.
     Any live cell with two or three live neighbors lives on to the next generation.
     Any live cell with more than three live neighbors dies, as if by overpopulation.
     Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
    
## Controls:

 - A:Add lives to current grid
 - R: Reset grid
 - C: Clear grid
 - N: Speed up the simulation
 - M: Speed down the simulation
 - Esc: Go back to menu

### Steps to run the app:
  Python 3 and Pygame is required to operate this simulation. You can simply open main.py to use.
  If you do not have Pygame, you can easily download it by using this code on your terminal:
  ```
  pip install Pygame
  ```

I hope you find it fun! :) 
