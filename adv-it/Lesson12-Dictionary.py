enemy = {
        'loc_x': 70,
        'loc_y': 50,
        'color': "green",
        'health': 100,
        'name': "Mudillo",
        'image' : ['image1.jpg', 'image2.jpg', 'image1.jpg']
}

all_enemies = [] #задаем пустой массив

for x in range(0, 10):          #добавляем в массив 10 словарей
        all_enemies.append(enemy.copy())


for ene in all_enemies:
        print(ene)
print("=====================================")
all_enemies[5]['health'] = 30
all_enemies[8]['name'] = "Kozel"
all_enemies[2]['loc_x'] += 10
for ene in all_enemies:
        print(ene)
