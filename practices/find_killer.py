import random

row1 = ['🌫', '🌫', '🌫', '🌫', '🌫']
row2 = ['🌫', '🌫', '🌫', '🌫', '🌫']
row3 = ['🌫', '🌫', '🌫', '🌫', '🌫']
row4 = ['🌫', '🌫', '🌫', '🌫', '🌫']
row5 = ['🌫', '🌫', '🌫', '🌫', '🌫']

map = [row1, row2, row3, row4, row5]
# print_map(map)
print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n")

killer = '🥷'
win = '⭕️'
lose = '❌'

random_pos_row = random.randint(0, 4)
random_pos_col = random.randint(0, 4)
map[random_pos_row][random_pos_row] = killer

pos = input("Please input the row and the column you choose, for example 24, it means row 2, column 4.")
row = int(pos[0]) - 1
col = int(pos[1]) - 1

if map[row][col] == '🥷':
    map[row][col] = win
else:
    map[row][col] = lose

for row in map:
    print(f"{row}\n")
