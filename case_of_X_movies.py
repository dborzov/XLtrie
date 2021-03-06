import xfast
import matplotlib.pyplot as plt

YEAR_SHIFT = 1950
order = 6


ticks, years = [], []
for year in open('years.txt','rb').readlines():
  ticks.append(year)
  years.append(int(year) - YEAR_SHIFT)


titles = []
for i, title in enumerate(open('result.txt','rb').readlines()):
  titles.append(title[:-1]+' ('+str(years[i] + YEAR_SHIFT)+')')


mytrie = xfast.Xtrie(order)

for year in years:
  mytrie.mark(year)

# mytrie.self_report()
atake = mytrie.visualize()

fig, ax = plt.subplots()
fig.set_size_inches(10,5)
ax.set_frame_on(False)
c = plt.pcolor(atake,cmap=plt.cm.Blues, alpha=0.8,edgecolors='k', linewidths=1)


ax.invert_yaxis()
plt.xticks(rotation=90)

ax = plt.gca()
for t in ax.xaxis.get_major_ticks():
    t.tick1On = False
    t.tick2On = False
for t in ax.yaxis.get_major_ticks():
    t.tick1On = False
    t.tick2On = False

ax.xaxis.set_ticks([float(year)+0.5 for year in years])
ax.xaxis.set_ticklabels(titles, fontsize=10)

plt.tight_layout()
plt.savefig('movies.png')
