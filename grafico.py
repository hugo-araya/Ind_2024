import matplotlib.pyplot as plt

x = []
y = []
i = -100
while i <= 100:
    x.append(i)
    y.append(i*i*i)
    i = i + 1
plt.bar(x,y)
plt.show()
