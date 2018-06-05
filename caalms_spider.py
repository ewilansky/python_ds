import numpy as np
import pylab as pl
import matplotlib.pyplot as py

class Radar(object):

    def __init__(self, fig, titles, label, rect=None):
        if rect is None:
            # layout area for polar plot - axes postioning left, bottom, width, height in fractions of figure width and height
            rect = [0.05, 0.15, 0.95, 0.75]

        self.n = len(titles)
        self.angles = [a if a <=360. else a - 360. for a in np.arange(90, 90+360, 360.0/self.n)]
        self.axes = [fig.add_axes(rect, projection="polar", label="axes%d" % i) 
                        for i in range(self.n)]

        self.ax = self.axes[0]
        # these are the endpoints for CAALMS spelled-out 
        self.ax.set_thetagrids(self.angles, labels=titles, fontsize=14, weight="bold", color="black")

        for ax in self.axes[1:]:
            ax.patch.set_visible(False)
            ax.grid(False)
            ax.xaxis.set_visible(False)
            self.ax.yaxis.grid(False)

        for ax, angle in zip(self.axes, self.angles):
            ax.set_rgrids(range(1, 6), labels=label, angle=angle, fontsize=12)
            # hide outer spine (circle)
            ax.spines["polar"].set_visible(False)
            ax.set_ylim(0, 6)  
            ax.xaxis.grid(True, color='black', linestyle='-')
            # doesn't do anything...
            # ax.tick_params(direction='inout', length=20, width=5, color='r', which='both')
            ticks = ax.xaxis.majorTicks
            for tick in ticks:
                tick.tick1On = True
                tick.tick2On = True
                # tick.set_visible = True
                # tick.set_size_inches = 1
                # tick.inout = True
               # tick.length=20
                # tick.color='r'
                # tick.width=5
                tick1line = tick.tick1line
                tick2line = tick.tick2line
                # tick1line.set_rgrids()
                tick1line.lineStyles = '-'
                tick1line.marker = 'o'
                tick1line.filled_markers = 'o'
                tick1line.drawStyles = 'steps'
                tick1line.markevery = 1        

    def plot(self, values, *args, **kw):
        angle = np.deg2rad(np.r_[self.angles, self.angles[0]])
        values = np.r_[values, values[0]]
        self.ax.plot(angle, values, *args, **kw)

fig = pl.figure(1)

titles = ['Culture', 'Automation', 'Architecture', 'LEAN', 'Measures', 'Sharing']
label = list("FMIAB")

radar = Radar(fig, titles, label)
radar.plot([3.75, 3.25, 3.0, 2.75, 4.25, 3.5], "-", linewidth=2, color="b", alpha=.7, label="PES")
radar.plot([3.25, 2.25, 2.25, 2.25, 1.5, 1.75],"-", linewidth=2, color="r", alpha=.7, label="CDS-A")

radar.ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.10),
      fancybox=True, shadow=True, ncol=4)

pl.show()

# for saving to file (convenience for inserting into pptx)
# fig = py.gcf()
# fig.set_size_inches(6, 10, forward=True)
# fig.savefig('CAALMS.png', dpi=100, bbox_inches="tight", pad_inches=1)