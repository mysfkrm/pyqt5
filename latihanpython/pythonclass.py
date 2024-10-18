from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel

class Mywindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Label = QLabel(self)
        self.Label.setText("Label1")
        self.Label.move(200, 0)
        self.button = QPushButton(self)
        self.button.setText("Button1")
        
        app = QApplication([])
        window = Mywindow()
        window.show()
        app.exec_()