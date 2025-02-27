import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QThread, pyqtSignal
from mainui import Ui_MainWindow
from genetic import GenAlgorithm


class Worker(QThread):
    finished = pyqtSignal()

    def run(self):
        gen = GenAlgorithm()
        for _ in range(50):
            gen.run_one_gen()
        self.finished.emit()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.start)
        self.ui.pushButton_2.clicked.connect(self.save)

    def start(self):
        open("result.txt", "w")
        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()

        self.ui.widget.start_anim()
        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton_2.setEnabled(False)

        self.thread.finished.connect(
            lambda: self.ui.pushButton.setEnabled(True)
        )
        self.thread.finished.connect(
            lambda: self.ui.pushButton_2.setEnabled(True)
        )
        self.ui.widget.stop_anim()

    def save(self):
        with open("./parameters/parameters.json", "r") as f:
            x = json.load(f)
        x["pool_size"] = self.ui.spinBox_2.value()
        x["mutation_factor"] = self.ui.spinBox_3.value()
        x["payoff"]["00"] = [self.ui.spinBox.value(), self.ui.spinBox_4.value()]
        x["payoff"]["10"] = [self.ui.spinBox_5.value(), self.ui.spinBox_6.value()]
        x["payoff"]["01"] = [self.ui.spinBox_8.value(), self.ui.spinBox_9.value()]
        x["payoff"]["11"] = [self.ui.spinBox_7.value(), self.ui.spinBox_10.value()]
        with open("./parameters/parameters.json", "w") as f:
            json.dump(x, f, indent=2)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
