# EXAMPLE SCRIPT TO VISUALISE COLLECTED PRESSURE DATA

# Tarmo Tanilsoo, 2022

import datetime
from matplotlib import pyplot as plt
import matplotlib.dates as mdates

x = []
y = []

#Read the lines from the text file and populate the axis
with open("tonga/1642377314.85_1642436915.35_500.csv", "r") as d:
    data = d.readlines()
    for row in data:
        columns = row.strip().split(",")
        DT = datetime.datetime.utcfromtimestamp(float(columns[0]))
        pressure = float(columns[1])
        x.append(DT)
        y.append(pressure)



fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(211)
ax.plot(x,y, lw=1)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M')) #Set time format of X axis

plt.xlabel("Time (UTC)")
plt.ylabel("Local air pressure")
plt.title("Laguja, Estonia")
plt.xlim(x[0],x[-1]) #Make sure there are no blanks at the left and right edges
plt.grid()
ax2 = fig.add_subplot(212)
plt.specgram(y, 120 , Fs = 2, detrend="linear", noverlap=60, vmin=-45, vmax=-15)
plt.ylabel("Frequency (Hz)")
plt.xlabel("Sample number")
plt.savefig("example_plot.png")

