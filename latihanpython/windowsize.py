# ===================== window management ===================
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QLabel 

class Mywindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Label = QLabel(self)
        self.Label.setText("Label1")
        self.Label.move(200, 0)
        self.button = QPushButton(self)
        self.button.setGeometry(0,0,400,400)
        self.setWindowTitle("Belajar pyQt5")
        
app = QApplication([])
window = Mywindow()
window.show()
app.exec_()
