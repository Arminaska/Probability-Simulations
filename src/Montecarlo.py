import random
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.animation import FuncAnimation

x = []
y = []

fig,ax = plt.subplots()
ax.set_ylim(0,1)
ax.set_xlim(0,1)
circ = plt.Circle((0.5,0.5),0.5)
#plt.axis('Equal')

ax.add_artist(circ)
scatter = ax.scatter([],[],color = 'red')

#the first component is inside, the last is outside
count = [1,1]

def update(i):
	new_x = random.uniform(0,1)
	new_y = random.uniform(0,1)

	#count total
	count[0] += 1

	#count if inside
	if new_x**2 + new_y**2 < 1:
		count[1] += 1

	x.append(new_x)
	y.append(new_y)

	#plt.text(100,100,'{}'.format(count[1]/count[0]))
	print((count[1]/count[0])*4)

	scatter.set_offsets(np.c_[x,y])
	fig.canvas.draw_idle()
	return scatter

anim = FuncAnimation(fig,update,interval = 100)
plt.show()