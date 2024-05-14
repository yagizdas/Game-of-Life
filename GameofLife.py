import pygame as py
import sys
import random
py.init()

BLK = (13,13,13)
WHITE = (242,242,242)
GREY = (38,38,38)
BLUE = (2,56,89)
W,H = 1200,1200
TILE_SIZE = 20
GRID_WIDTH = W//TILE_SIZE
GRID_HEIGHT = H//TILE_SIZE
FPS = 60

screen = py.display.set_mode((W, H))
menu = py.display.set_mode((W , H))

clock = py.time.Clock()

def gen(num):
    randset = set()
    for x in range(num):
        random_y = random.randrange(0,GRID_HEIGHT)
        random_x = random.randrange(0,GRID_WIDTH)
        randpos = (random_x,random_y)
        randset.add(randpos)
    return randset

def draw_grid(positions):
    for position in positions:
        col,row = position
        topleft = (col * TILE_SIZE, row * TILE_SIZE)
        py.draw.rect(screen, BLUE, (*topleft, TILE_SIZE, TILE_SIZE))

    for row in range(GRID_HEIGHT):
        py.draw.line(screen, BLK, (0,row * TILE_SIZE), (W, row * TILE_SIZE),2)
    for col in range(GRID_WIDTH):
        py.draw.line(screen, BLK, (col * TILE_SIZE, 0), (col * TILE_SIZE, H),2)

def grid_adjust(positions):
    all_neighbors = set()
    new_positions = set()

    for position in positions:
        neighbors = get_neighbors(position)
        all_neighbors.update(neighbors)
        
        neighbors = list(filter(lambda x: x in positions, neighbors))

        if len(neighbors) in [2,3]:
            new_positions.add(position)

    for position in all_neighbors:
        neighbors = get_neighbors(position)
        neighbors = list(filter(lambda x: x in positions, neighbors))
        
        if len(neighbors) == 3:
            new_positions.add(position)

    return new_positions
def get_neighbors(pos):
    x, y = pos
    neighbors = []
    for dx in [-1, 0, 1]:
        if x + dx < 0 or x + dx > GRID_WIDTH:
            continue
        for dy in [-1, 0, 1]:
            if y + dy < 0 or y + dy > GRID_HEIGHT:
                continue
            if dx == 0 and dy == 0:
                continue

            neighbors.append((x + dx, y + dy))
    
    return neighbors

def play():
    isRunning = True
    playing = True
    positions = set()
    count = 0
    first = True
    update_freq = 120
    update_freq_min = 10
    update_freq_max= 250
    while isRunning:
        clock.tick(FPS)
        if playing:
            count += 1

        if count >= update_freq:
            count = 0
            positions = grid_adjust(positions)

        for event in py.event.get():
            if event.type == py.QUIT:
                isRunning = False
            if event.type == py.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = py.mouse.get_pos()
                col = mouse_x // TILE_SIZE
                row = mouse_y // TILE_SIZE
                pos = (col,row)

                if pos in positions:
                    positions.remove(pos)
                else:
                    positions.add(pos)
            if event.type == py.KEYDOWN:
                if event.key == py.K_SPACE:
                    playing = not playing
                if event.key == py.K_c:
                    positions = set()
                    playing = False
                if event.key == py.K_r:
                    positions = gen(random.randrange(4,10) * GRID_WIDTH)
                    playing = True
                if event.key == py.K_a:
                    positions.update(gen(random.randrange(4,10) * GRID_WIDTH))
                if event.key == py.K_n:
                    if update_freq > update_freq_min:
                        update_freq -= 10
                        print("Decreased frequency")
                if event.key == py.K_m:
                        if update_freq < update_freq_max:
                            update_freq += 10
                            print("Increased frequency")
                if event.key == py.K_ESCAPE:
                        import main
                        main.pop()
                        isRunning = False
                        
                            

        screen.fill(GREY)
        if first:
            positions = gen(random.randrange(8,20) * GRID_WIDTH)
            first = False
        draw_grid(positions)
        py.display.update()
    py.quit()
    
if __name__ == "__main__":
    play()

