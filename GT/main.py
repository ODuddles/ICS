""""
Owen Duddles 15099261
Narek Wartanian 14787148
This file runs the custom made GUI and initializes neccesary
threads that will run the tournament in the background and will
plot the results in a graph. The GUI is also able to change the parameters
that can be found in parameters.json.

"""
import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QThread, pyqtSignal
from mainui import Ui_MainWindow
from genetic import GenAlgorithm
import battle
import matplotlib
import matplotlib.pyplot as plt
import os
import numpy as np
import strategies.strategies as strats
os.environ["QT_QPA_PLATFORM"] = "xcb"
matplotlib.use('Qt5Agg')


# This is the worker thread that, handles the live plot.
class Worker(QThread):
    finished = pyqtSignal()

    def __init__(self, generations, seed):
        super().__init__()
        self.generations = generations
        self.seed = seed
        self.running = True

    def run(self):
        np.random.seed(self.seed)
        gen = GenAlgorithm()
        for _ in range(self.generations):
            if not self.running:
                break
            gen.run_one_gen()
        self.finished.emit()


# The main GUI window that will load in.
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.start)
        self.ui.pushButton_2.clicked.connect(self.save)
        self.ui.pushButton_3.clicked.connect(self.reset)
        self.ui.pushButton_3.setEnabled(False)

        with open("./parameters/parameters.json", "r") as file:
            x = json.load(file)
        self.ui.spinBox_2.setValue(x["pool_size"])
        self.ui.doubleSpinBox.setValue(x["mutation_factor"])
        a, b = x["payoff"]["00"]
        c, d = x["payoff"]["10"]
        e, f = x["payoff"]["01"]
        g, h = x["payoff"]["11"]
        self.ui.spinBox.setValue(a)
        self.ui.spinBox_4.setValue(b)
        self.ui.spinBox_5.setValue(c)
        self.ui.spinBox_6.setValue(d)
        self.ui.spinBox_8.setValue(e)
        self.ui.spinBox_9.setValue(f)
        self.ui.spinBox_7.setValue(g)
        self.ui.spinBox_10.setValue(h)
        self.ui.spinBox_12.setValue(x["iterationsPerGame"])
        self.generations = self.ui.spinBox_11.value()
        self.seed = self.ui.spinBox_13.value()

    # This is the function that will call all the neccessary,
    # functions to make sure the live plot is plotted correctly.
    def start(self):
        with open("result.txt", "w") as _:
            pass
        self.worker = Worker(self.generations, self.seed)
        self.worker.finished.connect(self.worker.deleteLater)

        self.worker.finished.connect(
            lambda: self.ui.pushButton.setEnabled(True)
        )
        self.worker.finished.connect(
            lambda: self.ui.pushButton_2.setEnabled(True)
        )

        self.worker.finished.connect(
            lambda: self.ui.pushButton_3.setEnabled(False)
        )
        self.worker.finished.connect(self.ui.widget.stop_anim)

        if self.ui.checkBox.isChecked():
            self.worker.finished.connect(self.character_plot)

        if self.ui.checkBox_2.isChecked():
            self.worker.finished.connect(self.strategies_plot)

        self.worker.start()
        self.ui.widget.start_anim()

        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton_3.setEnabled(True)

    # The function that will handle the character plot
    def character_plot(self):
        data = open("top20.txt", "r").read()
        lines = data.split("\n")
        for line in lines:
            if len(line) > 1:
                score, bits = line.split(',')
                formatted = [int(x) for x in format(int(bits), 'b')]
                zeros = formatted.count(0)
                ratio = zeros / len(formatted)
                if ratio > 0.75:
                    color = "green"
                elif ratio >= 0.5:
                    color = "limegreen"
                elif ratio >= 0.25:
                    color = "orange"
                else:
                    color = "red"
                plt.bar(str(bits), int(score), color=color)
                plt.text(str(bits), int(score), score, size=6, ha='center')
        plt.xticks(fontsize=7, rotation=45)
        plt.title(f"Characteristics of the {len(lines) - 1} top evolved strategies.")
        plt.show()

    # The function that will handle the strategies plot.
    def strategies_plot(self):
        data = open("top20.txt", "r").read()
        lines = data.split("\n")
        _, bits = lines[0].split(',')
        diy_strats = [int(bits), strats.always_coop,
                      strats.always_defect,
                      strats.defect_last_two_moves_defect,
                      strats.eye_4_eye,
                      strats.alternate,
                      strats.double_alternate,
                      strats.sneaky_tit4tat,
                      strats.grudge,
                      strats.forgiving_grudge, strats.fair_game,
                      strats.tit4tat]
        resulting_dict = battle.everyone_v_everyone(diy_strats)
        list_from_dict = list(resulting_dict.items())
        results = sorted(list_from_dict, key=lambda x: x[1], reverse=True)
        plt.figure(figsize=(10, 6))
        for result in results:
            try:
                plt.bar(str(result[0].__name__), int(result[1]))
                plt.text(str(result[0].__name__), int(result[1]), result[1], size=8, ha='center')
            except AttributeError:
                plt.bar(str(result[0]), int(result[1]))
                plt.text(str(result[0]), int(result[1]), result[1], size=8, ha='center')
        plt.xticks(fontsize=7, rotation=45)
        plt.title("Strategies plot")
        plt.show()

    # The function that will make sure that all the parameters
    # are saved in parameters.json.
    def save(self):
        with open("./parameters/parameters.json", "r") as f:
            x = json.load(f)
        x["pool_size"] = self.ui.spinBox_2.value()
        x["mutation_factor"] = self.ui.doubleSpinBox.value()
        x["payoff"]["00"] = [self.ui.spinBox.value(), self.ui.spinBox_4.value()]
        x["payoff"]["10"] = [self.ui.spinBox_5.value(), self.ui.spinBox_6.value()]
        x["payoff"]["01"] = [self.ui.spinBox_8.value(), self.ui.spinBox_9.value()]
        x["payoff"]["11"] = [self.ui.spinBox_7.value(), self.ui.spinBox_10.value()]
        x["iterationsPerGame"] = self.ui.spinBox_12.value()
        self.generations = self.ui.spinBox_11.value()
        self.seed = self.ui.spinBox_13.value()
        with open("./parameters/parameters.json", "w") as f:
            json.dump(x, f, indent=2)

    # The function that will handle the resetting of the plot.
    def reset(self):
        if self.worker and self.worker.isRunning():
            self.worker.running = False
            self.worker.quit()
            self.worker.wait()
            self.worker.deleteLater()
            self.worker = None
        self.ui.pushButton_3.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
