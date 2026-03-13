import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Data points
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

fig, ax = plt.subplots()

ax.set_xlim(0, 6)
ax.set_ylim(0, 35)

ax.set_xlabel("X values (Independent Variable)")
ax.set_ylabel("Y values (Dependent Variable)")
ax.set_title("X-Y Axis Data Plot")
ax.grid(True)

line, = ax.plot([], [], marker='o')

def update(frame):
    line.set_data(x[:frame], y[:frame])
    return line,

ani = animation.FuncAnimation(
    fig,
    update,
    frames=len(x)+1,
    interval=1000,
    repeat=False
)

plt.show()