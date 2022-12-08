import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QRadioButton, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 270, 270)
        self.setWindowTitle('Крестики нолики QT edition')
        self.first = ''
        self.second = ''
        self.rb = QRadioButton('0', self)
        self.rb.move(150, 10)
        self.rb.clicked.connect(self.new_game)
        self.rb1 = QRadioButton('X', self)
        self.rb1.move(100, 10)
        self.rb1.clicked.connect(self.new_game)
        self.field = []
        for x in range(3):
            self.row = []
            for y in range(3):
                self.btn = QPushButton('', self)
                self.btn.resize(50, 50)
                self.btn.move(50 + 55 * x, 50 + 55 * y)
                self.btn.clicked.connect(self.tip)
                self.row.append(self.btn)
            self.field.append(self.row)
        self.lbl = QLabel('', self)
        self.lbl.resize(100, 10)
        self.lbl.move(100, 220)
        self.btn1 = QPushButton('Новая игра', self)
        self.btn1.resize(140, 30)
        self.btn1.move(60, 235)
        self.btn1.clicked.connect(self.new_game)

    def new_game(self):
        self.lbl.hide()
        self.time = 0
        if self.rb1.isChecked():
            self.first = 'X'
            self.second = '0'
        else:
            self.first = '0'
            self.second = 'X'
        for row in self.field:
            for elem in row:
                elem.setEnabled(True)
                elem.setText('')

    def end(self):
        for row in self.field:
            for elem in row:
                elem.setEnabled(False)

    def tip(self):
        self.sender().setText(self.first) if self.time % 2 == 0 else self.sender().setText(self.second)
        self.time += 1
        for x in range(3):
            if {y.text() for y in self.field[x]} == {'X'} or {y.text() for y in self.field[x]} == {'0'} or \
                    {self.field[0][x].text(), self.field[1][x].text(), self.field[2][x].text()} == {'X'} or \
                    {self.field[0][x].text(), self.field[1][x].text(), self.field[2][x].text()} == {'0'}:
                self.lbl.setText('Выиграл ' + self.field[x][x].text())
                self.lbl.show()
                self.end()
                break
        if (self.field[0][0].text() == self.field[1][1].text() and
            self.field[1][1].text() == self.field[2][2].text()) or \
                (self.field[0][2].text() == self.field[1][1].text() and
                 self.field[1][1].text() == self.field[2][0].text()):
            if self.field[1][1].text():
                self.lbl.setText('Выиграл ' + self.field[1][1].text())
                self.lbl.show()
                self.end()
        else:
            self.check = set()
            for row in self.field:
                for elem in row:
                    self.check.add(elem.text())
            if '' not in self.check:
                self.lbl.setText('Ничья!')
                self.lbl.show()
                self.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())