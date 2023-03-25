import sys
from PyQt5.QtWidgets import QApplication, QWidget,QHBoxLayout,QDialog
from PyQt5.QtWidgets import QVBoxLayout, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer, QDateTime, Qt


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.b()
        label = QLabel("DENEME",self)
    def b(self):
        ts = QDialog()
        layout = QHBoxLayout()
        layout2 = QHBoxLayout()

        font = QFont('Arial', 80, QFont.Bold)


        self.gun = QLabel()
        self.gun.setAlignment(Qt.AlignCenter)
        self.gun.setFont(font)
        self.saat = QLabel()
        self.saat.setAlignment(Qt.AlignCenter)
        self.saat.setFont(font)
        self.dakika = QLabel()
        self.dakika.setAlignment(Qt.AlignCenter)
        self.dakika.setFont(font)
        self.saniye = QLabel()
        self.saniye.setAlignment(Qt.AlignCenter)
        self.saniye.setFont(font)

        # adding label to the layout
        layout.addWidget(self.gun)
        layout.addWidget(self.saat)
        layout2.addWidget(self.dakika)
        layout2.addWidget(self.saniye)

        layout3 = QVBoxLayout()
        layw = QWidget()
        layw.setLayout(layout)
        lay2w = QWidget()
        lay2w.setLayout(layout2)
        layout3.addWidget(layw)
        layout3.addWidget(lay2w)
        # setting the layout to main window
        ts.setLayout(layout3)

        # creating a timer object
        timer = QTimer(self)
        # adding action to timer
        timer.timeout.connect(self.showDateTime)

        self.showDateTime()
        timer.start(1000)
        ts.exec_()
    # method called by timer
    def showDateTime(self):

        current_datetime = QDateTime.currentDateTime()
        end_datetime = QDateTime(2023, 6, 5, 0, 0, 0)
        remaining_time = current_datetime.secsTo(end_datetime)
        days, seconds = divmod(remaining_time, 86400)
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)

        self.gun.setText(str(days)+"\n Gün")
        self.saat.setText(str(hours)+"\n Saat")
        self.dakika.setText(str(minutes)+"\n Dakika")
        self.saniye.setText(str(seconds)+"\n Saniye")
# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# showing all the widgets
window.show()

# start the app
App.exit(App.exec_())
