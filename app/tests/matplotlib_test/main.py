import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.use('Agg')

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(range(10))
fig.savefig('figure.png')

print(range(10))