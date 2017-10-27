import pygal
import random
frequencies = []
for i in range(6):
    frequencies.append(random.randint(1, 100))

hist = pygal.Bar()
hist.title = 'xxd'
hist.x_labels = [str(i) for i in range(1, 7)]
hist._y_title = 'result'
hist._x_title = 'frequency'
hist.add('D6', frequencies)
hist.render_to_file('xxfjsh.svg')