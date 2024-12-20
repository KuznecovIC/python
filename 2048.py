import pygame
import random

pygame.init()

# отображение игры
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 4
TITLE_SIZE = WIDTH // GRID_SIZE
MARGIN = 5
FPS = 120
BACKGROUND_COLOR = (187, 173, 160)
EMPTY_TITLE_COLOR = (205, 193, 180)

# Список цветов кубиков
COLORS = {
    0: EMPTY_TITLE_COLOR, 
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 196, 63),
    2048: (237, 194, 46),
}

# текст и т д
TEXT_COLOR = (119, 110, 101)
FONT = pygame.font.Font(None, 40)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")
clock = pygame.time.Clock()

# начало функций
def draw_grid(grid, positions):
    screen.fill(BACKGROUND_COLOR)
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            value = grid[row][col]
            color = COLORS.get(value, (60, 60, 60))
            x, y = positions[row][col]
            rect = pygame.Rect(x, y, TITLE_SIZE - MARGIN * 2, TITLE_SIZE - MARGIN * 2)
            pygame.draw.rect(screen, color, rect)
            if value != 0:
                text_surface = FONT.render(str(value), True, TEXT_COLOR if value < 8 else (255, 255, 255))
                text_rect = text_surface.get_rect(center=rect.center)
                screen.blit(text_surface, text_rect)

# Конец 1 функции, начало 2

def init_grid():
    grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    add_new_title(grid)
    add_new_title(grid)
    return grid

# Конец 2 функции, начало 3

def add_new_title(grid):
    empty_titles = [(r, c) for r in range(GRID_SIZE) for c in range(GRID_SIZE) if grid[r][c] == 0]
    if empty_titles:
        row, col = random.choice(empty_titles)
        grid[row][col] = 2 if random.random() < 0.9 else 4

# Конец 3 функции, начало 4

def slide_and_merge_row(row):
    new_row = [num for num in row if num != 0]
    for i in range(len(new_row) - 1):
        if new_row[i] == new_row[i + 1]:
            new_row[i] *= 2
            new_row[i + 1] = 0
    new_row = [num for num in new_row if num != 0]
    return new_row + [0] * (GRID_SIZE - len(new_row))

# Конец 4 функции, начало 5

def move_grid(grid, direction):
    if direction == "left":
        return [slide_and_merge_row(row) for row in grid]
    elif direction == "right":
        return [slide_and_merge_row(row[::-1])[::-1] for row in grid]
    elif direction == "up":
        transposed = list(zip(*grid))
        moved = [slide_and_merge_row(list(row)) for row in transposed]
        return [list(row) for row in zip(*moved)]
    elif direction == "down":
        transposed = list(zip(*grid))
        moved = [slide_and_merge_row(list(row)[::-1])[::-1] for row in transposed]
        return [list(row) for row in zip(*moved)]

# Конец 5 функции, начало 6

def check_game_over(grid):
    for row in grid:
        if 0 in row:
            return False
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            if (c + 1 < GRID_SIZE and grid[r][c] == grid[r][c + 1]) or (r + 1 < GRID_SIZE and grid[r][c] == grid[r + 1][c]):
                return False
    return True

# Конец 6 функции, начало 7

def generate_target_positions(grid):
    return [[(col * TITLE_SIZE + MARGIN, row * TITLE_SIZE + MARGIN) for col in range(GRID_SIZE)] for row in range(GRID_SIZE)]

# Конец 7 функции, начало 8

def main():
    grid = init_grid()
    positions = generate_target_positions(grid)
    running = True
    game_over = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and not game_over:
                direction_map = {
                    pygame.K_LEFT: "left",
                    pygame.K_RIGHT: "right",
                    pygame.K_UP: "up",
                    pygame.K_DOWN: "down",
                }
                if event.key in direction_map:
                    direction = direction_map[event.key]
                    new_grid = move_grid(grid, direction)

                    if new_grid != grid:
                        grid = new_grid
                        add_new_title(grid)

                if check_game_over(grid):
                    game_over = True

        draw_grid(grid, positions)

        if game_over:
            text_surface = FONT.render("Game Over", True, (255, 0, 0))
            text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(text_surface, text_rect)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

main()