import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Konstanta
CELL_SIZE = 64
WALL_COLOR = (128, 128, 128)      # Abu-abu
FLOOR_COLOR = (255, 255, 255)     # Putih
STORAGE_COLOR = (255, 0, 0)       # Merah
BOX_COLOR = (139, 69, 19)         # Coklat
PLAYER_COLOR = (0, 0, 255)        # Biru

# Data level
level_data = [
    "##############",
    "#            #",
    "#   #        #",
    "#   .  #  $  #",
    "#    @     ###",
    "##############",
]

def parse_level(data):
    height = len(data)
    width = max(len(row) for row in data)
    
    walls = [[False for _ in range(width)] for _ in range(height)]
    storage = [[False for _ in range(width)] for _ in range(height)]
    boxes = []
    player_pos = (0, 0)
    
    for y in range(height):
        row = data[y].ljust(width)
        for x in range(width):
            char = row[x]
            if char == '#':
                walls[y][x] = True
            elif char == '.':
                storage[y][x] = True
            elif char == '@':
                player_pos = (x, y)
            elif char == '$':
                boxes.append((x, y))
            elif char == '*':
                boxes.append((x, y))
                storage[y][x] = True
            elif char == '+':
                player_pos = (x, y)
                storage[y][x] = True
    return walls, storage, boxes, player_pos

# Parse level
walls, storage, boxes, player_pos = parse_level(level_data)
width = len(walls[0])
height = len(walls)

# Fungsi gerakan
def move(dx, dy):
    global player_pos, boxes
    px, py = player_pos
    nx = px + dx
    ny = py + dy

    if nx < 0 or nx >= width or ny < 0 or ny >= height:
        return

    if walls[ny][nx]:
        return

    if (nx, ny) in boxes:
        nnx = nx + dx
        nny = ny + dy
        
        if nnx < 0 or nnx >= width or nny < 0 or nny >= height:
            return
            
        if walls[nny][nnx] or (nnx, nny) in boxes:
            return
            
        boxes.remove((nx, ny))
        boxes.append((nnx, nny))
    
    player_pos = (nx, ny)

# Fungsi cek kemenangan
def is_victory():
    for (x, y) in boxes:
        if not storage[y][x]:
            return False
    return True

# Setup display
screen = pygame.display.set_mode((width * CELL_SIZE, height * CELL_SIZE))
pygame.display.set_caption("Sokoban")
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move(0, -1)
            elif event.key == pygame.K_DOWN:
                move(0, 1)
            elif event.key == pygame.K_LEFT:
                move(-1, 0)
            elif event.key == pygame.K_RIGHT:
                move(1, 0)
    
    # Gambar grid
    screen.fill((0, 0, 0))
    
    for y in range(height):
        for x in range(width):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            
            # Gambar lantai/dinding
            if walls[y][x]:
                pygame.draw.rect(screen, WALL_COLOR, rect)
            else:
                pygame.draw.rect(screen, FLOOR_COLOR, rect)
                
                # Gambar titik penyimpanan
                if storage[y][x]:
                    center = (x * CELL_SIZE + CELL_SIZE//2, 
                             y * CELL_SIZE + CELL_SIZE//2)
                    pygame.draw.circle(screen, STORAGE_COLOR, center, CELL_SIZE//4)
    
    # Gambar kotak
    for (x, y) in boxes:
        box_rect = pygame.Rect(
            x * CELL_SIZE + CELL_SIZE//4,
            y * CELL_SIZE + CELL_SIZE//4,
            CELL_SIZE//2,
            CELL_SIZE//2
        )
        pygame.draw.rect(screen, BOX_COLOR, box_rect)
    
    # Gambar pemain
    px, py = player_pos
    player_center = (
        px * CELL_SIZE + CELL_SIZE//2,
        py * CELL_SIZE + CELL_SIZE//2
    )
    pygame.draw.circle(screen, PLAYER_COLOR, player_center, CELL_SIZE//3)
    
    # Cek kemenangan
    if is_victory():
        font = pygame.font.Font(None, 74)
        text = font.render('MENANG!', True, (0, 255, 0))
        text_rect = text.get_rect(center=(width*CELL_SIZE//2, height*CELL_SIZE//2))
        screen.blit(text, text_rect)
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()