grid_pos = (  # left, top
    (12, 12),
    (150, 12),
    (288, 12),
    (12, 150),
    (150, 150),
    (288, 150),
    (12, 288),
    (150, 288),
    (288, 288)
)

winning_combos = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
)

window_size = 426
square_size = 126
mark_size = 100
size_margin = (square_size - mark_size) / 2

x_positions = []
o_positions = []
all_positions = []
