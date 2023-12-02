import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Создание фигуры и осей для рисования ёлки
fig, ax = plt.subplots()

# Рисуем ствол ёлки
trunk = patches.Rectangle((0.45, 0), 0.1, 0.2, linewidth=1, edgecolor='brown', facecolor='brown')
ax.add_patch(trunk)

# Рисуем верхнюю часть ёлки
triangle = patches.Polygon([[0.4, 0.2], [0.6, 0.2], [0.5, 0.5]], linewidth=1, edgecolor='green', facecolor='green')
ax.add_patch(triangle)

# Рисуем среднюю часть ёлки
triangle = patches.Polygon([[0.35, 0.35], [0.65, 0.35], [0.5, 0.65]], linewidth=1, edgecolor='green', facecolor='green')
ax.add_patch(triangle)

# Рисуем нижнюю часть ёлки
triangle = patches.Polygon([[0.3, 0.5], [0.7, 0.5], [0.5, 0.85]], linewidth=1, edgecolor='green', facecolor='green')
ax.add_patch(triangle)

# Настройка осей и удаление рамки
ax.axis('off')
plt.box(False)

if __name__ == '__main__':
# Отображение результата
    plt.show()