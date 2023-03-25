import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QCheckBox, QVBoxLayout, QPushButton, QMessageBox, QButtonGroup
from PyQt5.QtCore import Qt
from random import choices
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import pyperclip


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.length_label = QLabel("Password Length:")
        self.length_edit = QLineEdit()
        self.length_edit.setAlignment(Qt.AlignCenter)
        self.num_check = QCheckBox("Numbers")
        self.upper_check = QCheckBox("Uppercase Letters")
        self.lower_check = QCheckBox("Lowercase Letters")
        self.special_check = QCheckBox("Special Characters")
        self.generate_button = QPushButton("Generate")
        self.password_label = QLabel("")
        self.password_label.setAlignment(Qt.AlignCenter)
        self.copy_button = QPushButton("Copy")
        self.copy_button.clicked.connect(lambda: pyperclip.copy(self.password_label.text()) if self.password_label.text() else None)

        self.groupbox = QButtonGroup()
        self.groupbox.addButton(self.upper_check)
        self.groupbox.addButton(self.lower_check)
        self.groupbox.addButton(self.special_check)
        self.groupbox.addButton(self.num_check)
        self.groupbox.setExclusive(False)

        vbox = QVBoxLayout()
        vbox.addWidget(self.length_label)
        vbox.addWidget(self.length_edit)
        vbox.addWidget(self.num_check)
        vbox.addWidget(self.upper_check)
        vbox.addWidget(self.lower_check)
        vbox.addWidget(self.special_check)
        vbox.addWidget(self.generate_button)
        vbox.addWidget(self.password_label, 0, Qt.AlignCenter)
        vbox.addWidget(self.copy_button, 0, Qt.AlignCenter)

        self.generate_button.clicked.connect(self.generate_password)

        self.setLayout(vbox)

    def generate_password(self):
        if not self.length_edit.text():
            msg = QMessageBox()
            msg.setIcon(msg.Critical)
            msg.setText("Please enter password length")
            msg.exec_()
        elif int(self.length_edit.text()) > 500:
            msg = QMessageBox()
            msg.setIcon(msg.Critical)
            msg.setText("Please shorten the length you entered")
            msg.exec_()
        elif self.groupbox.checkedButton() is None:
            msg = QMessageBox()
            msg.setIcon(msg.Critical)
            msg.setText("Please select an option")
            msg.exec_()
        else:
            length = int(self.length_edit.text())
            print(length)
            print(type(length))
            components = []
            if self.num_check.isChecked():
                components.extend(list(digits))
            if self.upper_check.isChecked():
                components.extend(list(ascii_uppercase))
            if self.lower_check.isChecked():
                components.extend(list(ascii_lowercase))
            if self.special_check.isChecked():
                components.extend(list(punctuation))
            password = "".join(choices(components, k=length))

            formatted_password = "\n".join([password[i:i + 23] for i in range(0, len(password), 30)])
            self.password_label.setText(formatted_password)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
