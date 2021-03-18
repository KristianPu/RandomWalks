#2D
import random
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')
x_val = [0]
y_val = [0]

def animate(i):
    
    data = [-1, 0, 1]
    x = x_val[-1] + random.choice(data)
    y = y_val[-1] + random.choice(data)
    
    if x == x_val[-1] and y == y_val[-1]:
        xy = [x_val, y_val]
        data2 = [-1, 1]
        rb = random.choice(xy)
        rb.append(rb[-1] + random.choice(data2))
        if len(x_val) > len(y_val):
            y_val.append(y)
        else:
            x_val.append(x)
            
    x_val.append(x)
    y_val.append(y)
    
    plt.cla()
    plt.plot(x_val, y_val, linewidth = 2, label = 'Random Walk 1')
    plt.legend(loc = 'upper right')
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval = 1000)

plt.tight_layout()
plt.show()
