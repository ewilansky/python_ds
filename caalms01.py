# Plots a radar chart.

from math import pi
# import matplotlib as mpl
import matplotlib.pyplot as plt
# import seaborn as sns # improves plot aesthetics

# fig = plt.figure(figsize=(8,8))
fig = plt.figure(figsize=(6,4))
# R styling for the plot is 'ggplot'
# plt.style.use('seaborn-white')
# show available style
# print(plt.style.available)


# Set data
cat = ['Culture', 'Automation', 'Architecture', 'LEAN', 'Measure', 'Sharing']
cdsa_values = [80, 60, 80, 75, 60, 25]
pes_values = [65, 45, 45, 45, 30, 35]

# of items in category array
N = len(cat)
# position of x axis categories on the circle
x_as = [n / float(N) * 2 * pi for n in range(N)]

# Because our chart will be circular, append a copy of the first 
# value of each list at the end of each list with data
cdsa_values += cdsa_values[:1]
pes_values += pes_values[:1]

x_as += x_as[:1]

# Set color of axes
plt.rc('axes', linewidth=0, edgecolor="#ffffff")

# Create polar plot
# ax = fig.add_subplot(111, projection='polar')
# ax1 = fig.add_subplot(111, projection='polar')

rect = [0.05, 0.1, 0.95, 0.7]
ax = fig.add_axes(rect, projection='polar')
ax1 = fig.add_axes(rect, projection='polar')

# Set clockwise rotation. That is:
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)

#ax.set_title("CAALMS Capability Diagram", va='top')

plt.Circle.visible = False

# Set position of y-labels
# ax.set_rlabel_position(0)

# Set color and linestyle of grid
ax.xaxis.grid(True, color="#888888", linestyle='solid', linewidth=0.5)
# ax.yaxis.grid(True, color="#888888", linestyle='solid', linewidth=1.0)
# IMPORTANT, TURNING OFF TO SEE AFFECT TO THETAGRID (NO AFFECT )
ax.yaxis.grid(False)

# ax1.grid(False)
# ax.grid(False)

caalms = ['F', 'M', 'I', 'A', 'B']
positions = [20, 40, 60, 80, 100]

# this is the general idea for annotating the grid...
# ax.annotate(s='F', xy=[1,20])
# ax.annotate(s = 'M', xy=[1,40])

# turning internal iterator into a list comprehension
for p in x_as:
   [ax.annotate(s=caalms[n], xy=[p - 1,positions[n]]) for n in range(0,5)]

# ax.annotate("", xy=(1, 1), xytext=(0, 0), arrowprops=dict(arrowstyle="->"))

# set the locations and labels of the radial gridlines and labels
# lines, labels = plt.thetagrids()
# lines, labels = plt.thetagrids(range(0,360,6), ('Culture', 'Automation', 'Architecture','LEAN', 'Measures', 'Sharing') )

# Set number of radial axes and remove label
plt.xticks(x_as[:-1], [])

# Disable ytick labels
ax.set_yticklabels([])
# plt.yticks([20, 40, 60, 80, 100], ["F", "M", "I", "A", "B"])

# Plot data
ax.plot(x_as, cdsa_values, linewidth=2, linestyle='solid', color='red', zorder=3)
ax1.plot(x_as, pes_values, linewidth=2, linestyle='solid', color='blue', zorder=2)

# Fill area
# alpha is transparency 
ax.fill(x_as, cdsa_values, color='b', alpha=0)
ax1.fill(x_as, pes_values, color='r', alpha=0)

# Set axes limits
plt.ylim(0, 100)


# Draw xtick labels to make sure they fit properly
# these are the CAALMS labels on the periphery of the circle
for i in range(N):
    angle_rad = i / float(N) * 2 * pi

    if angle_rad == 0:
        ha, distance_ax = "center", 10
    elif 0 < angle_rad < pi:
        ha, distance_ax = "left", 1
    elif angle_rad == pi:
        ha, distance_ax = "center", 1
    else:
        ha, distance_ax = "right", 1

    ax.text(angle_rad, 110 + distance_ax, cat[i], size=12, horizontalalignment=ha, verticalalignment="top")
    
# Show polar plot
plt.show()