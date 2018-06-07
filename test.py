import numpy as np
import matplotlib.pyplot as plt

class Radar(object):

    def __init__(self, fig, titles, label, rect=None):
        if rect is None:
            rect = [0.05, 0.15, 0.95, 0.75]

        self.n = len(titles)
        self.angles = [a if a <=360. else a - 360. for a in np.arange(90, 90+360, 360.0/self.n)]
        self.axes = [fig.add_axes(rect, projection="polar", label="axes%d" % i) 
                        for i in range(self.n)]

        self.ax = self.axes[0]
        
        # Show the labels
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

    def decorate_ticks(self, axes):
        for idx, tick in enumerate(axes.xaxis.majorTicks):
            # print(idx, tick.label._text)
            # get the gridline
            gl = tick.gridline
            gl.set_marker('o')
            gl.set_markersize(15)
            if idx == 0:
                gl.set_markerfacecolor('b')
            elif idx == 1:
                gl.set_markerfacecolor('c')
            elif idx == 2:
                gl.set_markerfacecolor('g')
            elif idx == 3:
                gl.set_markerfacecolor('y')
            elif idx == 4:
                gl.set_markerfacecolor('r')
            # this doesn't get used. The center doesn't seem to be different than 5
            else:
                gl.set_markerfacecolor('black')

            if idx == 0 or idx == 3:
                tick.set_pad(10)
            else:
                tick.set_pad(30)

    def plot(self, values, *args, **kw):
        angle = np.deg2rad(np.r_[self.angles, self.angles[0]])
        values = np.r_[values, values[0]]
        self.ax.plot(angle, values, *args, **kw)

fig = plt.figure(1)

titles = ['TG01', 'TG02', 'TG03', 'TG04', 'TG05', 'TG06']
label = list("ABCDE")

radar = Radar(fig, titles, label)
radar.plot([3.75, 3.25, 3.0, 2.75, 4.25, 3.5], "-", linewidth=2, color="b", alpha=.7, label="Data01")
radar.plot([3.25, 2.25, 2.25, 2.25, 1.5, 1.75],"-", linewidth=2, color="r", alpha=.7, label="Data02")

radar.decorate_ticks(radar.ax)

# this avoids clipping the markers below the thetagrid labels
radar.ax.xaxis.grid(clip_on = False)

radar.ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.10),
      fancybox=True, shadow=True, ncol=4)

plt.show()