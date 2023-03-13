import matplotlib.pyplot as plt
import numpy as np

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