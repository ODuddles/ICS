""""
Owen Duddles 15099261
Narek Wartanian 14787148
This file contains the logic that handles the plotting
of the matplotlib figure in the GUI. The x-axis shows the
current generation, while the y-axis shows us the payoff score.
Note that only the highest scoring random strategy will be plot.

"""
from PyQt5.QtWidgets import QWidget, QVBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvas
import matplotlib.animation as animation
from matplotlib.figure import Figure


# This is the main class that will initalize and actually
# plot the live plot.
class mplwidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.running = 0
        self.canvas = FigureCanvas(Figure())
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.canvas.axes.set_xlabel("Generation")
        self.canvas.axes.set_ylabel("Payoff")

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        self.setLayout(vertical_layout)

    # Starts the animation
    def start_anim(self):
        self.anim = animation.FuncAnimation(self.canvas.figure, self.animate, interval=100)
        self.canvas.draw()

    # Stops the animation
    def stop_anim(self):
        self.anim = None

    # The function that will be called everytime, to
    # make the plot live.
    def animate(self, i):
        graph_data = open('./result.txt', 'r').read()
        lines = graph_data.split('\n')
        xs = []
        ys = []
        for line in lines:
            if len(line) > 1:
                x, y = line.split(',')
                xs.append(float(x))
                ys.append(float(y))

        self.canvas.axes.clear()
        self.canvas.axes.plot(xs, ys, label="Random (Best version)")
        self.canvas.axes.legend()
        self.canvas.axes.set_xlabel("Generation")
        self.canvas.axes.set_ylabel("Payoff")
        self.canvas.draw()
