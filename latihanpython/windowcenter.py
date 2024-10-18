# =============================== window Management ===============================
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QLabel, QDesktopWidget

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Label = QLabel(self)
        self.Label.setText("label1")
        self.Label.move(200, 0)
        self.Button = QPushButton(self)
        self.Button.setText("button1")
        self.setGeometry(0,0,500,500)
        self.setWindowTitle("Belajar PyQt5")
        cwa = self.frameGeometry() # cek ukuran main window app kita
        cwc = QDesktopWidget().availableGeometry().center() # pada screen saya: (682,363)
        #print(cwc)
        cwa.moveCenter(cwc)
        self.move(cwa.topLeft())
        
        app = QApplication([])
        window = MyWindow()
        window.show()
        app.exec_()