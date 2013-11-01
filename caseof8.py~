import xfast
import matplotlib.pyplot as plt

order = 3

mytrie = xfast.Xtrie(order)
years = [1]

for year in years:
  mytrie.mark(year)

# mytrie.self_report()
atake = mytrie.visualize()

fig, ax = plt.subplots()
ax.set_frame_on(False)
c = plt.pcolor(atake,cmap=plt.cm.Blues, alpha=0.8,edgecolors='k', linewidths=4)


ax.invert_yaxis()

ax = plt.gca()
for t in ax.xaxis.get_major_ticks():
    t.tick1On = False
    t.tick2On = False
for t in ax.yaxis.get_major_ticks():
    t.tick1On = False
    t.tick2On = False


plt.savefig('figure.png')