import numpy as np
# import pylab as pl
import matplotlib.pyplot as plt
from matplotlib import rcParams

class Radar(object):

    def __init__(self, fig, titles, label, rect=None):
        if rect is None:
            # layout area for polar plot - axes postioning left, bottom, width, height in fractions of figure width and height
            rect = [0.05, 0.15, 0.85, 0.75]

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

            # draw a line on the y axis at each label
            ax.tick_params(axis='y', pad=0, left=True, length=6, width=1, direction='inout')
            # adjust positioning of theta labels
            # ax.tick_params(axis='x', pad=5)     
            
    def decorate_ticks(self, axes):
        for idx, tick in enumerate(axes.xaxis.majorTicks):
            # print(idx, tick.label._text)
            # get the gridline
            gl = tick.gridline
            gl.set_marker('o')
            gl.set_markersize(30)
            if idx == 0:
                gl.set_markerfacecolor('#003399')
            elif idx == 1:
                gl.set_markerfacecolor('#336666')
            elif idx == 2:
                gl.set_markerfacecolor('#336699')
            elif idx == 3:
                gl.set_markerfacecolor('#CC3333')
            elif idx == 4:
                gl.set_markerfacecolor('#CC9933')
            # this doesn't get used. The center doesn't seem to be different than 5
            else:
                gl.set_markerfacecolor('#CC0033')

            if idx == 0 or idx == 3:
                tick.set_pad(15)
            else:
                tick.set_pad(35)


    def plot(self, values, *args, **kw):
        angle = np.deg2rad(np.r_[self.angles, self.angles[0]])
        values = np.r_[values, values[0]]
        self.ax.plot(angle, values, *args, **kw)


titles = ['Culture', 'Sharing', 'Measures', 'LEAN', 'Architecture', 'Automation']
label = list("FMIAB")

# Adding frameon False allows for seeing the edge of the figure.
fig = plt.figure(figsize=(7,7), frameon=True)

radar = Radar(fig, titles, label)
radar.plot([3.75, 3.5, 4.25, 2.75, 3.0, 3.25], "-", linewidth=2, color="b", alpha=.7, label="PES")
radar.plot([3.25, 1.75, 1.5, 2.25, 2.25, 2.25],"-", linewidth=2, color="r", alpha=.7, label="CDS-A")

radar.decorate_ticks(radar.ax)

# this is doing the trick!
radar.ax.xaxis.grid(clip_on = False)

radar.ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.10),
      fancybox=True, shadow=True, ncol=4)

# plt.gcf().subplots_adjust(bottom=0.55)
# plt.tight_layout()
# print(rcParams.keys())

plt.show()

# for saving to file (convenience for inserting into pptx)
# fig = py.gcf()
# fig.set_size_inches(6, 10, forward=True)
# fig.savefig('CAALMS.png', dpi=100, bbox_inches="tight", pad_inches=1)