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


class Worker(QThread):
    finished = pyqtSignal()

    def __init__(self, generations):
        super().__init__()
        self.generations = generations

    def run(self):
        gen = GenAlgorithm()
        for _ in range(self.generations):
            gen.run_one_gen()
        self.finished.emit()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.start)
        self.ui.pushButton_2.clicked.connect(self.save)

        with open("./parameters/parameters.json", "r") as file:
            x = json.load(file)
        self.ui.spinBox_2.setValue(x["pool_size"])
        self.ui.spinBox_3.setValue(x["mutation_factor"])
        a, b = x["payoff"]["00"]
        c, d = x["payoff"]["10"]
        e, f = x["payoff"]["01"]
        g, h = x["payoff"]["01"]
        self.ui.spinBox.setValue(a)
        self.ui.spinBox_4.setValue(b)
        self.ui.spinBox_5.setValue(c)
        self.ui.spinBox_6.setValue(d)
        self.ui.spinBox_8.setValue(e)
        self.ui.spinBox_9.setValue(f)
        self.ui.spinBox_7.setValue(g)
        self.ui.spinBox_10.setValue(h)
        self.generations = self.ui.spinBox_11.value()

    def start(self):
        with open("result.txt", "w") as _:
            pass
        self.worker = Worker(self.generations)
        self.worker.finished.connect(self.worker.deleteLater)

        self.worker.finished.connect(
            lambda: self.ui.pushButton.setEnabled(True)
        )
        self.worker.finished.connect(
            lambda: self.ui.pushButton_2.setEnabled(True)
        )
        self.worker.finished.connect(self.ui.widget.stop_anim)

        self.worker.start()
        self.ui.widget.start_anim()

        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton_2.setEnabled(False)

    def save(self):
        with open("./parameters/parameters.json", "r") as f:
            x = json.load(f)
        x["pool_size"] = self.ui.spinBox_2.value()
        x["mutation_factor"] = self.ui.spinBox_3.value()
        x["payoff"]["00"] = [self.ui.spinBox.value(), self.ui.spinBox_4.value()]
        x["payoff"]["10"] = [self.ui.spinBox_5.value(), self.ui.spinBox_6.value()]
        x["payoff"]["01"] = [self.ui.spinBox_8.value(), self.ui.spinBox_9.value()]
        x["payoff"]["11"] = [self.ui.spinBox_7.value(), self.ui.spinBox_10.value()]
        self.generations = self.ui.spinBox_11.value()
        with open("./parameters/parameters.json", "w") as f:
            json.dump(x, f, indent=2)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
