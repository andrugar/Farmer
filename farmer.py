n, m = [int(i) for i in input().split()]
field = []
for i in range(m):
    field.append(list(map(int, input().split())))

num_of_region = 2 # начнем считать регионы с 2, тк 0 и 1 заняты

def neighboring_cells(i, j):
    for di in range(-1, 2):
        for dj in range(-1, 2):
            y = i + di
            x = j + dj
            if 0 <= y < m and 0 <= x < n and field[y][x] == 1:
                field[y][x] = num_of_region
                neighboring_cells(y, x)
    
for i in range(m):
    for j in range(n):
        if field[i][j] == 1:
            neighboring_cells(i, j)
            num_of_region += 1

regions = []

for num in range(2, num_of_region):
    top_edge = 0
    bottom_edge = 0
    left_edge = 0
    right_edge = 0
    first_one = True
    for i in range(m):
        for j in range(n):
            if field[i][j] == num:
                if first_one:
                    top_edge = i
                    bottom_edge = i
                    left_edge = j
                    right_edge = j
                    first_one = False
                else:
                    top_edge = min(i, top_edge)
                    bottom_edge = max(i, bottom_edge)
                    left_edge = min(j, left_edge)
                    right_edge = max(j, right_edge)
    s = (bottom_edge - top_edge + 1) * (right_edge - left_edge + 1)
    fertile_plots = 0
    for i in range(top_edge, bottom_edge + 1):
        for j in range(left_edge, right_edge +1):
            if field[i][j] > 0:
                fertile_plots += 1
    regions.append([s, fertile_plots / s])

max_fertility = 0
max_s = 0

for i in range(len(regions)):
    if regions[1][i] > max_fertility:
        max_fertility = regions[1][i]

for i in range(len(regions)):
    if regions[1][i] == max_fertility and regions[0][i] > max_s:
        max_s= regions[0][i]

print(max_s)

'''
for i in range(m):
    for j in range(n):
        print('| ', field[i][j], end = ' ')
    print()
print(regions)'''
