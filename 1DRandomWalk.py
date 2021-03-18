#1D
import random
from matplotlib import pyplot as plt

x = [] 
y = []

lsx = [] # last step cord x
lsy = [] # last step cord y

walks = [] # inputs are appended here

def RandomNumber(n):
    l = [-1,1]
    RN = []
    e = 0
    for i in range(n+1):
        RN.append(random.choice(l))
    for m in RN:
        e += m
        x.append(e)
        y.append(0)
    print(sum(RN))
    lsx.append(x[-1])
    lsy.append(y[-1])

while True:
    k = int(input("Insert number of steps for 1D Random Walk and 0 to stop: "))
    if k == 0:
        break
    else:
        walks.append(k)

for i in walks:
    RandomNumber(i)

 
plt.scatter(x[:-1], y[:-1], label = "Step", color = 'k')
plt.scatter(lsx, lsy, label = "Final Step", color = 'g')
plt.xlabel("Places Stepped On")
plt.ylabel("Y")
plt.title("1D Random Walk")
plt.legend()
plt.show()

    
