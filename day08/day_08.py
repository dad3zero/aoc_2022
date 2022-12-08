
from utils import io
from pprint import pprint

def get_viewable_left_2_right(tree_row):
    max_height = -1
    viewable_row = []

    for tree_height in tree_row:
        tree_height = int(tree_height)
        if tree_height > max_height:
            max_height = tree_height
            viewable_row.append(True)
        else:
            viewable_row.append(False)

    return viewable_row

def get_viewable_right_2_left(tree_row):
    viewable_reversed_row = get_viewable_left_2_right(tree_row[::-1])
    viewable_reversed_row.reverse()
    return viewable_reversed_row

def get_viewable_on_row(tree_row):
    viewable_l2r = get_viewable_left_2_right(tree_row)
    viewable_r2l = get_viewable_right_2_left(tree_row)

    return [viewable1 or viewable2
            for viewable1, viewable2 in zip(viewable_l2r, viewable_r2l)]

def update_viewable_on_column(tree_matrix, visibility_matrix):

    for column_index in range(len(tree_matrix[0])):
        column = [tree_height[column_index] for tree_height in tree_matrix]
        viewable_column = get_viewable_on_row(column)

        for element_index, is_viewable in enumerate(viewable_column):
            visibility_matrix[element_index][column_index] = visibility_matrix[element_index][column_index] or is_viewable

def count_visible_trees(visibility_matrix):
    visibles = 0
    for row in visibility_matrix:
        for visibility_heigth in row:
            visibles += visibility_heigth

    return visibles

def get_view_score(x, y, tree_grid):
    tree_height = tree_grid[x][y]
    upscore = 0
    while True:
        upscore += 1
        try:
            next_tree = tree_grid[x + upscore][y]
        except IndexError:
            upscore -=1
            break

        if next_tree >= tree_height:
            break

    downscore = 0
    while True:
        downscore += 1
        try:
            next_tree = tree_grid[x - downscore][y]
        except IndexError:
            downscore -= 1
            break

        if next_tree >= tree_height or x - downscore == 0:
            break

    rightscore = 0
    while True:
        rightscore += 1
        try:
            next_tree = tree_grid[x][y + rightscore]
        except IndexError:
            rightscore -= 1
            break

        if next_tree >= tree_height:
            break

    leftscore = 0
    while True:
        leftscore += 1
        try:
            next_tree = tree_grid[x][y - leftscore]
        except IndexError:
            leftscore -= 1
            break

        if next_tree >= tree_height or y - leftscore == 0:
            break

    return rightscore * leftscore * upscore * downscore

def get_max_score(tree_grid):
    max_value = 0
    for tree_row_index in range(len(tree_grid)):
        for tree_column_index in range(len(tree_grid[0])):
            tree_score = get_view_score(tree_row_index, tree_column_index, tree_grid)
            max_value = max(max_value, tree_score)

    return max_value



if __name__ == "__main__":
    tree_grid = []
    input_flow = io.load_game_input()
    for line in input_flow:
        tree_grid.append(line)

    pprint(tree_grid)

    visibility_matrix = [get_viewable_on_row(tree_row) for tree_row in tree_grid]
    update_viewable_on_column(tree_grid, visibility_matrix)
    print(visibility_matrix)
    print(count_visible_trees(visibility_matrix))

    print(get_max_score(tree_grid))

