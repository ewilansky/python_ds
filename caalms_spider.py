import numpy as np
import pylab as pl
import matplotlib.pyplot as py

class Radar(object):

    def __init__(self, fig, titles, labels, rect=None):
        # ?legend?
        if rect is None:
            rect = [0.05, 0.1, 0.95, 0.7]
            # rect = [0.05, 0.05, 0.95, 0.95]

        self.n = len(titles)
        self.angles = [a if a <=360. else a - 360. for a in np.arange(90, 90+360, 360.0/self.n)]
        self.axes = [fig.add_axes(rect, projection="polar", label="axes%d" % i) 
                        for i in range(self.n)]

        self.ax = self.axes[0]
        # these are the endpoints (CAALMS) spelled-out 
        self.ax.set_thetagrids(self.angles, labels=titles, fontsize=12, weight="bold", color="black")

        for ax in self.axes[1:]:
            ax.patch.set_visible(False)
            ax.grid("off")
            ax.xaxis.set_visible(False)
            self.ax.yaxis.grid(False)

        for ax, angle, label in zip(self.axes, self.angles, labels):
            ax.set_rgrids(range(1, 6), labels=label, angle=angle, fontsize=12)
            ax.spines["polar"].set_visible(False)
            ax.set_ylim(0, 6)  
            ax.xaxis.grid(True,color='black',linestyle='-')

    def plot(self, values, *args, **kw):
        angle = np.deg2rad(np.r_[self.angles, self.angles[0]])
        values = np.r_[values, values[0]]
        self.ax.plot(angle, values, *args, **kw)

# fig = pl.figure(figsize=(20, 20))
fig = pl.figure(1)

titles = ['Culture', 'Automation', 'Architecture', 'LEAN', 'Measures', 'Sharing']

labels = [list("FMIAB"), list("ABCDE")]
# list("FMIAB"), list("FMIAB"), list("FMIAB"), list("FMIAB"), list("FMIAB")]

radar = Radar(fig, titles, labels)
radar.plot([1, 3, 2, 5, 4, 2], "--", lw=1, color="b", alpha=.5, label="PES")
# radar.plot([2.5, 2, 3, 3, 2, 1],"-", lw=1, color="r", alpha=.5, label="CDS-A")
# radar.plot([3, 4, 3, 4, 2, 2, 1, 3, 2], "-", lw=1, color="g", alpha=.5, label="2013")
# radar.plot([4.5, 5, 4, 5, 3, 3, 4, 4, 2], "-", lw=1, color="y", alpha=.5, label="2012")

radar.ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.10),
      fancybox=True, shadow=True, ncol=4)

pl.show()

# fig = py.gcf()
# fig.set_size_inches(6, 10, forward=True)
# fig.savefig('test2png.png', dpi=100, bbox_inches="tight", pad_inches=1)