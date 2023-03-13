import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt

# данные для диаграммы тип красивый
# labels = ['Apples', 'Oranges', 'Bananas', 'Pears']
# sizes = [25, 30, 20, 15]
# colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
#
# # создаем кольцевую диаграмму
# fig, ax = plt.subplots()
# ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, pctdistance=0.85,
#        wedgeprops=dict(width=0.7, edgecolor='w'))
#
# # добавляем текст в центр кольца
# centre_circle = plt.Circle((0, 0), 0.70, fc='white')
# fig.gca().add_artist(centre_circle)
# plt.text(0, 0, 'Fruit', ha='center', va='center', fontsize=20)
#
# # настраиваем стиль
# ax.axis('equal')
# plt.tight_layout()
# plt.show()


labels = ['A', 'B', 'C', 'D', 'E']
sizes = [15, 30, 25, 10, 20]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'orange']
explode = (0.01, 0.01, 0.01, 0.01, 0.01) # выделение сегмента

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, colors=colors, #labels=labels,
        autopct='%1.1f%%', startangle=90, pctdistance=1.25,# установка удаления от кольца
        wedgeprops={'width': 0.5})  # установка ширины кольца

# добавление текста с указанием процентного соотношения
# for i, label in enumerate(labels):
#     angle = (sum(sizes[:i]) + sizes[i]/2) / sum(sizes) * 360
#     x = 0.85 * np.cos(np.deg2rad(angle))
#     y = 0.85 * np.sin(np.deg2rad(angle))
    # if x > 0:
    #     ax1.annotate('{:.1f}%'.format(sizes[i]/sum(sizes)*100), (x, y), ha='left', va='center', fontsize=12)
    # else:
    #     ax1.annotate('{:.1f}%'.format(sizes[i]/sum(sizes)*100), (x, y), ha='right', va='center', fontsize=12)

ax1.axis('equal')
plt.title('Title')
plt.show()